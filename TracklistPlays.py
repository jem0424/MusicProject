from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    track = "joris voorn ryo"
    chromedriver = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(chromedriver)
    # Test name: test2
    # Step # | name | target | value | comment
    # 1 | open | / |  |
    driver.get("https://www.google.com/")
    # 2 | setWindowSize | 1534x939 |  |
    driver.set_window_size(1534, 939)
    # 3 | sendKeys | name=q | ${KEY_DOWN} |
    driver.find_element(By.NAME, "q").send_keys(Keys.DOWN)
    # 4 | type | name=q | 1001tracklist |
    driver.find_element(By.NAME, "q").send_keys("1001tracklist")
    # 5 | sendKeys | name=q | ${KEY_ENTER} |
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    # 6 | click | id=nqsbq |  |
    driver.find_element(By.ID, "nqsbq").click()
    # 7 | type | id=nqsbq | joris voorn ryo |
    driver.find_element(By.ID, "nqsbq").send_keys(track)
    # 8 | sendKeys | id=nqsbq | ${KEY_ENTER} |
    driver.find_element(By.ID, "nqsbq").send_keys(Keys.ENTER)
    # 9 | click | css=.g:nth-child(1) .S3Uucc |  |
    driver.find_element(By.CSS_SELECTOR, ".g:nth-child(1) .S3Uucc").click()
    # 10 | runScript | window.scrollTo(0,18) |  |
    driver.execute_script("window.scrollTo(0,18)")

    HTMLdata = driver.page_source
    soup = BeautifulSoup(HTMLdata, 'html.parser')
    trackplays = soup.find_all(string=re.compile("Total Tracklist"))
    plays = list(map(lambda sub: int(''.join(
        [ele for ele in sub if ele.isnumeric()])), trackplays))
    print(trackplays)
    driver.close()
# element = driver.find_element_by_class_name("").text
