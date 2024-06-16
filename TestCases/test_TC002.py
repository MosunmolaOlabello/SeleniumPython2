from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_thirdtestcase():
    driver = Firefox()
    driver.get("https://www.zendwallet.com/")
    obj = ActionChains(driver)
    obj.click(driver.find_element(By.XPATH,"//span[text()='App Store']")).perform()
    driver.close()