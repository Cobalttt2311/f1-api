from core.database import get_db_cursor
from typing import List, Dict, Any

class SeasonsRepository:
    def get_all_seasons(self) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT "year", "url" AS season_wiki_url
                FROM public.seasons
                ORDER BY "year" DESC;
            """)
            return cur.fetchall()

    def get_season_circuits(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT DISTINCT
                    r."year",
                    r."round",
                    r."name" AS grand_prix_name,
                    c."circuitId",
                    c."name" AS circuit_name,
                    c."location",
                    c."country",
                    c."lat" AS latitude,
                    c."lng" AS longitude,
                    c."url" AS circuit_wiki_url,
                    r."url" AS race_wiki_url
                FROM public.races r
                JOIN public.circuits c ON r."circuitId" = c."circuitId"
                WHERE r."year" = %s
                ORDER BY r."round" ASC;
            """, (year,))
            return cur.fetchall()

    def get_season_drivers(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT DISTINCT
                    r."year",
                    d."driverId",
                    d."code" AS driver_code,
                    d."number" AS permanent_number,
                    d."forename" || ' ' || d."surname" AS full_name,
                    d."nationality",
                    d."url" AS driver_wiki_url
                FROM public.results res
                JOIN public.races r ON res."raceId" = r."raceId"
                JOIN public.drivers d ON res."driverId" = d."driverId"
                WHERE r."year" = %s
                ORDER BY full_name ASC;
            """, (year,))
            return cur.fetchall()

    def get_season_constructors(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT DISTINCT
                    r."year",
                    c."constructorId",
                    c."name" AS constructor_name,
                    c."nationality" AS constructor_nationality,
                    c."url" AS constructor_wiki_url
                FROM public.results res
                JOIN public.races r ON res."raceId" = r."raceId"
                JOIN public.constructors c ON res."constructorId" = c."constructorId"
                WHERE r."year" = %s
                ORDER BY constructor_name ASC;
            """, (year,))
            return cur.fetchall()

    def get_season_lineups(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT DISTINCT
                    r."year",
                    c."name" AS team_name,
                    d."forename" || ' ' || d."surname" AS driver_name,
                    d."code" AS driver_code,
                    d."number" AS car_number,
                    c."url" AS constructor_wiki_url,
                    d."url" AS driver_wiki_url
                FROM public.results res
                JOIN public.races r ON res."raceId" = r."raceId"
                JOIN public.constructors c ON res."constructorId" = c."constructorId"
                JOIN public.drivers d ON res."driverId" = d."driverId"
                WHERE r."year" = %s
                ORDER BY team_name ASC, driver_name ASC;
            """, (year,))
            return cur.fetchall()

    def get_season_winners(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    r."round",
                    r."name" AS grand_prix_name,
                    r."date" AS race_date,
                    cir."name" AS circuit_name,
                    d."forename" || ' ' || d."surname" AS winner_name,
                    c."name" AS winning_team,
                    res."time" AS winning_time,
                    res."laps" AS laps_completed,
                    r."url" AS race_wiki_url,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.results res
                JOIN public.races r ON res."raceId" = r."raceId"
                JOIN public.circuits cir ON r."circuitId" = cir."circuitId"
                JOIN public.drivers d ON res."driverId" = d."driverId"
                JOIN public.constructors c ON res."constructorId" = c."constructorId"
                WHERE r."year" = %s AND res."positionOrder" = 1
                ORDER BY r."round" ASC;
            """, (year,))
            return cur.fetchall()

    def get_season_pole_sitters(self, year: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    r."round",
                    r."name" AS grand_prix,
                    d."forename" || ' ' || d."surname" AS pole_sitter,
                    c."name" AS team_name,
                    q."q3" AS fastest_q3_lap,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.qualifying q
                JOIN public.races r ON q."raceId" = r."raceId"
                JOIN public.drivers d ON q."driverId" = d."driverId"
                JOIN public.constructors c ON q."constructorId" = c."constructorId"
                WHERE r."year" = %s AND q."position" = 1
                ORDER BY r."round" ASC;
            """, (year,))
            return cur.fetchall()
