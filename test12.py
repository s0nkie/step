from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

button = browser.find_element_by_tag_name('button').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

a = browser.find_element_by_id('input_value').text
x = int(a)

def sum(x):
    return str(math.log(abs(12 * math.sin(x))))

y = sum(x)

answer = browser.find_element_by_id('answer').send_keys(y)
button = browser.find_element_by_tag_name('button').click()

time.sleep(5)

browser.quit()
