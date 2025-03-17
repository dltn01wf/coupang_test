import time
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.main_page import MainPage
from tests.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TestLoginPage():
    def test_login(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()
            
            login_page = LoginPage(driver)
            
            time.sleep(2)
 
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
            time.sleep(2)
           
            main_page.click_by_LINK_TEXT('로그인')
            
            wait = ws(driver, 10)
            wait.until(EC.url_contains("login"))
            assert "login" in driver.current_url
            
            login_page.input_email_and_password('', '')
            time.sleep(2)
            login_page.click_login_button('//*[@id="memberLogin"]/div[1]/form/div[5]/button')
            
            time.sleep(2)
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
            
            driver.save_screenshot('로그인-성공.jpg')
        
        except NoSuchElementException as e:
            assert False
        
    
