from selenium import webdriver
from selenium.webdriver import ActionChains#引入动作链
import time

def dragObject():
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    driver.get(url)
    driver.switch_to.frame('iframeResult')
    source = driver.find_element_by_css_selector('#draggable')#找到被拖拽对象
    target = driver.find_element_by_css_selector('#droppable')#找到目标
    actions = ActionChains(driver)#声明actions对象
    actions.drag_and_drop(source, target)
    actions.perform()#执行动作
def downPage():
    driver.get('https://www.zhihu.com/explore')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    driver.execute_script('alert("To Bottom")')

def getLogo():
    url = 'https://www.zhihu.com/explore'
    driver.get(url)
    logo = driver.find_element_by_id('zh-top-link-logo')  # 获取网站logo
    print(logo)
    print(logo.get_attribute('class'))

def getText():
    url = 'https://www.zhihu.com/explore'
    driver.get(url)
    input = driver.find_element_by_class_name('question_link')
    print(input.text)  # input.text文本值

def ForwardAndBack():
    driver.get('https://www.baidu.com/')
    driver.get('https://www.taobao.com/')
    driver.get('https://www.python.org/')
    driver.back()

def UseCookies():
    driver.get('https://www.zhihu.com/explore')
    print(driver.get_cookies())
    driver.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(driver.get_cookies())
    driver.delete_all_cookies()
    print(driver.get_cookies())

driver= webdriver.Firefox()
UseCookies()
time.sleep(7)
driver.quit()