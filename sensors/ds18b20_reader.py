import glob

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

if __name__ == "__main__":
    temp = read_temperature()
    if temp:
        print(f"Lämpötila: {temp:.2f} °C")
    else:
        print("Lämpötilan luku epäonnistui")

