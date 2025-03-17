from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class AddToCartPage: 
    #객체 -> 인스턴스화 \ 내가 원하는 설정으로 셋업하는 함수
    def __init__(self, driver: WebDriver):
        self.driver = driver
        
    def click_by_LINK_TEXT(self, link_text: str):
        button = self.driver.find_element(By.LINK_TEXT, link_text)
        button.click()
  