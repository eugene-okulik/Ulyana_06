from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/automation-practice-form')
driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys('Ulyana')
driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]').send_keys('Yunitskaya')
driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys('test@mail.ru')
driver.find_element(By.CSS_SELECTOR, '[placeholder="Mobile Number"]').send_keys('1234567890')
driver.find_element(By.ID, "gender-radio-2").click()
driver.find_element(By.ID, "dateOfBirthInput").click()
month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
month.select_by_visible_text("October")
year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
year.select_by_visible_text("1994")
driver.find_element(
    By.XPATH,
    "//div[contains(@class,'react-datepicker__day--006') and not(contains(@class,'outside-month'))]"
).click()
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)
driver.find_element(By.ID, "hobbies-checkbox-3").click()
driver.find_element(By.ID, "currentAddress").send_keys('ul. Karpia 22D/10, Gdansk, Poland')
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Uttar Pradesh")
state.send_keys(Keys.ENTER)
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Lucknow")
city.send_keys(Keys.ENTER)
driver.find_element(By.ID, "submit").click()
modal = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
)
print(modal.text)
