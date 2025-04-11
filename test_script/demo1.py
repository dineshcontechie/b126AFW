import openpyxl

wb=openpyxl.load_workbook("./../data/input.xlsx")
sheet=wb['script1']
value=sheet.cell(2,1).value
print(value)
wb.close()