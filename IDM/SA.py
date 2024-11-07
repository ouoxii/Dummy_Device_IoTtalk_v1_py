import random

ServerURL = 'https://class.iottalk.tw' #For example: 'https://DomainName'
MQTT_broker = 'iot.iottalk.tw' # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 8883
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'usagi_idm'
IDF_list = ['usagi_idf']
ODF_list = [] #原本的['Dummy_Control']不是自訂的
device_id =  "usagi" #if None, device_id = MAC address
device_name = "wahaha_idm"
exec_interval = 1  # IDF/ODF interval

def usagi_idf():
    num = random.randint(0, 20)
    print('usagi_idf:', num)
    return num

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def Dummy_Sensor():
    return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)

def Dummy_Control(data:list):
    print(data[0])


