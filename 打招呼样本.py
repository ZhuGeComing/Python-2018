from cv2 import VideoCapture, imshow, waitKey, imwrite, destroyAllWindows
from aip import AipFace
from aip import AipSpeech
from base64 import b64encode
from os import system
import datetime


def recognize():
    now = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(now, '%H')
    if int(timestamp) < 12:
        stamp = '早上'
    elif int(timestamp) < 19:
        stamp = '下午'
    else:
        stamp = '晚上'
    try:
        score = res['result']['user_list'][0]['score']
        if score > 50:
            print(stamp + '好~' + names[res['result']['user_list'][0]['user_id']])
            return (stamp + '好~' + names[res['result']['user_list'][0]['user_id']])
        else:
            print('抱歉识别失败')
            return ('抱歉识别失败')
    except TypeError:
        print('抱歉识别失败')
        return('抱歉识别失败')
def detect():
    global res
    global names
    APP_ID = '11304911'
    API_KEY = 'pbW5Gp5iw2EFY6KVs9bOjmWe'
    SECRET_KEY = 'Z3oXfUVfwAMmb5NZhq94mWs16pUMnO4c'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    with open('test1.jpg', 'rb') as f:
        pic1 = f.read()
    res = client.search((b64encode(pic1)).decode(), 'BASE64', '1')
    # print(res['result']['user_list'][0])
    names = {
        'lhy': '刘恒宇',
        'wpf': '亲爱的温鹏飞学长',
        'wm': '亲爱的武萌学姐',
        'yk': '亲爱的杨柯学姐',
        'wdc': '亲爱的王栋才学长',
        'wmn': '亲爱的王美男学姐',
        'mxd': '亲爱的马旭东同学',
        'ljz':'亲爱的爸爸'
    }

    APP_ID = '11174193'
    API_KEY = '2OG012BvAtWdvzfWQGwscFzO'
    SECRET_KEY = 'lTD6LRVGDfewVsLadvhkH7cBixHkjnLL'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(recognize(), 'zh', 1, {
        'vol': 5,
        'per': 4,
        'spd': 5
    })
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    system('auido.mp3')
    # pygame.init()
    # track = pygame.mixer.music.load('auido.mp3')
    # pygame.mixer.music.play()
    # time.sleep(3)
    # pygame.mixer.music.stop()
    # pygame.quit()
if __name__ == '__main__':

    cap = VideoCapture(0)
    while(1):
        ret, frame = cap.read()
        imshow("capture", frame)
        if waitKey(1) & 0xFF == ord('q'):
            break
    imwrite('test1.jpg', frame)
    cap.release()
    destroyAllWindows()
    detect()
