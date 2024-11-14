import random
import pyautogui
from PIL import ImageGrab
ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'
device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = None #if None, device_id = MAC address
device_name = None
exec_interval = 1 # IDF/ODF interval

def Dummy_Sensor(): # 取得滑鼠當前位置
    x, y = pyautogui.position()
    screen = ImageGrab.grab()
    r, g, b = screen.getpixel((x, y))
    r = 255#(r / 255) * 100
    g = 192#(g / 255) * 100
    b = 203#(b / 255) * 100
    print(f"Mouse Position: ({x}, {y}), Color: (R: {r}, G: {g}, B: {b})")
    return r, g, b


def Dummy_Control(data:list):
    print(data[0])

def on_register(r):
    print(f'Device name: {r["d_name"]}')