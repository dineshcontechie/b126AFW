from generic.base_class import BaseClass
from generic.lib import Utility
class Test_Script1(BaseClass):
    def test_script1(self):
        print(self.driver.title)
        data=Utility.get_xl_data(self.xl_path,'script1',2,1)
        print('data from xl',data)