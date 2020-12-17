import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '847365049:AAHP_qPi8e_bePCWY8OVOx-vChb4Qk6OmX4'
    bot_chatID = '1305712253'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(bot_message)
    response = requests.get(send_text)
    print(response)
    return(response)
    
def telegram_bot_sendImage(img):
    bot_token = '847365049:AAHP_qPi8e_bePCWY8OVOx-vChb4Qk6OmX4'
    bot_chatID = '1305712253'
    url = "https://api.telegram.org/bot"+ bot_token +"/sendPhoto"
    files = {'photo': open(img, 'rb')}
    data = {'chat_id' : bot_chatID}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)    
    
