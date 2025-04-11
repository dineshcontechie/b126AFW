import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.support.ui import WebDriverWait
from generic.lib import Utility
import os
class BaseClass:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        generic_folder=os.path.dirname(__file__)
        print("generic folder path",generic_folder)
        print('Read data from property file')
        config_path=generic_folder+"/../config.properties"
        self.xl_path=generic_folder+"/../data/input.xlsx"
        GRID=Utility.get_property_value(config_path,'GRID')
        GRID_URL=Utility.get_property_value(config_path,'GRID_URL')
        BROWSER=Utility.get_property_value(config_path,'BROWSER')
        APP_URL=Utility.get_property_value(config_path,'APP_URL')
        ITO = Utility.get_property_value(config_path, 'ITO')
        ETO = Utility.get_property_value(config_path, 'ETO')

        if GRID.lower()=="yes":
            print("using Selenium GRID")

            if BROWSER.lower() == 'chrome':
                print('Open Chrome Browser in Remote system')
                self.driver = Remote(GRID_URL,options=ChromeOptions())
            else:
                print('Open Edge Browser in Remote system')
                self.driver = Remote(GRID_URL,options=EdgeOptions())
        else:
            print("using local system")

            if BROWSER.lower() == 'chrome':
                print('Open Chrome Browser in local system')
                self.driver = Chrome()
            else:
                print('Open Edge Browser in local system')
                self.driver = Edge()

        print('Enter the URL:',APP_URL)
        self.driver.get(APP_URL)
        print('Maximize the browser')
        self.driver.maximize_window()
        print('set ITO:',ITO)
        self.driver.implicitly_wait(ITO)
        print('set ETO:',ETO)
        self.wait=WebDriverWait(self.driver,ETO)

    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        print('Close the browser')
        self.driver.quit()