from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))
    wait.until(EC.visibility_of_element_located((By.ID, "menu")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "menu"), "Desktops"))
