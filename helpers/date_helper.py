"""
Date & Timezone Conversion Helper
Converts UTC times from database to localized timezones (e.g., WIB / UTC+7).
"""

from datetime import datetime, timedelta
from typing import Optional, Dict, Any


class DateHelper:
    @staticmethod
    def utc_to_wib_time(utc_time: Optional[str], date_str: Optional[str] = None) -> Optional[str]:
        """
        Converts a UTC time string ('HH:MM:SS') to Western Indonesia Time (WIB, UTC+7) 'HH:MM:SS'.
        """
        if not utc_time or str(utc_time).strip().lower() in ["none", "null", "nan", "\\n", ""]:
            return None

        try:
            clean_time = str(utc_time).strip()[:8]
            if len(clean_time) == 5:
                clean_time += ":00"

            if date_str and str(date_str).strip().lower() not in ["none", "null", "nan", "\\n", ""]:
                clean_date = str(date_str).strip()[:10]
                dt = datetime.strptime(f"{clean_date} {clean_time}", "%Y-%m-%d %H:%M:%S")
                wib_dt = dt + timedelta(hours=7)
                return wib_dt.strftime("%H:%M:%S")
            else:
                t = datetime.strptime(clean_time, "%H:%M:%S")
                wib_t = t + timedelta(hours=7)
                return wib_t.strftime("%H:%M:%S")
        except Exception:
            return None

    @staticmethod
    def utc_to_wib_datetime(date_str: Optional[str], utc_time: Optional[str]) -> Optional[str]:
        """
        Converts UTC date and time strings into a full WIB datetime string ('YYYY-MM-DD HH:MM:SS').
        """
        if not date_str or not utc_time or str(utc_time).strip().lower() in ["none", "null", "nan", "\\n", ""]:
            return None

        try:
            clean_date = str(date_str).strip()[:10]
            clean_time = str(utc_time).strip()[:8]
            if len(clean_time) == 5:
                clean_time += ":00"

            dt = datetime.strptime(f"{clean_date} {clean_time}", "%Y-%m-%d %H:%M:%S")
            wib_dt = dt + timedelta(hours=7)
            return wib_dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return None

    @classmethod
    def enrich_race_calendar_item(cls, row: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculates and injects all WIB localized time fields for a race calendar dictionary.
        """
        data = dict(row)
        # Main Race
        data["race_time_wib"] = cls.utc_to_wib_time(data.get("race_time_utc"), data.get("race_date"))
        data["race_datetime_wib"] = cls.utc_to_wib_datetime(data.get("race_date"), data.get("race_time_utc"))

        # Free Practices
        data["fp1_time_wib"] = cls.utc_to_wib_time(data.get("fp1_time_utc"), data.get("fp1_date"))
        data["fp2_time_wib"] = cls.utc_to_wib_time(data.get("fp2_time_utc"), data.get("fp2_date"))
        data["fp3_time_wib"] = cls.utc_to_wib_time(data.get("fp3_time_utc"), data.get("fp3_date"))

        # Qualifying & Sprint
        data["quali_time_wib"] = cls.utc_to_wib_time(data.get("quali_time_utc"), data.get("quali_date"))
        data["sprint_time_wib"] = cls.utc_to_wib_time(data.get("sprint_time_utc"), data.get("sprint_date"))

        return data

    @classmethod
    def enrich_practice_schedule_item(cls, row: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculates and injects WIB localized practice times.
        """
        data = dict(row)
        data["fp1_time_wib"] = cls.utc_to_wib_time(data.get("fp1_time_utc"), data.get("fp1_date"))
        data["fp2_time_wib"] = cls.utc_to_wib_time(data.get("fp2_time_utc"), data.get("fp2_date"))
        data["fp3_time_wib"] = cls.utc_to_wib_time(data.get("fp3_time_utc"), data.get("fp3_date"))
        return data

    @classmethod
    def enrich_sprint_schedule_item(cls, row: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculates and injects WIB localized sprint and main race times.
        """
        data = dict(row)
        data["sprint_time_wib"] = cls.utc_to_wib_time(data.get("sprint_time_utc"), data.get("sprint_date"))
        data["sprint_datetime_wib"] = cls.utc_to_wib_datetime(data.get("sprint_date"), data.get("sprint_time_utc"))
        data["main_race_time_wib"] = cls.utc_to_wib_time(data.get("main_race_time_utc"), data.get("main_race_date"))
        return data
