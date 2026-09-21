from core.database import get_db_cursor
from typing import List, Dict, Any, Optional

class DriversRepository:
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

    def get_driver_profile(self, driver_id: int) -> Optional[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    d."driverId",
                    d."forename" || ' ' || d."surname" AS full_name,
                    d."code" AS driver_code,
                    d."number" AS permanent_number,
                    d."dob" AS birth_date,
                    d."nationality",
                    d."url" AS driver_wiki_url,
                    COUNT(res."resultId") AS total_races_entered,
                    COUNT(CASE WHEN res."positionOrder" = 1 THEN 1 END) AS total_career_wins,
                    COUNT(CASE WHEN res."positionOrder" IN (1, 2, 3) THEN 1 END) AS total_career_podiums,
                    COALESCE(SUM(res."points"), 0) AS total_career_points
                FROM public.drivers d
                LEFT JOIN public.results res ON d."driverId" = res."driverId"
                WHERE d."driverId" = %s
                GROUP BY d."driverId", d."forename", d."surname", d."code", d."number", d."dob", d."nationality", d."url";
            """, (driver_id,))
            return cur.fetchone()
