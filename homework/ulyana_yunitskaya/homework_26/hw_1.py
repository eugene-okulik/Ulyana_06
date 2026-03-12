from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get('http://testshop.qa-practice.com/')
link = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.find_element(By.ID, 'add_to_cart').click()
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer .btn-secondary'))
).click()
driver.close()
driver.switch_to.window(tabs[0])
wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.o_wsale_my_cart'))
).click()
product = wait.until(
    EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Customizable Desk'))
)
assert product.is_displayed()
