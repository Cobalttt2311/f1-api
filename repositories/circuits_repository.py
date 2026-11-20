from repositories.interfaces.Icircuits_repository import ICircuitsRepository
from core.database import get_db_cursor
from typing import List, Dict, Any

# Official circuit lengths (in km) keyed by Ergast circuitRef
CIRCUIT_LENGTH_KM: Dict[str, float] = {
    "albert_park": 5.278,
    "americas": 5.513,
    "bahrain": 5.412,
    "baku": 6.003,
    "catalunya": 4.657,
    "hungaroring": 4.381,
    "imola": 4.909,
    "interlagos": 4.309,
    "jeddah": 6.174,
    "losail": 5.419,
    "marina_bay": 4.940,
    "miami": 5.412,
    "monaco": 3.337,
    "monza": 5.793,
    "red_bull_ring": 4.318,
    "rodriguez": 4.304,
    "shanghai": 5.451,
    "silverstone": 5.891,
    "spa": 7.004,
    "suzuka": 5.807,
    "vegas": 6.201,
    "villeneuve": 4.361,
    "yas_marina": 5.281,
    "zandvoort": 4.259,
    "madring": 5.474,
    # Historic & recent venues
    "paul_ricard": 5.842,
    "sochi": 5.848,
    "portimao": 4.653,
    "mugello": 5.245,
    "istanbul": 5.338,
    "nurburgring": 5.148,
    "hockenheimring": 4.574,
    "sepang": 5.543,
    "buddh": 5.125,
    "yeongam": 5.615,
    "valencia": 5.419,
    "fuji": 4.563,
    "magny_cours": 4.411,
    "indianapolis": 4.192,
    "jerez": 4.428,
    "estoril": 4.360,
    "adelaide": 3.780,
    "kyalami": 4.261,
    "donington": 4.023,
    "aida": 3.703,
    "jacarepagua": 5.031,
    "galvez": 4.259,
    "brands_hatch": 3.703,
    "zolder": 4.262,
    "dijon": 3.801,
    "watkins_glen": 5.435,
    "long_beach": 3.275,
    "jarama": 3.404,
    "anderstorp": 4.018,
    "mosport": 3.957,
    "montjuic": 3.791,
    "nivelles": 3.724,
    "charade": 8.055,
    "zeltweg": 3.200,
    "reims": 8.302,
    "rouen": 6.542,
    "essarts": 6.542,
    "phoenix": 3.720,
    "dallas": 3.901,
    "detroit": 4.023,
    "las_vegas": 3.650,
    "tremblant": 4.265,
    "pedralbes": 6.316,
    "bremgarten": 7.280,
    "pescara": 25.579,
    "ain_diab": 7.618,
    "monsanto": 5.440,
    "avus": 8.300,
    "riverside": 5.271,
    "sebring": 8.356,
    "boavista": 7.775,
    "george": 3.920,
}


class CircuitsRepository(ICircuitsRepository):
    def get_all_circuits(self) -> List[Dict[str, Any]]:
        with get_db_cursor() as cur:
            cur.execute("""
                WITH circuit_race_stats AS (
                    SELECT
                        rc."circuitId",
                        MIN(rc."year") AS first_grand_prix,
                        COUNT(DISTINCT rc."raceId") AS number_of_gps
                    FROM public.races rc
                    WHERE EXISTS (
                        SELECT 1
                        FROM public.results res
                        WHERE res."raceId" = rc."raceId"
                    )
                    GROUP BY rc."circuitId"
                ),
                circuit_lap_records AS (
                    SELECT DISTINCT ON (rc."circuitId")
                        rc."circuitId",
                        res."fastestLapTime" AS lap_record_time,
                        d."forename" || ' ' || d."surname" AS lap_record_driver,
                        rc."year" AS lap_record_year
                    FROM public.results res
                    JOIN public.races rc ON res."raceId" = rc."raceId"
                    JOIN public.drivers d ON res."driverId" = d."driverId"
                    WHERE res."fastestLapTime" IS NOT NULL
                      AND res."fastestLapTime" <> ''
                      AND res."fastestLapTime" <> '\\N'
                      AND res."fastestLapTime" ~ '^[0-9]+:[0-9]{2}(\\.[0-9]+)?$'
                    ORDER BY
                        rc."circuitId",
                        (
                            split_part(res."fastestLapTime", ':', 1)::int * 60
                            + split_part(res."fastestLapTime", ':', 2)::numeric
                        ) ASC,
                        rc."year" DESC
                )
                SELECT 
                    c."circuitId", 
                    c."circuitRef", 
                    c."name" AS circuit_name, 
                    c."location", 
                    c."country",
                    c."lat" AS latitude,
                    c."lng" AS longitude,
                    c."alt" AS altitude_meters,
                    c."url" AS circuit_wiki_url,
                    crs.first_grand_prix,
                    COALESCE(crs.number_of_gps, 0) AS number_of_gps,
                    clr.lap_record_time,
                    clr.lap_record_driver,
                    clr.lap_record_year
                FROM public.circuits c
                LEFT JOIN circuit_race_stats crs ON c."circuitId" = crs."circuitId"
                LEFT JOIN circuit_lap_records clr ON c."circuitId" = clr."circuitId"
                ORDER BY c."country" ASC, c."name" ASC;
            """)
            rows = cur.fetchall()
            for row in rows:
                ref = str(row.get("circuitRef") or "").strip().lower()
                row["length_km"] = CIRCUIT_LENGTH_KM.get(ref)
            return rows

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
