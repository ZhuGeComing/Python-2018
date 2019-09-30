import requests
import selenium.webdriver
import re
import time

def get_page(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    headers = {'User-Agent':user_agent}
    response = requests.get(url,headers=headers)
    return response

def open_page(url):
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_class_name('s_ipt').send_keys('天气')
    driver.find_element_by_id('su').click()
    time.sleep(2)

    # for eve in driver.find_elements_by_class_name('result'):
    #     print(eve.find_element_by_xpath('h3/a').get_attribute('href'))

    time.sleep(5)
    driver.quit()




if __name__ == '__main__':
    # url = 'http://jandan.net/ooxx/'
    url = 'https://www.baidu.com/'
    open_page(url)

