import xlwt
# import xlwt3
import xlutils
import os

class SaveData:
    def __init__(self):
        pass


    def save_txt(self,filename,rowlist):
        path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        with open(path,'w+')  as f:
            f.write('\n'.join(list(map(str, rowlist))))


    def save_excel(self,filename,list,sheet_name='Sheet1',col=0):
        path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        wb = xlwt.Workbook()
        sheet = wb.add_sheet(sheet_name)
        for i in range(len(list)):
            sheet.write(i,col,list[i])
        wb.save(path)



def main():
    data = SaveData()
    rowlist = range(10)
    data.save_excel('output.xls',rowlist,'output')
    data.save_txt('output.txt',rowlist)


if __name__ == '__main__':
    main()
