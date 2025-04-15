from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:

    __logout:tuple[str,str]

    def __init__(self,driver):
        self.driver=driver
        self.__logout=(By.XPATH,"//a[text()='Logout']")

    def verify_home_page_is_displayed(self,wait:WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located( self.__logout))
            print('Home page is displayed')
            return True
        except:
            print('Home page is NOT displayed')
            return False