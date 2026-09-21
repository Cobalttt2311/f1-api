"""
Database Connection & Context Manager
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from core.config import settings

@contextmanager
def get_db_cursor():
    """
    Context manager for safe PostgreSQL connection handling with dict results.
    Automatically commits and closes connections.
    """
    conn = psycopg2.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT
    )
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
