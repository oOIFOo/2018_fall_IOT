# -*- coding: UTF-8 -*-
import time, DAN, requests, random
import queue
import threading
import random
import time

ServerURL = 'http://140.113.199.189:9999'
Reg_addr = '1122'
DAN.profile['dm_name']='line'
DAN.profile['df_list']=['line_Sensor', 'line_Control']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerURL, Reg_addr)


#Python module requirement: line-bot-sdk, flask
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('hUV9rMkAYYsbxBDCyjbzBPEIihKPtE/EbYzQtTRUZVQHk1GX5lxqQqveyJIBRwV9LQ2Vj8R3UeyGALklDY0ogfDAtH4voLNXkIqXxuKGh96Ft9r8GtrdoSqUzOObV/tpQ7XJPUDZFDX7yCv9y6eMYQdB04t89/1O/w1cDnyilFU=') #LineBot's Channel access token
handler = WebhookHandler('58494ab9c47fad65d4017f026b2d0821')        #LineBot's Channel secret
user_id_set=set()                                         #LineBot's Friend's user id 
app = Flask(__name__)


def loadUserId():
    try:
        idFile = open('idfile', 'r')
        idList = idFile.readlines()
        idFile.close()
        idList = idList[0].split(';')
        idList.pop()
        return idList
    except Exception as e:
        print(e)
        return None


def saveUserId(userId):
        idFile = open('idfile', 'a')
        idFile.write(userId+';')
        idFile.close()


@app.route("/", methods=['GET'])
def hello():
    return "HTTPS Test OK."

@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']    # get X-Line-Signature header value
    body = request.get_data(as_text=True)              # get request body as text
    print("Request body: " + body, "Signature: " + signature)
    try:
        handler.handle(body, signature)                # handle webhook body
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    Msg = event.message.text
    if Msg == 'Hello, world': return
    print('GotMsg:{}'.format(Msg))

    #line_bot_api.reply_message(event.reply_token,TextSendMessage(text="收到訊息!!"))   # Reply API example
    DAN.push ('line_Sensor', Msg,  Msg)
    userId = event.source.user_id
    if not userId in user_id_set:
        user_id_set.add(userId)
        saveUserId(userId)

def f ():
    while True:
        value=DAN.pull('line_Control')
        if value != None:
            for userId in user_id_set:
                line_bot_api.push_message(userId,TextSendMessage(text=value[0]))
                print(value)
			
if __name__ == "__main__":

    idList = loadUserId()
    if idList: user_id_set = set(idList)

    try:
        for userId in user_id_set:
            line_bot_api.push_message(userId, TextSendMessage(text='LineBot is ready for you.'))  # Push API example
    except Exception as e:
        print(e)
    
    t = threading.Thread(target=f, args=())
    t.daemon = True
    t.start()
	
    app.run('127.0.0.1', port=32768, threaded=True, use_reloader=False)

    

