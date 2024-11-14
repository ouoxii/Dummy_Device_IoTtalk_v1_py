import random
import pyautogui
from PIL import ImageGrab
import time

# 定義顏色的 RGB 值
colors = [
    (255, 0, 0),      # 紅
    (255, 165, 0),    # 橙
    (255, 255, 0),    # 黃
    (0, 255, 0),      # 綠
    (0, 0, 255),      # 藍
    (75, 0, 130),     # 靛
    (238, 130, 238),  # 紫
    (255, 255, 255)   # 白
]

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

# 初始化計數器
color_index = 0

def Dummy_Sensor():
    global color_index

    # 取得當前顏色
    r, g, b = colors[color_index]
    print(f"Returning Color: (R: {r}, G: {g}, B: {b})")

    # 更新 index 並模 8 以輪流選擇顏色
    color_index = (color_index + 1) % len(colors)

    # 每隔兩秒返回新的顏色
    time.sleep(1.5)
    return r, g, b

def Dummy_Control(data:list):
    print(data[0])

def on_register(r):
    print(f'Device name: {r["d_name"]}')