from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class LoginPage: 
  #객체 -> 인스턴스화 \ 내가 원하는 설정으로 셋업하는 함수
  def __init__(self, driver: WebDriver):
    self.driver = driver
  
  def input_email_and_password(self, email: str, password: str):
    email_input_box = self.driver.find_element(By.ID, 'login-email-input')
    email_input_box.send_keys(email)
    password_input_box = self.driver.find_element(By.ID, 'login-password-input')
    password_input_box.send_keys(password)
  
  def click_login_button(self, login_btn: str):
    login_button = self.driver.find_element(By.XPATH, login_btn)
    login_button.click()
  
    
  

  





  