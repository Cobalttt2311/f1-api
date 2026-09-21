from core.database import get_db_cursor
from typing import List, Dict, Any

class AnalyticsRepository:
    def get_biggest_movers(self, year: int, limit: int = 10) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    rc."year",
                    rc."name" AS grand_prix,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    r."grid" AS starting_grid,
                    r."positionOrder" AS finish_position,
                    (r."grid" - r."positionOrder") AS positions_gained,
                    d."url" AS driver_wiki_url,
                    rc."url" AS race_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                JOIN public.constructors c ON r."constructorId" = c."constructorId"
                WHERE r."grid" > 0 AND r."positionOrder" > 0 
                  AND rc."year" = %s
                ORDER BY positions_gained DESC
                LIMIT %s;
            """, (year, limit))
            return cur.fetchall()

    def get_pit_stop_efficiency(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    c."name" AS team_name,
                    COUNT(ps."stop") AS total_pit_stops,
                    ROUND(AVG(CAST(ps."duration" AS NUMERIC)), 2) AS avg_duration_seconds,
                    MIN(CAST(ps."duration" AS NUMERIC)) AS fastest_stop_seconds,
                    c."url" AS constructor_wiki_url
                FROM public.pit_stops ps
                JOIN public.races rc ON ps."raceId" = rc."raceId"
                JOIN public.results r ON (r."raceId" = ps."raceId" AND r."driverId" = ps."driverId")
                JOIN public.constructors c ON r."constructorId" = c."constructorId"
                WHERE rc."year" = %s 
                  AND ps."duration" ~ '^[0-9]+(\.[0-9]+)?$'
                GROUP BY c."name", c."url"
                ORDER BY avg_duration_seconds ASC;
            """, (year,))
            return cur.fetchall()

    def get_pole_to_win_rate(self, start_year: int = 2015) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    rc."year",
                    COUNT(*) AS total_races,
                    COUNT(CASE WHEN r."positionOrder" = 1 THEN 1 END) AS pole_and_won_count,
                    ROUND(
                        COUNT(CASE WHEN r."positionOrder" = 1 THEN 1 END) * 100.0 / COUNT(*), 
                        2
                    ) AS pole_to_win_percentage
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                WHERE r."grid" = 1 
                  AND rc."year" >= %s
                GROUP BY rc."year"
                ORDER BY rc."year" DESC;
            """, (start_year,))
            return cur.fetchall()

    def get_high_dnf_circuits(self, limit: int = 10) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    c."name" AS circuit_name,
                    c."country",
                    COUNT(r."resultId") AS total_dnf_incidents,
                    c."url" AS circuit_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.circuits c ON rc."circuitId" = c."circuitId"
                JOIN public.status s ON r."statusId" = s."statusId"
                WHERE s."status" NOT IN ('Finished', '+1 Lap', '+2 Laps', '+3 Laps', '+4 Laps', '+5 Laps', '+6 Laps')
                GROUP BY c."name", c."country", c."url"
                ORDER BY total_dnf_incidents DESC
                LIMIT %s;
            """, (limit,))
            return cur.fetchall()

    def get_deep_grid_wins(self, min_grid: int = 10, limit: int = 10) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    rc."year",
                    rc."name" AS grand_prix,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    r."grid" AS starting_grid_position,
                    d."url" AS driver_wiki_url,
                    rc."url" AS race_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                JOIN public.constructors c ON r."constructorId" = c."constructorId"
                WHERE r."positionOrder" = 1 
                  AND r."grid" >= %s
                ORDER BY r."grid" DESC
                LIMIT %s;
            """, (min_grid, limit))
            return cur.fetchall()

    def get_most_laps_led(self, limit: int = 15) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    d."forename" || ' ' || d."surname" AS driver_name,
                    COUNT(lt."lap") AS total_laps_led,
                    d."url" AS driver_wiki_url
                FROM public.lap_times lt
                JOIN public.drivers d ON lt."driverId" = d."driverId"
                WHERE lt."position" = 1
                GROUP BY d."driverId", d."forename", d."surname", d."url"
                ORDER BY total_laps_led DESC
                LIMIT %s;
            """, (limit,))
            return cur.fetchall()

    def get_fastest_speeds(self, limit: int = 10) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    rc."year",
                    rc."name" AS grand_prix,
                    c."name" AS circuit_name,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    r."fastestLapSpeed" AS max_speed_kmh,
                    r."fastestLapTime",
                    d."url" AS driver_wiki_url,
                    c."url" AS circuit_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.circuits c ON rc."circuitId" = c."circuitId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                WHERE r."fastestLapSpeed" IS NOT NULL
                ORDER BY r."fastestLapSpeed" DESC
                LIMIT %s;
            """, (limit,))
            return cur.fetchall()

    def get_all_time_winners(self, limit: int = 15) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    d."forename" || ' ' || d."surname" AS driver_name,
                    d."nationality",
                    COUNT(*) AS total_race_wins,
                    d."url" AS driver_wiki_url
                FROM public.results res
                JOIN public.drivers d ON res."driverId" = d."driverId"
                WHERE res."positionOrder" = 1
                GROUP BY d."driverId", d."forename", d."surname", d."nationality", d."url"
                ORDER BY total_race_wins DESC
                LIMIT %s;
            """, (limit,))
            return cur.fetchall()

    def get_teammate_qualifying(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                WITH team_quali AS (
                    SELECT 
                        rc."year",
                        q."raceId",
                        c."name" AS team_name,
                        q."driverId",
                        d."forename" || ' ' || d."surname" AS driver_name,
                        q."position" AS quali_pos,
                        ROW_NUMBER() OVER (PARTITION BY q."raceId", q."constructorId" ORDER BY q."position" ASC) AS team_rank
                    FROM public.qualifying q
                    JOIN public.races rc ON q."raceId" = rc."raceId"
                    JOIN public.drivers d ON q."driverId" = d."driverId"
                    JOIN public.constructors c ON q."constructorId" = c."constructorId"
                    WHERE rc."year" = %s
                )
                SELECT 
                    team_name,
                    driver_name,
                    COUNT(CASE WHEN team_rank = 1 THEN 1 END) AS outqualified_teammate_count,
                    COUNT(*) AS total_sessions_entered
                FROM team_quali
                GROUP BY team_name, driver_name
                ORDER BY team_name ASC, outqualified_teammate_count DESC;
            """, (year,))
            return cur.fetchall()

    def get_driver_form(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                WITH driver_races AS (
                    SELECT 
                        rc."year",
                        rc."round",
                        rc."name" AS grand_prix,
                        d."forename" || ' ' || d."surname" AS driver_name,
                        r."points",
                        AVG(r."points") OVER (
                            PARTITION BY r."driverId" 
                            ORDER BY rc."date", rc."round" 
                            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
                        ) AS rolling_avg_points_5_races
                    FROM public.results r
                    JOIN public.races rc ON r."raceId" = rc."raceId"
                    JOIN public.drivers d ON r."driverId" = d."driverId"
                    WHERE rc."year" = %s
                )
                SELECT * FROM driver_races 
                ORDER BY "round" ASC, rolling_avg_points_5_races DESC;
            """, (year,))
            return cur.fetchall()

    def get_points_progression(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    rc."round",
                    rc."name" AS grand_prix,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    r."points" AS race_points,
                    SUM(r."points") OVER (
                        PARTITION BY r."driverId" 
                        ORDER BY rc."round" ASC
                    ) AS cumulative_season_points
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                WHERE rc."year" = %s
                ORDER BY rc."round" ASC, cumulative_season_points DESC;
            """, (year,))
            return cur.fetchall()

    def get_constructor_one_twos(self) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                WITH team_top_two AS (
                    SELECT 
                        rc."year",
                        rc."round",
                        rc."name" AS grand_prix,
                        c."name" AS team_name,
                        COUNT(CASE WHEN r."positionOrder" IN (1, 2) THEN 1 END) AS top_2_count
                    FROM public.results r
                    JOIN public.races rc ON r."raceId" = rc."raceId"
                    JOIN public.constructors c ON r."constructorId" = c."constructorId"
                    GROUP BY rc."year", rc."round", rc."name", c."name"
                    HAVING COUNT(CASE WHEN r."positionOrder" IN (1, 2) THEN 1 END) = 2
                )
                SELECT 
                    team_name,
                    "year",
                    COUNT(*) AS total_one_two_finishes
                FROM team_top_two
                GROUP BY team_name, "year"
                ORDER BY total_one_two_finishes DESC;
            """)
            return cur.fetchall()

    def get_youngest_winners(self, limit: int = 10) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    d."forename" || ' ' || d."surname" AS driver_name,
                    d."dob" AS birth_date,
                    rc."date" AS race_date,
                    rc."name" AS grand_prix,
                    rc."year",
                    DATE_PART('year', AGE(TO_DATE(rc."date", 'YYYY-MM-DD'), TO_DATE(d."dob", 'YYYY-MM-DD'))) AS age_years,
                    DATE_PART('month', AGE(TO_DATE(rc."date", 'YYYY-MM-DD'), TO_DATE(d."dob", 'YYYY-MM-DD'))) AS age_months,
                    DATE_PART('day', AGE(TO_DATE(rc."date", 'YYYY-MM-DD'), TO_DATE(d."dob", 'YYYY-MM-DD'))) AS age_days,
                    d."url" AS driver_wiki_url,
                    rc."url" AS race_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                WHERE r."positionOrder" = 1 
                  AND rc."date" IS NOT NULL AND rc."date" != '' 
                  AND d."dob" IS NOT NULL AND d."dob" != ''
                ORDER BY AGE(TO_DATE(rc."date", 'YYYY-MM-DD'), TO_DATE(d."dob", 'YYYY-MM-DD')) ASC
                LIMIT %s;
            """, (limit,))
            return cur.fetchall()

    def get_circuit_masters(self, limit: int = 15) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    c."name" AS circuit_name,
                    c."country",
                    d."forename" || ' ' || d."surname" AS driver_name,
                    COUNT(*) AS total_wins_at_circuit,
                    c."url" AS circuit_wiki_url,
                    d."url" AS driver_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.circuits c ON rc."circuitId" = c."circuitId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                WHERE r."positionOrder" = 1
                GROUP BY c."circuitId", c."name", c."country", c."url", d."driverId", d."forename", d."surname", d."url"
                ORDER BY total_wins_at_circuit DESC
                LIMIT %s;
            """, (limit,))
            return cur.fetchall()
