from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/selects2.html')

first = driver.find_element_by_id('num1').text
second = driver.find_element_by_id('num2').text
x = first
y = second

def summ(x, y):
    return int(x) + int(y)

suma = str(summ(x, y))
print(suma)

dropdown = Select(driver.find_element_by_tag_name('select'))
dropdown.select_by_value(suma)
submit = driver.find_element_by_tag_name('button').click()

time.sleep(5)

driver.quit()