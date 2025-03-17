import time
import random
from urllib import parse
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.pages.main_page import MainPage
from tests.pages.add_to_cart import AddToCartPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestTC002:
    def test_search_item(self, driver: WebDriver):
        try:
            ITEMS_XPATH = 'search-product'  
            
            add_to_cart_page = AddToCartPage(driver)
            
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
            
            
            time.sleep(random.uniform(2,4))  # 랜덤한 대기 시간
            
            products = driver.find_elements(By.CLASS_NAME, 'search-product')
            
            for product in products:
                try:
                    time.sleep(2)
                    
                    product.click()  # 직접 클릭
                    
                    time.sleep(random.uniform(2,4))  # 랜덤한 대기 시간
                    
                    # 새로 열린 창으로 전환
                    new_window = driver.window_handles[1] #두번째 창의 핸들 가져오기
                    driver.switch_to.window(new_window)
                    print("현재 URL:", driver.current_url)  # 현재 URL을 출력
                    wait = ws(driver, 10)
                    wait.until(EC.url_contains("products"))  # URL 검증
                    assert "products" in driver.current_url  # 검증
                    
                    print("상품 페이지로 이동 성공")
                    driver.save_screenshot('상품페이지-이동-성공.jpg')
                    break  # 첫 번째 상품만 클릭 후 종료

                except NoSuchElementException:
                    print("상품 요소를 찾을 수 없음. 다음 상품으로 진행.")
                    continue
                
            # add_to_cart_page.click_by_LINK_TEXT('장바구니 담기')
            # print("장바구니 담기 버튼 클릭 성공")   
            
        except NoSuchElementException as e:
            driver.save_screenshot('메인페이지-검색-실패-노서치.jpg')
            assert False
            

        