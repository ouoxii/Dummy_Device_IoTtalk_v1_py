import random

ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'ntou_acc_dm'
IDF_list = []
ODF_list = ['ntou_acc']
device_id = "AABBCCDD" #if None, device_id = MAC address
device_name = "ntou1031"
exec_interval = 1  # IDF/ODF interval

def ntou_acc(data:list):
    print(data)

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def Dummy_Sensor():
    return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)

def Dummy_Control(data:list):
    print(data[0])


