import os
import glob
import sqlite3

# Määritellään polku tietokantaan dynaamisesti
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data/kasvihuone.db')

def read_temperature():
    device_folder = glob.glob('/sys/bus/w1/devices/28-*')[0]
    device_file = device_folder + '/w1_slave'

    with open(device_file, 'r') as f:
        lines = f.readlines()

    if lines[0].strip()[-3:] != 'YES':
        return None

    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def save_to_db(temp):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO temperature_log (temperature) VALUES (?)", (temp,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    temp = read_temperature()
    if temp:
        print(f"Lämpötila: {temp:.2f} °C")
        save_to_db(temp)
    else:
        print("Lämpötilan luku epäonnistui")
