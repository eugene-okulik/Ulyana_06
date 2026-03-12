from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get('http://testshop.qa-practice.com/')
first_product = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.oe_product_image_link'))
)
product_name = first_product.get_attribute('title')
ActionChains(driver).move_to_element(first_product).perform()
add_to_cart = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.a-submit'))
)
add_to_cart.click()
popup = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
)
popup_product = popup.find_element(By.CSS_SELECTOR, '.product-name').text
assert product_name in popup_product
print('Done')
