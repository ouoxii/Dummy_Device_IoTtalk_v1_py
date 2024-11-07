import random

ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'MYwahaha'
IDF_list = []
ODF_list = ['usagi_wahaha'] #原本的['Dummy_Control']不是自訂的
device_id =  None #"AABBCCDD" if None, device_id = MAC address
device_name = "wahaha1107"
exec_interval = 1  # IDF/ODF interval

def usagi_wahaha(data:list):
    print(data)

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def Dummy_Sensor():
    return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)

def Dummy_Control(data:list):
    print(data[0])


