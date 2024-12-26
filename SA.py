import random
import numpy as np
import openpyxl
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


from openpyxl import Workbook

wb = Workbook()
ws = wb.active
state = "直立"
import time
l = list()
res = list()
t = time.time()
save_flag = False
def Dummy_Control(data):
    global l, res, t, save_flag  # 明確宣告使用全域變數

    print(len(res))
    if 2.5 <= time.time() - t <= 3:
        print('start gesture')
    if time.time() - t > 3:
        data = data[0]
        l.append(data)
        if len(l) == 10:
            res.extend(l)
            l = list()
            t = time.time()  # 重新更新全域變數 t
            print('end gesture')
    if len(res) >= 1500 and not save_flag:  # 加入條件判斷以避免多次儲存
        # 將結果寫入 Excel
        for row in res:
            ws.append(row)
        wb.save("circle.xlsx")
        print("save end close")
        save_flag = True  # 設定旗標為 True，表示已完成儲存



