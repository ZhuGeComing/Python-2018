from aip import AipOcr

def read_file():
    filePath = "123.png"
    with open(filePath, 'rb') as fp:
        return fp.read()
word =[]
APP_ID = '11093944'
API_KEY = 'FsXgNk6eu06BnqsIaraR4QIz'
SECRET_KEY = '9TsNdo86h2CpGmOGf45oGTgjglmlHG14'
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
result = client.basicGeneral(read_file())
for x in result['words_result']:
    word.append(x['words'])
    print type(x['words'])
words = ''.join(word).encode('utf-8')
print (words)
# print type(example)

    # print (x['words'].encode('utf-8'))
    # print(x['word'])

