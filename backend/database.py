import sqlite3

def get_db_connection():
    conn = sqlite3.connect('myface_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities (
        record_id TEXT PRIMARY KEY,
        user_id TEXT,
        activity_name TEXT,
        emotion TEXT,
        flow_score INTEGER,
        timestamp DATETIME,
        memo TEXT
    )
    """)
    
    conn.commit()
    conn.close()