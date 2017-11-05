from readdata import ReadData
from config import Config
from mylog import Log

log = Log('loaddata')

class LoadData:
    def __init__(self,input_file=None,input_sheet=None,Baseline_sheet=None):
        if input_file is None:
            input_file = 'input.xls'
        else:
            input_file = input_file
        if input_sheet is None:
            input_sheet = 'Input'
        else:
            input_sheet = input_sheet
        if Baseline_sheet is None:
            Baseline_sheet = 'Baseline'
        else:
            Baseline_sheet = Baseline_sheet

        mode = Config().getConfig("flag", "mode")
        input_data = ReadData().read_excel(input_file, input_sheet)
        expect_data= ReadData().read_excel(input_file, Baseline_sheet)
        self.test_data = []
        if mode == '1':
            case_list = range(1,len(request_list))
        elif mode == '0':
            case_list = eval(Config().getConfig("flag", "caselist"))
        else:
            case_list = []
            log.error("mode配置有误")

        for i in case_list:
            input_data[i].extend(expect_data[i][1:])
            self.test_data.append(input_data[i])

def main():
    test_data = LoadData().test_data
    print(test_data)


if __name__ == '__main__':
    main()