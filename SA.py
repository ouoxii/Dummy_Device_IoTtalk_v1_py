import random

ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Dummy_Device'
IDF_list = []
ODF_list = ['Dummy_Control']
device_id = None #if None, device_id = MAC address
device_name = None
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def Dummy_Sensor():
    return random.randint(0, 100)
    #return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)

state = "直立"

def Dummy_Control(data):
    # print(data[0])
    # Training Dataset: save to a file (.csv)
    print("----------")
    global state
    if data[0][1] <= -7:
        state = "直立"
    elif data[0][0] >= 7 or data[0][0] <= -7:
        state = "橫擺"
    elif data[0][2] >= 9 or data[0][2] <= -9:
        state = "平躺"
    print(state)
