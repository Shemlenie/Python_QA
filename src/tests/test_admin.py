from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin(browser, url):
    browser.get(url + "/admin")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")))
    wait.until(EC.visibility_of_element_located((By.ID, "footer")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "container-fluid")))
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "form-group"), "Username"))

