from pyjavaproperties import Properties
import openpyxl
class Utility:
    @staticmethod
    def get_property_value(path,key):
        ppt_obj = Properties()
        ppt_obj.load(open(path))
        value = ppt_obj[key]
        return value

    @staticmethod
    def get_xl_data(path,sheet_name,row,col):
        value=''
        try:
            wb = openpyxl.load_workbook(path)
            sheet = wb[sheet_name]
            value = sheet.cell(row,col).value
            if value == None:
                value = ''
            wb.close()
        except:
            print('some exception')

        return value