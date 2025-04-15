from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#POM class
class LoginPage:
    #declaration
    __username:tuple[str,str]
    __password:tuple[str,str]
    __go_button:tuple[str,str]
    __err_msg:tuple[str,str]
    #initialization
    def __init__(self,driver):
        self.driver=driver
        self.__username = (By.ID, "input-username")
        self.__password =  (By.ID, "input-password")
        self.__go_button = (By.NAME,"login-button")
        self.__err_msg= (By.CSS_SELECTOR,"div.error")

    #utlization
    def set_username(self,un):
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_go_button(self):
        self.driver.find_element(*self.__go_button).click()

    def verify_err_msg_is_displayed(self,wait:WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__err_msg))
            msg=self.driver.find_element(*self.__err_msg).text
            print('Err Msg is displayed:',msg)
            return True
        except:
            print('Err Msg is NOT displayed')
            return False