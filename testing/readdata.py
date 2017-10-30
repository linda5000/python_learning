import xlrd
import os

class ReadData:
    def __init__(self):
        pass

    # 从excel读取测试数据,返回列表
    def read_excel(self,filename,sheet_name):
        list = []
        path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        try:
            wb = xlrd.open_workbook(path)
            sheet = wb.sheet_by_name(sheet_name)
        except Exception as e:
            print('excel读取失败：%s'%e)
        else:
            key = sheet.row_values(0,1,)
            nrows = sheet.nrows
            ncols = sheet.ncols
            for i in range(nrows):
                row = []
                for j in range(ncols):
                    cell = sheet.cell(i, j)
                    ctype = cell.ctype  # 单元格数据类型
                    cell = cell.value
                    if ctype == 2 and cell % 1 == 0:  # 如果是整形
                        cell = int(cell)
                    elif ctype == 3:   # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    row.append(cell)
                list.append(row)
        return list




    # 从文本文件读取测试数据,返回列表
    def read_cvs(self,filename):
        list = []
        path = os.path.split(os.path.realpath(__file__))[0] + '/data/' + filename
        try:
            f = open(path, 'r+', encoding='utf8')
        except IOError as e:
            print('文件读取失败：%s' % e)
        else:
            for line in f:
                list.append(line.replace('\n', '').split(','))
            f.close()
        return list


def main():
    data = ReadData()
    list = data.read_excel('input.xls','input')
    print(list)

if __name__ == '__main__':
    main()