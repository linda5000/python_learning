import xlrd
import xlutils

file = 'test.xls'
wb = xlrd.open_workbook(file)
print(wb)
sheet = wb.sheet_by_index(0)
col = sheet.col_values(0)


wb2 = xlwt.Workbook()
sheet = wb2.add_sheet('sheet2')
sheet.write(0, 1, 'hello world')
wb.save('test2.xls')