from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DB_PATH = 'data/kasvihuone.db'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    range_sel = request.args.get('range', 'day')
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if range_sel == 'day':
        c.execute("""
            SELECT timestamp, temperature FROM temperature_log 
            WHERE timestamp >= datetime('now', '-1 day')
            ORDER BY timestamp
        """)
    elif range_sel == 'week':
        c.execute("""
            SELECT timestamp, temperature FROM temperature_log 
            WHERE timestamp >= datetime('now', '-7 day')
            ORDER BY timestamp
        """)
    rows = c.fetchall()
    conn.close()

    labels = [r[0][11:16] for r in rows]  # Näytetään kellonaika
    temps = [round(r[1], 2) for r in rows]

    if temps:
        max_temp = max(temps)
        min_temp = min(temps)
        avg_temp = round(sum(temps)/len(temps), 2)
    else:
        max_temp = min_temp = avg_temp = 0

    return jsonify({'labels': labels, 'temps': temps, 'max': max_temp, 'min': min_temp, 'avg': avg_temp})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
