import xlwt
import xlwt3
import xlutils

class SaveData:
    def __init__(self):
        pass


    def save_txt(self,path,rowlist):
        with open(path,'w+')  as f:
            f.write('\n'.join(list(map(str, rowlist))))


    def save_excel(self,path,sheet_name,list):
        wb = xlwt3.Workbook()
        sheet = wb.add_sheet(sheet_name)
        for i in range(len(list)):
            sheet.write(i,0,list[i])
        wb.save(path)



def main():
    data = SaveData()
    data.save_excel('output.xls','output',range(10))
    data.save_txt('output.txt',range(10))


if __name__ == '__main__':
    main()
