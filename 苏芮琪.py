import selenium.webdriver

url = 'https://weibo.com/1972417605/like?from=page_100505_profile&wvr=6&mod=like#status'

driver = selenium.webdriver.Firefox()
driver.get(url)
# driver.find_element_by_id('loginname').send_keys('15829478003')
# driver.find_element_by_class_name('password').send_keys('199566')
# driver.find_element_by_class_name('W_btn_a btn_32px').click()
namelist = driver.find_elements_by_class_name('W_f14 W_fb S_txt1')
print(namelist)