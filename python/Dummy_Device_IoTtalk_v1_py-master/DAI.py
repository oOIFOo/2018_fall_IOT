import time, DAN, requests, random

ServerURL = 'http://140.113.199.189:9999' #with no secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = None #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

id = 0
send = 0
receive = 0
count = 10
while True:
    try:
    #Pull data from a device feature called "Dummy_Control"
        value1=DAN.pull('Dummy_Control')
        if value1 != None:
            if value1[0] == id:
                receive = receive+(time.time()-send)/10
                count = count-1
                if count == 0:print(receive)

    #Push data to a device feature called "Dummy_Sensor"
        value2=random.uniform(1, 10)
        send = time.time()
        id = value2
        DAN.push ('Dummy_Sensor', value2,  value2)


    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

