from repositories.interfaces.Idrivers_repository import IDriversRepository
from core.database import get_db_cursor
from typing import List, Dict, Any, Optional


class DriversRepository(IDriversRepository):
    def get_all_drivers(self) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    "driverId", 
                    "driverRef", 
                    "code" AS driver_code, 
                    "number" AS permanent_number,
                    "forename" || ' ' || "surname" AS full_name, 
                    "nationality",
                    "dob" AS date_of_birth,
                    "url" AS driver_wiki_url
                FROM public.drivers
                ORDER BY full_name ASC;
            """)
            return cur.fetchall()

    def get_driver_profile(self, driver_id: int, year: Optional[int] = None) -> Optional[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                WITH gp_stats AS (
                    SELECT
                        res."driverId",
                        COUNT(res."resultId") AS total_races_entered,
                        COUNT(CASE WHEN res."positionOrder" = 1 THEN 1 END) AS total_career_wins,
                        COUNT(CASE WHEN res."positionOrder" IN (1, 2, 3) THEN 1 END) AS total_career_podiums,
                        COALESCE(SUM(res."points"), 0) AS total_career_points,
                        COUNT(CASE WHEN res."rank" = 1 THEN 1 END) AS total_fastest_laps,
                        COUNT(
                            CASE WHEN st."status" IS NOT NULL
                                  AND st."status" NOT IN ('Finished', '+1 Lap', '+2 Laps', '+3 Laps', '+4 Laps', '+5 Laps', '+6 Laps')
                            THEN 1 END
                        ) AS total_dnfs,
                        MIN(CASE WHEN res."grid" > 0 THEN res."grid"::int END) AS highest_grid,
                        COUNT(CASE WHEN res."grid" = 1 THEN 1 END) AS grid_p1_count,
                        MIN(rc."year") AS first_year,
                        MAX(rc."year") AS last_year,
                        STRING_AGG(DISTINCT c."name", ', ' ORDER BY c."name") AS teams_driven_for
                    FROM public.results res
                    JOIN public.races rc ON res."raceId" = rc."raceId"
                    LEFT JOIN public.constructors c ON res."constructorId" = c."constructorId"
                    LEFT JOIN public.status st ON res."statusId" = st."statusId"
                    WHERE res."driverId" = %s
                    GROUP BY res."driverId"
                ),
                quali_poles AS (
                    SELECT
                        q."driverId",
                        COUNT(*) AS quali_count,
                        COUNT(CASE WHEN q."position" = 1 THEN 1 END) AS pole_count
                    FROM public.qualifying q
                    WHERE q."driverId" = %s
                    GROUP BY q."driverId"
                ),
                season_max_round AS (
                    SELECT rc."year", MAX(rc."round") AS max_round
                    FROM public.driver_standings ds
                    JOIN public.races rc ON ds."raceId" = rc."raceId"
                    GROUP BY rc."year"
                ),
                champ_titles AS (
                    SELECT
                        ds."driverId",
                        COUNT(*) AS world_championships
                    FROM public.driver_standings ds
                    JOIN public.races rc ON ds."raceId" = rc."raceId"
                    JOIN season_max_round smr ON rc."year" = smr."year" AND rc."round" = smr.max_round
                    WHERE ds."driverId" = %s
                      AND ds."position" = 1
                      AND rc."year" < EXTRACT(YEAR FROM CURRENT_DATE)::int
                    GROUP BY ds."driverId"
                )
                SELECT 
                    d."driverId",
                    d."forename" || ' ' || d."surname" AS full_name,
                    d."code" AS driver_code,
                    d."number" AS permanent_number,
                    d."dob" AS birth_date,
                    d."nationality",
                    d."url" AS driver_wiki_url,
                    COALESCE(gp.total_races_entered, 0) AS total_races_entered,
                    COALESCE(gp.total_career_wins, 0) AS total_career_wins,
                    COALESCE(gp.total_career_podiums, 0) AS total_career_podiums,
                    COALESCE(gp.total_career_points, 0) AS total_career_points,
                    CASE
                        WHEN COALESCE(qp.quali_count, 0) > 0 THEN COALESCE(qp.pole_count, 0)
                        ELSE COALESCE(gp.grid_p1_count, 0)
                    END AS total_career_poles,
                    COALESCE(gp.total_fastest_laps, 0) AS total_fastest_laps,
                    COALESCE(gp.total_dnfs, 0) AS total_dnfs,
                    COALESCE(ct.world_championships, 0) AS world_championships,
                    gp.highest_grid,
                    CASE
                        WHEN gp.first_year IS NOT NULL AND gp.last_year IS NOT NULL THEN
                            CASE WHEN gp.first_year = gp.last_year THEN gp.first_year::text
                                 ELSE gp.first_year::text || ' – ' || gp.last_year::text
                            END
                        ELSE NULL
                    END AS seasons_active,
                    gp.teams_driven_for
                FROM public.drivers d
                LEFT JOIN gp_stats gp ON d."driverId" = gp."driverId"
                LEFT JOIN quali_poles qp ON d."driverId" = qp."driverId"
                LEFT JOIN champ_titles ct ON d."driverId" = ct."driverId"
                WHERE d."driverId" = %s;
            """, (driver_id, driver_id, driver_id, driver_id))
            profile = cur.fetchone()
            if not profile:
                return None

            profile["season_year"] = None
            profile["season_position"] = None
            profile["season_points"] = None
            profile["season_team"] = None

            if year is not None:
                cur.execute("""
                    SELECT
                        ds."position"::int AS season_position,
                        ds."points" AS season_points,
                        (
                            SELECT c."name"
                            FROM public.results res2
                            JOIN public.races r2 ON res2."raceId" = r2."raceId"
                            JOIN public.constructors c ON res2."constructorId" = c."constructorId"
                            WHERE res2."driverId" = %s AND r2."year" = %s
                            ORDER BY r2."round" DESC
                            LIMIT 1
                        ) AS season_team
                    FROM public.driver_standings ds
                    JOIN public.races rc ON ds."raceId" = rc."raceId"
                    WHERE ds."driverId" = %s AND rc."year" = %s
                    ORDER BY rc."round" DESC
                    LIMIT 1;
                """, (driver_id, year, driver_id, year))
                s_row = cur.fetchone()
                if s_row:
                    profile["season_year"] = year
                    profile["season_position"] = s_row.get("season_position")
                    profile["season_points"] = s_row.get("season_points")
                    profile["season_team"] = s_row.get("season_team")

            return profile
