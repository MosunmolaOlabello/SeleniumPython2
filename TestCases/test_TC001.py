from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_firsttestcase():
    driver = Firefox()
    driver.get("https://www.zendwallet.com/register")
    driver.find_element(By.NAME,"emailAddress").send_keys("Ayobamiolabello@gmail.com")
    driver.find_element(By.NAME,"firstName").send_keys("Mosunmola")
    driver.find_element(By.NAME,"lastName").send_keys("Olabello")
    driver.find_element(By.NAME,"username").send_keys("Mosbel")
    driver.find_element(By.NAME,"password").send_keys("Mosunbaby")
    obj=Select(driver.find_element(By.NAME,"country"))
    obj.select_by_visible_text("Nigeria")
    driver.close()