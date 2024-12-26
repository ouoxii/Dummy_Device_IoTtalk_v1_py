import pickle, os
import numpy as np
from sklearn.preprocessing import StandardScaler

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


model_name = ['Decision_Tree', 'Random_Forest', 'KNN', 'SVM', 'Gaussian_Naive_Bayes', 'Neural_Network']

# 選模型name
with open(os.path.join('model', 'Random_Forest.pkl'), 'rb') as f:
    classifier = pickle.load(f)

scaler = StandardScaler()
x = list()
now_state = 0
now_action = 0
data_size = 8
light = 0

def Dummy_Sensor():
    global light
    return light


def Dummy_Control(data:list):
    global x, data_size, light, now_action, now_state
    data = data[0]
    x.append(data)
    if len(x) > data_size:
        x.pop(0)
        label = classifier.predict(np.array([np.array(x).T.flatten()]))[0]

        # 各類別prob值
        print(classifier.predict_proba(np.array([np.array(x).T.flatten()]))[0])
        match label:
            case 0:  # other: 0
                now_state = 0
            case 1:
                if now_state == 1:
                    now_action = 1
                now_state = 1
            case 2:
                if now_state == 2:
                    now_action = 2
                now_state = 2
# =============================================================================
#             case 3:
#                 if now_state == 3:
#                     now_action = 3
#                 now_state = 3
# =============================================================================
    match now_action:
        case 0:
            print("畫圈\n")
        case 1:
            print("舉起\n")
            light=100
        case 2:
            print("未偵測到動作\n")
            light=0
# =============================================================================
#         case 3:
#             print("偵測到直線，燈泡亮度調整成中間值\n")
#             light=50
# =============================================================================
    now_action = 0


def on_register(r):
    print(f'Device name: {r["d_name"]}')
    '''
    #You can write some SA routine code here, for example:
    import time, DAI
    while True:
        DAI.push('Dummy_Sensor', [100, 200])
        time.sleep(exec_interval)
    '''


