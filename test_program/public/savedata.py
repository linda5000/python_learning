import time
import xlrd,xlwt
# import xlwt3
# from  xlutils.copy import copy
from public.globalpath import savedata_path
from public.log import Log

log = Log("SaveData")

class SaveData:
    def __init__(self):
        pass


    def save_txt(self,filename,rowlist):
        path = savedata_path + filename
        with open(path,'w+')  as f:
            f.write('\n'.join(list(map(str, rowlist))))


    def save_excel_once(self,filename,list,sheet_name='Sheet1',col=0):
        path = savedata_path + filename
        wb = xlwt.Workbook()
        sheet = wb.add_sheet(sheet_name)
        for i in range(len(list)):
            sheet.write(i,col,list[i])
        wb.save(path)


class SaveExcel:
    def __init__(self,filename,sheet_name):
        self.filename =  filename + "_" + time.strftime('%Y-%m-%d_%H_%M_%S') + ".xls"
        self.path = savedata_path + self.filename
        self.wb = xlwt.Workbook()
        self.sheet = self.wb.add_sheet(sheet_name)

    def write(self,row,col,value):
        self.sheet.write(row,col,value)

    def save(self):
        try:
            self.wb.save(self.path)
            log.debug(self.filename + "保存成功")
        except Exception as e:
            log.error(e)



