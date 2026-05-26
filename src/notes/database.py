import sqlite3

DB_NAME = "notes.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def add_note(title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content)
    )

    conn.commit()
    conn.close()

def list_notes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, content
        FROM notes
        ORDER BY created_at DESC
        """
    )

    notes = cursor.fetchall()

    conn.close()

    return notes

def get_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, content FROM notes WHERE id = ?", (note_id, ))

    note = cursor.fetchone()

    conn.close()

    return note

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id, ))

    conn.commit()
    conn.close()
