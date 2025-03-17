import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class MainPage:
    URL = "https://www.coupang.com"
    SEARCH_INPUT_ID = "headerSearchKeyword"
    
    #객체 -> 인스턴스화 \ 내가 원하는 설정으로 셋업하는 함수
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    #메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)
        
    def search_items(self, item_name: str):
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        for char in item_name:
            search_input_box.send_keys(char)
            time.sleep(0.5)  # 0.2초(200ms) 정도 대기 (원하는 만큼 조절)
        #search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)
        
    def click_by_LINK_TEXT(self, link_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, link_text)
        login_button.click()

     
        
    
        
    #기능 만들고 기는에 대한 테스트
        
        
        

    # LOGIN_BUTTON = (By.CSS_SELECTOR,
    #                 "button.MuiButtonBase-root.MuiButton-root.MuiButton-text.css-ii6ciq"
    #                 )

    # SIGNUP_BUTTON = (By.CSS_SELECTOR, "a.css-16cuj6o")
    # PRODUCT_BUTTON = (By.XPATH, "//button[contains(normalize-space(.), '제품')]")

    # # 2) '엘리스LXP' 카드가 나타나는  div.
    # LXP_CARD_CONTAINER = (
    #     By.CSS_SELECTOR,
    #     "div.MuiStack-root.MuiCardContent-root.css-1pzbmah"
    # )

    # def __init__(self, driver):
    #     self.driver = driver

    # def open(self):
    #     self.driver.get(self.URL)

    # def click_login(self):
    #     """
    #     로그인 버튼이 2개 잡히는 문제를 해결하기 위해:
    #     - 모든 .css-ii6ciq 요소를 찾은 뒤
    #     - 표시(displayed)된 요소만 골라 마지막 것을 클릭
    #     """
    #     wait = WebDriverWait(self.driver, 10)

    #     # (1) DOM 상에 LOGIN_BUTTONS 요소들이 나타날 때까지 대기
    #     wait.until(EC.presence_of_all_elements_located(self.LOGIN_BUTTON))

    #     # (2) 여러 개 찾기
    #     all_buttons = self.driver.find_elements(*self.LOGIN_BUTTON)
    #     print(f"[DEBUG] Found {len(all_buttons)} login elements with .css-ii6ciq")

    #     # 각 버튼 상태 디버그 출력
    #     for i, b in enumerate(all_buttons):
    #         print(
    #             f"  [#{i}] text='{b.text}' displayed={b.is_displayed()} "
    #             f"location={b.location} size={b.size}"
    #         )

    #     # (3) 표시된(displayed=True) 요소만 필터링
    #     visible_btns = [b for b in all_buttons if b.is_displayed()]
    #     if not visible_btns:
    #         raise AssertionError(
    #             "No displayed login button found. Possibly overshadowed or hidden."
    #         )

    #     # (4) 표시된 요소 중 가장 마지막(혹은 첫 번째) 요소를 선택
    #     target_btn = visible_btns[-1]

    #     # (5) 클릭 가능할 때까지 대기 후 클릭
    #     wait.until(EC.element_to_be_clickable(target_btn))
    #     target_btn.click()

    # def click_signup(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     signup_btn = wait.until(EC.element_to_be_clickable(self.SIGNUP_BUTTON))
    #     signup_btn.click()

    # def click_product_button(self):
    #     """
    #     헤더의 '제품' 버튼을 클릭한다.
    #     """
    #     wait = WebDriverWait(self.driver, 10)
    #     product_btn = wait.until(EC.element_to_be_clickable(self.PRODUCT_BUTTON))
    #     product_btn.click()

    # def wait_for_lxp_card_visible(self):
    #     """
    #     '제품' 메뉴를 클릭하면 펼쳐지는 드롭다운(또는 오버레이)에
    #     엘리스LXP 카드가 표시되는지 기다린다.
    #     """
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.presence_of_element_located(self.LXP_CARD_CONTAINER))

    # def click_lxp_card(self):
    #     """
    #     엘리스LXP 카드(전체 div)를 클릭하거나,
    #     내부의 화살표 아이콘 등을 클릭해도 무방하다.
    #     """
    #     wait = WebDriverWait(self.driver, 10) 
    #     lxp_card = wait.until(EC.element_to_be_clickable(self.LXP_CARD_CONTAINER))
    #     lxp_card.click()


   