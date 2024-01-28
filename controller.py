import serial
import time
import pyautogui as pui

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(5)

def read_sensor_data():
    try:
        while True:
            time.sleep(1)
            distance_str = ser.readline().decode('utf-8').rstrip()
            distance_cm = int(distance_str)
            print(f'Distance: {distance_cm} cm')
            if distance_cm >= 100:
                pass
            elif distance_cm <= 10:
                pui.press('up')
            elif 10<distance_cm < 22:
                pui.press('down')
            elif distance_cm >= 22:
                pui.press('space')
                time.sleep(0.5)
            else:
                pass

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Stopping the program.")
        ser.close()

if __name__ == "__main__":
    read_sensor_data()
