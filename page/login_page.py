from selenium.webdriver.common.by import By
#POM class
class LoginPage:
    #declaration
    __username:tuple[str,str]
    __password:tuple[str,str]
    __go_button:tuple[str,str]

    #initialization
    def __init__(self,driver):
        self.driver=driver
        self.__username = (By.ID, "input-username")
        self.__password =  (By.ID, "input-password")
        self.__go_button = (By.NAME,"login-button")

    #utlization
    def set_username(self,un):
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_go_button(self):
        self.driver.find_element(*self.__go_button).click()