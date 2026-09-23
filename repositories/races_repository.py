from core.database import get_db_cursor
from typing import List, Dict, Any, Optional

class RacesRepository:
    def get_race_calendar(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    r."raceId",
                    r."year",
                    r."round",
                    r."name" AS grand_prix_name,
                    c."circuitId",
                    c."name" AS circuit_name,
                    c."location",
                    c."country",
                    (r."sprint_date" IS NOT NULL AND r."sprint_date" != '' AND r."sprint_date" NOT LIKE '%%N%%') AS has_sprint,
                    -- Main Race (UTC)
                    r."date" AS race_date,
                    r."time" AS race_time_utc,
                    -- Free Practices (UTC)
                    r."fp1_date",
                    r."fp1_time" AS fp1_time_utc,
                    r."fp2_date",
                    r."fp2_time" AS fp2_time_utc,
                    r."fp3_date",
                    r."fp3_time" AS fp3_time_utc,
                    -- Qualifying & Sprint (UTC)
                    r."quali_date",
                    r."quali_time" AS quali_time_utc,
                    r."sprint_date",
                    r."sprint_time" AS sprint_time_utc,
                    r."url" AS race_wiki_url,
                    c."url" AS circuit_wiki_url
                FROM public.races r
                JOIN public.circuits c ON r."circuitId" = c."circuitId"
                WHERE r."year" = %s
                ORDER BY r."round" ASC;
            """, (year,))
            return cur.fetchall()

    def get_practice_schedule(self, year: int, round_no: int) -> Optional[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    r."raceId",
                    r."year",
                    r."round",
                    r."name" AS grand_prix_name,
                    c."name" AS circuit_name,
                    c."country",
                    -- Free Practices (UTC)
                    r."fp1_date",
                    r."fp1_time" AS fp1_time_utc,
                    r."fp2_date",
                    r."fp2_time" AS fp2_time_utc,
                    r."fp3_date",
                    r."fp3_time" AS fp3_time_utc,
                    r."url" AS race_wiki_url
                FROM public.races r
                JOIN public.circuits c ON r."circuitId" = c."circuitId"
                WHERE r."year" = %s AND r."round" = %s;
            """, (year, round_no))
            return cur.fetchone()

    def get_sprint_schedule(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    r."raceId",
                    r."year",
                    r."round",
                    r."name" AS grand_prix_name,
                    c."name" AS circuit_name,
                    c."country",
                    -- Sprint (UTC)
                    r."sprint_date",
                    r."sprint_time" AS sprint_time_utc,
                    -- Main Race (UTC)
                    r."date" AS main_race_date,
                    r."time" AS main_race_time_utc,
                    r."url" AS race_wiki_url
                FROM public.races r
                JOIN public.circuits c ON r."circuitId" = c."circuitId"
                WHERE r."year" = %s 
                  AND r."sprint_date" IS NOT NULL AND r."sprint_date" != '' AND r."sprint_date" NOT LIKE '%%N%%'
                ORDER BY r."round" ASC;
            """, (year,))
            return cur.fetchall()

    def get_race_results(self, year: int, round_no: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    r."positionText" AS finish_position,
                    d."number" AS car_number,
                    d."code" AS driver_code,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    r."grid" AS starting_grid,
                    r."laps" AS laps_completed,
                    r."time" AS race_time_or_gap,
                    r."points" AS points_awarded,
                    s."status",
                    r."fastestLapTime" AS fastest_lap_time,
                    r."rank" AS fastest_lap_rank,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                JOIN public.constructors c ON r."constructorId" = c."constructorId"
                JOIN public.status s ON r."statusId" = s."statusId"
                WHERE rc."year" = %s AND rc."round" = %s
                ORDER BY r."positionOrder" ASC;
            """, (year, round_no))
            return cur.fetchall()

    def get_qualifying_results(self, year: int, round_no: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    q."position" AS qualifying_position,
                    d."number" AS car_number,
                    d."code" AS driver_code,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    q."q1" AS q1_time,
                    q."q2" AS q2_time,
                    q."q3" AS q3_time,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.qualifying q
                JOIN public.races rc ON q."raceId" = rc."raceId"
                JOIN public.drivers d ON q."driverId" = d."driverId"
                JOIN public.constructors c ON q."constructorId" = c."constructorId"
                WHERE rc."year" = %s AND rc."round" = %s
                ORDER BY q."position" ASC;
            """, (year, round_no))
            return cur.fetchall()

    def get_sprint_results(self, year: int, round_no: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    sr."positionText" AS finish_position,
                    d."number" AS car_number,
                    d."code" AS driver_code,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    sr."grid" AS starting_grid,
                    sr."laps" AS laps_completed,
                    sr."time" AS time_or_gap,
                    sr."points" AS points_awarded,
                    s."status",
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.sprint_results sr
                JOIN public.races rc ON sr."raceId" = rc."raceId"
                JOIN public.drivers d ON sr."driverId" = d."driverId"
                JOIN public.constructors c ON sr."constructorId" = c."constructorId"
                JOIN public.status s ON sr."statusId" = s."statusId"
                WHERE rc."year" = %s AND rc."round" = %s
                ORDER BY sr."positionOrder" ASC;
            """, (year, round_no))
            return cur.fetchall()

    def get_pit_stops(self, year: int, round_no: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    ps."stop" AS stop_number,
                    ps."lap",
                    ps."time" AS time_of_day_utc,
                    d."code" AS driver_code,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    ps."duration" AS stop_duration_seconds,
                    ps."milliseconds" AS total_stop_milliseconds,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.pit_stops ps
                JOIN public.races rc ON ps."raceId" = rc."raceId"
                JOIN public.drivers d ON ps."driverId" = d."driverId"
                JOIN public.results r ON (r."raceId" = ps."raceId" AND r."driverId" = ps."driverId")
                JOIN public.constructors c ON r."constructorId" = c."constructorId"
                WHERE rc."year" = %s AND rc."round" = %s
                ORDER BY ps."lap" ASC, ps."stop" ASC;
            """, (year, round_no))
            return cur.fetchall()

    def get_starting_grid(self, year: int, race_id: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    CASE 
                        WHEN r."grid" = 0 THEN 'PL' 
                        ELSE CAST(r."grid" AS TEXT) 
                    END AS starting_grid_position,
                    d."number" AS car_number,
                    d."code" AS driver_code,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    c."name" AS team_name,
                    q."position" AS qualifying_position,
                    COALESCE(q."q3", q."q2", q."q1") AS qualifying_best_lap,
                    CASE 
                        WHEN r."grid" = 0 THEN 'Started from Pit Lane'
                        WHEN q."position" IS NULL THEN 'Unclassified in Qualifying'
                        WHEN r."grid" > q."position" THEN '+' || CAST(r."grid" - q."position" AS TEXT) || ' Places Grid Penalty'
                        WHEN r."grid" < q."position" THEN '-' || CAST(q."position" - r."grid" AS TEXT) || ' Grid Promotion'
                        ELSE 'As Qualified'
                    END AS grid_status,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url,
                    rc."url" AS race_wiki_url
                FROM public.results r
                JOIN public.races rc ON r."raceId" = rc."raceId"
                JOIN public.drivers d ON r."driverId" = d."driverId"
                JOIN public.constructors c ON r."constructorId" = c."constructorId"
                LEFT JOIN public.qualifying q ON (r."raceId" = q."raceId" AND r."driverId" = q."driverId")
                WHERE rc."year" = %s AND rc."raceId" = %s
                ORDER BY (CASE WHEN r."grid" = 0 THEN 999 ELSE r."grid" END) ASC;
            """, (year, race_id))
            return cur.fetchall()

    def get_lap_chart(self, year: int, round_no: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    lt."lap",
                    lt."position" AS track_position,
                    d."code" AS driver_code,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    lt."time" AS lap_time_str,
                    lt."milliseconds" AS lap_time_ms
                FROM public.lap_times lt
                JOIN public.races rc ON lt."raceId" = rc."raceId"
                JOIN public.drivers d ON lt."driverId" = d."driverId"
                WHERE rc."year" = %s AND rc."round" = %s
                ORDER BY lt."lap" ASC, lt."position" ASC;
            """, (year, round_no))
            return cur.fetchall()
