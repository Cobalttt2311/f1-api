from core.database import get_db_cursor
from typing import List, Dict, Any

class ConstructorsRepository:
    def get_all_constructors(self) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                SELECT 
                    "constructorId", 
                    "constructorRef", 
                    "name" AS constructor_name, 
                    "nationality" AS constructor_nationality,
                    "url" AS constructor_wiki_url
                FROM public.constructors
                ORDER BY "name" ASC;
            """)
            return cur.fetchall()
