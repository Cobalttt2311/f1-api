from core.database import get_db_cursor
from typing import List, Dict, Any

class StandingsRepository:

    def get_latest_driver_standings(self) -> List[Dict[str, Any]]:
        query = """
        SELECT 
            lr."year" AS season,
            lr."round" AS after_round,
            lr."race_name" AS after_grand_prix,
            ds."position" AS championship_rank,
            d."code" AS driver_code,
            d."forename" || ' ' || d."surname" AS driver_name,
            d."nationality",
            COALESCE(c."name", 'Unknown') AS team_name,
            ds."points" AS total_points,
            ds."wins" AS total_wins,
            d."url" AS driver_wiki_url,
            c."url" AS constructor_wiki_url
        FROM public.driver_standings ds
        JOIN (
            SELECT r."raceId", r."year", r."round", r."name" AS race_name, r."date"
            FROM public.races r
            JOIN public.driver_standings ds ON r."raceId" = ds."raceId"
            ORDER BY r."date" DESC, r."round" DESC
            LIMIT 1
        ) lr ON ds."raceId" = lr."raceId"
        JOIN public.drivers d ON ds."driverId" = d."driverId"
        LEFT JOIN LATERAL (
            SELECT c."name", c."url"
            FROM public.results res
            JOIN public.constructors c ON res."constructorId" = c."constructorId"
            JOIN public.races r ON res."raceId" = r."raceId"
            WHERE res."driverId" = ds."driverId" AND r."year" = lr."year" AND r."round" <= lr."round"
            ORDER BY r."round" DESC
            LIMIT 1
        ) c ON true
        ORDER BY ds."position" ASC;
        """
        with get_db_cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def get_latest_constructor_standings(self) -> List[Dict[str, Any]]:
        query = """
        SELECT 
            lr."year" AS season,
            lr."round" AS after_round,
            lr."race_name" AS after_grand_prix,
            cs."position" AS championship_rank,
            c."name" AS constructor_name,
            c."nationality",
            cs."points" AS total_points,
            cs."wins" AS total_wins,
            c."url" AS constructor_wiki_url
        FROM public.constructor_standings cs
        JOIN (
            SELECT r."raceId", r."year", r."round", r."name" AS race_name, r."date"
            FROM public.races r
            JOIN public.constructor_standings cs ON r."raceId" = cs."raceId"
            ORDER BY r."date" DESC, r."round" DESC
            LIMIT 1
        ) lr ON cs."raceId" = lr."raceId"
        JOIN public.constructors c ON cs."constructorId" = c."constructorId"
        ORDER BY cs."position" ASC;
        """
        with get_db_cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def get_season_driver_standings(self, year: int) -> List[Dict[str, Any]]:
        query = """
        SELECT 
            r."year" AS season,
            r."round" AS after_round,
            r."name" AS after_grand_prix,
            ds."position" AS championship_rank,
            d."code" AS driver_code,
            d."forename" || ' ' || d."surname" AS driver_name,
            d."nationality",
            COALESCE(c."name", 'Unknown') AS team_name,
            ds."points" AS total_points,
            ds."wins" AS total_wins,
            d."url" AS driver_wiki_url,
            c."url" AS constructor_wiki_url
        FROM public.driver_standings ds
        JOIN public.races r ON ds."raceId" = r."raceId"
        JOIN public.drivers d ON ds."driverId" = d."driverId"
        LEFT JOIN LATERAL (
            SELECT c."name", c."url"
            FROM public.results res
            JOIN public.constructors c ON res."constructorId" = c."constructorId"
            JOIN public.races r2 ON res."raceId" = r2."raceId"
            WHERE res."driverId" = ds."driverId" AND r2."year" = r."year" AND r2."round" <= r."round"
            ORDER BY r2."round" DESC
            LIMIT 1
        ) c ON true
        WHERE r."year" = %s 
  AND r."round" = (
      SELECT MAX(r2."round") 
      FROM public.races r2 
      JOIN public.driver_standings ds2 ON r2."raceId" = ds2."raceId" 
      WHERE r2."year" = %s
  )
        ORDER BY ds."position" ASC;
        """
        with get_db_cursor() as cur:
            cur.execute(query, (year, year))
            return cur.fetchall()

    def get_season_constructor_standings(self, year: int) -> List[Dict[str, Any]]:
        query = """
        SELECT 
            r."year" AS season,
            r."round" AS after_round,
            r."name" AS after_grand_prix,
            cs."position" AS championship_rank,
            c."name" AS constructor_name,
            c."nationality",
            cs."points" AS total_points,
            cs."wins" AS total_wins,
            c."url" AS constructor_wiki_url
        FROM public.constructor_standings cs
        JOIN public.races r ON cs."raceId" = r."raceId"
        JOIN public.constructors c ON cs."constructorId" = c."constructorId"
        WHERE r."year" = %s 
  AND r."round" = (
      SELECT MAX(r2."round") 
      FROM public.races r2 
      JOIN public.constructor_standings cs2 ON r2."raceId" = cs2."raceId" 
      WHERE r2."year" = %s
  )
        ORDER BY cs."position" ASC;
        """
        with get_db_cursor() as cur:
            cur.execute(query, (year, year))
            return cur.fetchall()
