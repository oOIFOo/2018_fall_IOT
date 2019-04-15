import random
import time

from dan import NoData

### The register server host, you can use IP or Domain.
host = 'iottalk2.tw'

### [OPTIONAL] The register port, default = 9992
# port = 9992

### [OPTIONAL] If not given or None, server will auto-generate.
# device_name = 'Dummy_Test'

### [OPTIONAL] If not given or None, DAN will register using a random UUID.
### Or you can use following code to use MAC address for device_addr.
# from uuid import getnode
# device_addr = "{:012X}".format(getnode())
#device_addr = "aa8e5b58-8a9b-419b-b8d5-72624d61108d"

### [OPTIONAL] If not given or None, this device will be used by anyone.
username = '0416313'

### The Device Model in IoTtalk, please check IoTtalk document.
device_model = 'Dummy_Device'

### The input/output device features, please check IoTtalk document.
idf_list = ['Dummy_Sensor']
odf_list = ['Dummy_Control']

### Set the push interval, default = 1 (sec)
### Or you can set to 0, and control in your feature input function.
push_interval = 5  # global interval
interval = {
    'Dummy_Sensor': 3,  # assign feature interval
}

id = 0
send = 0
receive = 0
count = 10
def register_callback():
    print('register successfully')

def Dummy_Sensor():
    global id
    global send
    id = random.randint(0, 100)
    send = time.time()
    return id
    # return NoData

def Dummy_Control(data):  # data is a list
    global count
    global id
    global receive
    if id == data[0]:receive = receive+(time.time()-send)/10
    count = count-1
    if count == 0:print(receive)