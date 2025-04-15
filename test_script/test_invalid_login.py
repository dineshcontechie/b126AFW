from generic.base_class import BaseClass
from generic.lib import Utility
from page.login_page import LoginPage


class Test_Invalid_Login(BaseClass):

    def test_invalid_login(self):
        un = Utility.get_xl_data(self.xl_path, 'invalid_login', 2, 1)
        pw = Utility.get_xl_data(self.xl_path, 'invalid_login', 2, 2)

        # 1. enter invalid username
        loginpage=LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. enter invalid password
        loginpage.set_password(pw)
        # 3. click on Go button
        loginpage.click_go_button()
        # 4. verify that error message is displayed
        result=loginpage.verify_err_msg_is_displayed(self.wait)
        assert result