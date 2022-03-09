from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_card(browser, url):
    browser.get(url + "/index.php?route=product/product&path=25_28&product_id=42")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Apple Cinema 30"))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "col-sm-8")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-group")))
    wait.until(EC.visibility_of_element_located((By.ID, "product")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tab-content")))
