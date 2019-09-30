from selenium import webdriver
from time import sleep
from wxpy import Bot
from sys import exit

count = 9999

def order(url):
    num = 0
    global count

    while True:
        driver = webdriver.Firefox()
        driver.get(url)
        sleep(5)
        list = driver.find_elements_by_class_name('orderLogin')
        sleep(3)
        driver.quit()

        if not list:
            print('再等等,再尝试%d次。'%(count-1))
            count -= 1
            num = 0
        else:
            print('快来吧')
            num = 1

        judge(num)



def judge(num):

    global me

    while True:

        if count == 0:
            # return False

            exit()

        elif num == 1:
            me.send('快来吧！！！')
            sleep(1)
            me.send('快来吧！！！')
            sleep(1)
            me.send('快来吧！！！')
            # return False
            exit()

        else:

            break



        # for i in list:
        #     if i.is_displayed():
        #         if not i.text == '预约':
        #             print('再等等')
        #             continue

                #     time.sleep(3)


        # print(list)
        # time.sleep(5)
        # if list == '预约':
        #     break



    # list_1 = list.find_elements_by_xpath('a')
    # for i in list_1:
    #     condition = i.get_attribute('title')
    #     print(condition)


if __name__ == '__main__':

    bot = Bot()

    me = bot.friends().search('我是地球人')[0]

    url = 'https://www.91160.com/doctors/index/docid-200161473.html'
    # url = 'https://www.91160.com/doctors/index/unit_id-200003204/dep_id-200055338/docid-200139309.html'

    order(url)

    bot.join()

    exit()

