import xlrd
import xlwt
# import xlwt3
from  xlutils.copy import copy
import os

class SaveData:
    def __init__(self):
        pass


    def save_txt(self,filename,rowlist):
        path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        with open(path,'w+')  as f:
            f.write('\n'.join(list(map(str, rowlist))))


    def save_excel_once(self,filename,list,sheet_name='Sheet1',col=0):
        path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        wb = xlwt.Workbook()
        sheet = wb.add_sheet(sheet_name)
        for i in range(len(list)):
            sheet.write(i,col,list[i])
        wb.save(path)


class SaveExcel:
    def __init__(self,filename,sheet_name):
        # self.path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        self.path = '/result/' + filename

        self.wb = xlwt.Workbook()
        self.sheet = self.wb.add_sheet(sheet_name)

    def write(self,row,col,value):
        self.sheet.write(row,col,value)

    def save(self):
        self.wb.save(self.path)


