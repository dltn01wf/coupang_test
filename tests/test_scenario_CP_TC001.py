import time
import pytest
from urllib import parse
from tests.pages.main_page import MainPage
from tests.pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestTC001:
    
    #로그인 후 상품 검색 기능
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_login_search_item(self, driver: WebDriver):
        try:
            # ITEMS_XPATH ="//form/ul/li"
            ITEMS_XPATH = 'search-product'  
            
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
        
            # time.sleep(2)
            driver.implicitly_wait(10)  # ✅ 요소가 나타날 때까지 최대 10초 기다림
            
            main_page.search_items('노트북')
            ws(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, ITEMS_XPATH))
            )
            
            items = driver.find_elements(By.CLASS_NAME, ITEMS_XPATH)
            item_name = parse.quote('노트북')

            assert len(items) > 0
            assert item_name in driver.current_url
            
            driver.save_screenshot('메인페이지-검색-성공.jpg')
            
            
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-검색-실패-노서치.jpg')
            assert False
        
        # except TimeoutException as e:
        #     driver.save_screenshot('메인페이지-검색-실패-타임에러.jpg')
        #     assert False

 
    #로그인 전 상품 검색 기능
    def test_login_search_item(self, driver: WebDriver):
        try:
            ITEMS_XPATH = 'search-product'  
            
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)
 
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
            time.sleep(2)
           
            main_page.search_items('노트북')
            ws(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, ITEMS_XPATH))
            )
            
            items = driver.find_elements(By.CLASS_NAME, ITEMS_XPATH)
            item_name = parse.quote('노트북')

            assert len(items) > 0
            assert item_name in driver.current_url
            
            driver.save_screenshot('메인페이지-검색-성공.jpg')
            
            
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-검색-실패-노서치.jpg')
            assert False
            
        # except TimeoutException as e:
        #     driver.save_screenshot('메인페이지-검색-실패-타임에러.jpg')
        #     assert False
        