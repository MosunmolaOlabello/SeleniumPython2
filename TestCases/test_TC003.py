from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_secondtestcase():
    driver = Firefox()
    driver.get("https://www.zendwallet.com/")
    obj = ActionChains(driver)
    obj.click(driver.find_element(By.XPATH,"//button[text()='Login']")).perform()
    driver.close()
