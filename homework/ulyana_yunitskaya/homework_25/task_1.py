from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

input_text = 'hello'
driver.get('https://www.qa-practice.com/elements/input/simple')
text_string = driver.find_element(By.ID, 'id_text_string')
text_string.send_keys(input_text)
text_string.submit()
result_text = driver.find_element(By.ID, 'result-text')
print(result_text.get_attribute('innerText'))
