import time, DAN, requests, random #引入以計時
import requests                  #向網站發出request
from bs4 import BeautifulSoup    #解析html網頁
from datetime import datetime    #handle timestamp
ServerURL = 'http://140.113.199.189:9999' #with no secure connection
Reg_addr = 'WWWLLK'#if None, Reg_addr = MAC address


DAN.profile['dm_name']='wheather0416313'
DAN.profile['df_list']=['hum038080', 'tmp038080', 'rain038080', 'wind038080']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)

urls = ["https://www.cwb.gov.tw/V7/observe/real/ObsN.htm?", #北部
       #"https://www.cwb.gov.tw/V7/observe/real/ObsC.htm?", #中部
       #"https://www.cwb.gov.tw/V7/observe/real/ObsS.htm?", #南部
       #"https://www.cwb.gov.tw/V7/observe/real/ObsE.htm?", #東部
       #"https://www.cwb.gov.tw/V7/observe/real/ObsI.htm?", #外島
]

Cord = {
    '桃園農改': {'lat':'24.950944', 'lng':'121.030583'},
	'茶改場'  : {'lat':'24.908472', 'lng':'121.185333'},
	'中央大學': {'lat':'24.967708', 'lng':'121.185142'},
	'拉拉山'  : {'lat':'24.690286', 'lng':'121.403914'},
	'農工中心': {'lat':'24.985917', 'lng':'121.239833'},
	'復興'    : {'lat':'24.820208', 'lng':'121.352281'},
	'桃園'    : {'lat':'24.992425', 'lng':'121.323172'},
	'八德'    : {'lat':'24.928708', 'lng':'121.283289'},
	'大園'    : {'lat':'25.04775', 'lng':'121.225958'},
	'觀音'    : {'lat':'25.027072', 'lng':'121.153317'},
	'蘆竹'    : {'lat':'25.084275', 'lng':'121.265767'},
	'大溪'    : {'lat':'24.882853', 'lng':'121.265547'},
	'平鎮'    : {'lat':'24.897503', 'lng':'121.214636'},
	'楊梅'    : {'lat':'24.912375', 'lng':'121.143047'},
	'龍潭'    : {'lat':'24.870056', 'lng':'121.221389'},
}

def timestamp_handler(timestamp):
    year = '2018'
    month = timestamp.split()[0].split('/')[0]
    day = timestamp.split()[0].split('/')[1]
    hour = timestamp.split()[1].split(':')[0]
    minute = timestamp.split()[1].split(':')[1]
    second = '00'
    return year+'-'+month+'-'+day+' '+hour+':'+minute+':'+second

while True:
    #向網站發出request要html資料
    for url in urls:
        res = requests.get(url)
        res.encoding = 'utf-8'
        #確認是否回傳成功
        if  res.status_code == requests.codes.ok:
            #成功的話開始解析網頁
            soup = BeautifulSoup(res.text, 'html.parser')
            data_rows = soup.find_all('tr')
            # print(data_rows[1].find_all('td'))
            # 一筆資料
            # [<td style="display: none;">46694</td>,                  *ID
            # <td id="MapID46694"><a href="46694.htm">基隆</a></td>,   *測站名稱
            # <td>11/20 11:20</td>,                                    *觀測時間
            # <td class="temp1">22.7</td>,                             *溫度(攝氏)          <need>
            # <td class="temp2" style="display: none;">72.9</td>,      *溫度(華氏)
            # <td>陰</td>,                                             *天氣
            # <td>東北</td>,                                           *風向
            # <td>2.5 </td>,                                           *風力(m/s)           <need>
            # <td>2</td>,                                              *風力(級)
            # <td>-</td>,                                              *陣風(m/s)
            # <td>-</td>,                                              *陣風(級)
            # <td>16.0</td>,                                           *能見度(公里)
            # <td>64</td>,                                             *相對溼度(%)         <need>
            # <td>1019.8</td>,                                         *海平面氣壓(百帕)
            # <td><font color="black">0.0</font></td>,                 *當日累積雨量(毫米)  <need>
            # <td>0.1</td>]                                            *日照時數
            for row in data_rows:
                if len(row.find_all('td')) == 16:
                    #測站名稱, 溫度(攝氏), 風力(m/s), 相對溼度(%), 當日累積雨量(毫米), 觀測時間
                    # print(row.find_all('td')[1].find('a').text, row.find_all('td')[3].text, row.find_all('td')[7].text, row.find_all('td')[12].text, row.find_all('td')[14].find('font').text, timestamp_handler(row.find_all('td')[2].text))
                    loc = row.find_all('td')[1].find('a').text
                    if loc in Cord:
                       DAN.push ('hum038080', Cord[loc]['lat'],  Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[12].text, timestamp_handler(row.find_all('td')[2].text))
                       DAN.push ('tmp038080', Cord[loc]['lat'],  Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[3].text, timestamp_handler(row.find_all('td')[2].text))
                       DAN.push ('rain038080', Cord[loc]['lat'],  Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[14].text, timestamp_handler(row.find_all('td')[2].text))
                       DAN.push ('wind038080', Cord[loc]['lat'],  Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[7].text, timestamp_handler(row.find_all('td')[2].text))
					   
                       print('\nTemperature-I', Cord[loc]['lat'], Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[3].text, timestamp_handler(row.find_all('td')[2].text))
                       print('rainnnnnnnn-I', Cord[loc]['lat'], Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[14].text, timestamp_handler(row.find_all('td')[2].text))
                       print('windddddddd-I', Cord[loc]['lat'], Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[7].text, timestamp_handler(row.find_all('td')[2].text))
                       print('humidityyyy-I', Cord[loc]['lat'], Cord[loc]['lng'], row.find_all('td')[1].find('a').text, row.find_all('td')[12].text, timestamp_handler(row.find_all('td')[2].text))
					   
    #計時十分鐘後再抓
    time.sleep(6)