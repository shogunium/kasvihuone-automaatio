from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

DB_PATH = 'data/kasvihuone.db'

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT timestamp, temperature FROM temperature_log ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()

    html = """
    <h1>Kasvihuoneen lämpötilat</h1>
    <table border="1">
        <tr><th>Aikaleima</th><th>Lämpötila (°C)</th></tr>
        {% for row in rows %}
        <tr><td>{{ row[0] }}</td><td>{{ "%.2f"|format(row[1]) }}</td></tr>
        {% endfor %}
    </table>
    """
    return render_template_string(html, rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
