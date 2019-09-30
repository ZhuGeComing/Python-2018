from aip import AipFace
# import cv2 as cv
APP_ID = '11304911'
API_KEY = 'pbW5Gp5iw2EFY6KVs9bOjmWe'
SECRET_KEY = 'Z3oXfUVfwAMmb5NZhq94mWs16pUMnO4c'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
with open('lena.jpg', 'rb') as f:
    res = f.read()
# res = cv.imread('lena.jpg')
print client.detect(res, 'jpg')