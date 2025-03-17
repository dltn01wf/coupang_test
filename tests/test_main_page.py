# tests/test_main_page.py
import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver # noqa
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from urllib import parse

from tests.pages.main_page import MainPage

class TestMainPage:
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)
 
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
            time.sleep(2)
            
            #새로운 기능 여기서 테스트
            
            # main_page.click_by_LINK_TEXT("회원가입")
            # assert "memberJoinFrm" in driver.current_url
        
        except NoSuchElementException as e:
            assert False
            
            
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)

            wait = ws(driver, 10) #최대 10까지 기다림
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
           
            main_page.click_by_LINK_TEXT('로그인')
            
            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지-로그인-성공.jpg')
            
            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
            
            time.sleep(2)
            main_page.click_by_LINK_TEXT('회원가입')
            assert "memberJoinFrm" in driver.current_url
            driver.save_screenshot('메인페이지-회원가입-성공.jpg')
            
            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 
            
            time.sleep(2)
            main_page.click_by_LINK_TEXT('장바구니')
            assert "cartView" in driver.current_url
            driver.save_screenshot('메인페이지-장바구니-성공.jpg')
            
            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증 
            
            #비로그인 테스트이므로 마이쿠팡을 클릭시 로그인으로 가야함
            time.sleep(2)
            main_page.click_by_LINK_TEXT('마이쿠팡')
            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지-마이쿠팡-성공.jpg')
            
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-링크테스트-실패-노서치.jpg')
            assert False
        
        except TimeoutException as e:
            driver.save_screenshot('메인페이지-링크테스트-실패-타임에러.jpg')
            assert False
           
        
    # @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_search_items(self, driver: WebDriver):
        try:
            ITEMS_XPATH ="//form/ul/li"
        
            main_page = MainPage(driver)
            main_page.open()
            
            time.sleep(2)

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("coupang.com")) #URL 검증
            assert "coupang.com" in driver.current_url #검증
        
            time.sleep(2) #2초 왜? 봇인거 안들키기 위해서
        
            main_page.search_items('노트북')
            ws(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, ITEMS_XPATH))
            )
            
            items = driver.find_element(By.XPATH, ITEMS_XPATH)
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
            
        




    # def test_click_signup_button(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.open()
    #     login_page = LoginPage(driver)
    #     login_page.click_login_button()


    #     # 무료 체험하기 버튼 클릭
    #     main_page.click_signup()

    #     # 회원가입(또는 get-started/services) 페이지로 이동했는지 확인
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(EC.url_contains("accounts.elice.io/accounts/signup"))
    #     assert "accounts.elice.io/accounts/signup" in driver.current_url

    # def test_click_product_lxp_card(self, driver):
    #     """
    #     1) 헤더의 '제품' 버튼을 클릭한다.
    #     2) '엘리스LXP' 카드(또는 해당 div)가 나타났는지 확인한다.
    #     3) '엘리스LXP' 카드를 클릭한다.
    #     4) 'https://elice.io/ko/products/lxp'로 이동했는지 확인한다.
    #     """

    #     main_page = MainPage(driver)
    #     main_page.open()

    #     # (1) 헤더 '제품' 버튼 클릭
    #     main_page.click_product_button()

    #     # (2) '엘리스LXP' 카드가 표시되었는지 확인
    #     main_page.wait_for_lxp_card_visible()

    #     time.sleep(4)

    #     # (3) '엘리스LXP' 카드 클릭
    #     main_page.click_lxp_card()

    #     # (4) 이동한 URL 확인
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(EC.url_contains("/ko/products/lxp"))

    #     time.sleep(4)
    #     assert "https://elice.io/ko/products/lxp" in driver.current_url