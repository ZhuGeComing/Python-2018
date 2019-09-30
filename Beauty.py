import selenium.webdriver
import time
import requests

def get_url(url):
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    for eve in driver.find_elements_by_class_name('text'):
        picture_url = eve.find_element_by_xpath('p/img').get_attribute('src')
        print(picture_url)
        save_pic(picture_url)
    driver.quit()
    # links = driver.find_elements_by_class_name('view_img_link')
    #
    # for i in links:
    #     for link in i.find_elements_by_xpath("//*[@href]"):
    #         print(link.get_attribute('href'))


    # for link in driver.find_elements_by_xpath('//*[@src]'):
    #     print(link.get_attribute('src'))
def get_page(n):
    page_list = []
    for i in range(100-n,100):
        page_list.append('http://jandan.net/ooxx/page-%d#comments'%i)
    return page_list
def save_pic(url):
    response = requests.get(url).content

    with open(url[-10:],'wb') as f:
        f.write(response)

if __name__ == '__main__':
    n = int(input('Please Input Your Pages:'))

    for i in get_page(n):
        get_url(i)
