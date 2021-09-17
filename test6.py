from selenium import webdriver
import time
import math


driver = webdriver.Chrome()
browser = driver.get('http://suninjuly.github.io/get_attribute.html')


x_element = driver.find_element_by_id('treasure')
attribute = x_element.get_attribute('valuex')

x = attribute

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

y = calc(x)

res = driver.find_element_by_id('answer')
res.send_keys(y)
check = driver.find_element_by_id('robotCheckbox')
check.click()
check2 = driver.find_element_by_id('robotsRule')
check2.click()
submit = driver.find_element_by_tag_name('button')
submit.click()

time.sleep(5)



driver.quit()   