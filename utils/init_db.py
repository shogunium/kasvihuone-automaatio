import sqlite3

def create_db():
    conn = sqlite3.connect('data/kasvihuone.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS temperature_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("Tietokanta ja taulu varmistettu.")
