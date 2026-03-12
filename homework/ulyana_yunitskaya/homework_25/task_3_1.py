from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select_element = driver.find_element(By.ID, "id_choose_language")
    select = Select(select_element)
    options = [_.text for _ in select.options if _.text.strip()]
    chosen = random.choice(options)
    select.select_by_visible_text(chosen)
    submit_button = driver.find_element(By.ID, "submit-id-submit").click()
    result_text_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "result-text"))
    )
    assert result_text_element.text == chosen
    print("Passed:", chosen)

finally:
    driver.quit()
