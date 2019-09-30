import selenium.webdriver
import time
from wxpy import *

def order(url):
    num = 0

    while True:
        driver = selenium.webdriver.Firefox()
        driver.get(url)
        time.sleep(4)
        templist = driver.find_elements_by_class_name('orderLogin')
        time.sleep(4)
        driver.quit()
        if not templist:
            print(templist)
            print('再等等')
            num = 0
        else:
            print(templist)
            for _ in templist:
                print('快来吧')
                num = 1

            break
    return num

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

    url = 'https://www.91160.com/doctors/index/unit_id-200014707/dep_id-200054533/docid-200161473.html'
    # url = 'https://www.91160.com/doctors/index/unit_id-200003204/dep_id-200055411/docid-200139429.html'
    num = order(url)

    while True:

        if num == 1:
            me.send('快来吧！！！')
            # print('快来吧！！！')
            time.sleep(1)
            me.send('快来吧！！！')
            # print('快来吧！！！')
            time.sleep(1)
            me.send('快来吧！！！')
            # print('快来吧！！！')
            break


