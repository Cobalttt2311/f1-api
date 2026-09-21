from core.database import get_db_cursor
from typing import List, Dict, Any

class CircuitsRepository:
    def get_all_circuits(self) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    "circuitId", 
                    "circuitRef", 
                    "name" AS circuit_name, 
                    "location", 
                    "country",
                    "lat" AS latitude,
                    "lng" AS longitude,
                    "alt" AS altitude_meters,
                    "url" AS circuit_wiki_url
                FROM public.circuits
                ORDER BY "country" ASC, "name" ASC;
            """)
            return cur.fetchall()

    def get_circuit_history(self, circuit_id: int) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    rc."year",
                    rc."name" AS grand_prix_name,
                    d."forename" || ' ' || d."surname" AS winner_name,
                    c."name" AS winning_team,
                    res."time" AS winning_time,
                    rc."url" AS race_wiki_url,
                    d."url" AS driver_wiki_url,
                    c."url" AS constructor_wiki_url
                FROM public.results res
                JOIN public.races rc ON res."raceId" = rc."raceId"
                JOIN public.drivers d ON res."driverId" = d."driverId"
                JOIN public.constructors c ON res."constructorId" = c."constructorId"
                WHERE rc."circuitId" = %s
                  AND res."positionOrder" = 1
                ORDER BY rc."year" DESC;
            """, (circuit_id,))
            return cur.fetchall()
