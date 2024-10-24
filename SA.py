import random

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
exec_interval = 1  # IDF/ODF interval

# 設定兩個全域變數用來追蹤遞增和遞減的數值
increasing = True  # 用來控制是遞增還是遞減
value = 0  # 初始值

def Dummy_Sensor():
    global value, increasing

    if increasing:
        value += 10
        if value >= 100:  # 當達到 100 時開始遞減
            increasing = False
    else:
        value -= 10
        if value <= 0:  # 當降到 0 時開始遞增
            increasing = True

    return value, value

def Dummy_Control(data:list):
    print(data[0])

def on_register(r):
    print(f'Device name: {r["d_name"]}')
    '''
    #You can write some SA routine code here, for example:
    import time, DAI
    while True:
        DAI.push('Dummy_Sensor', [100, 200])
        time.sleep(exec_interval)
    '''


