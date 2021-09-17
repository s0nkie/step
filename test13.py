from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = WebDriverWait(browser, price).until(EC.element_to_be_clickable((By.ID, 'book'))).click()

num = browser.find_element_by_id('input_value').text
x = int(num)
def sum(x):
    return str(math.log(abs(12 * math.sin(x))))

y = sum(x)

res = browser.find_element_by_id('answer').send_keys(y)

button2 = browser.find_element_by_id("solve").click()

assert "successful" in message.text

time.sleep(5)

browser.quit()