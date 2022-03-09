from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register(browser, url):
    browser.get(url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Register Account"))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "radio-inline")))
    wait.until(EC.visibility_of_element_located((By.ID, "account")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "buttons")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))

