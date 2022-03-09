from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalog(browser, url):
    browser.get(url + "/index.php?route=product/category&path=25")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Components"))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group-item")))
    wait.until(EC.visibility_of_element_located((By.ID, "column-left")))
    wait.until(EC.visibility_of_element_located((By.ID, "product-category")))
