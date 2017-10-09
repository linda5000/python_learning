# 输出结果
class Output:
    def __init__(self,type = None):
        self.type = type


    def write_list(self,filename,context):
        with open(filename,'w+')  as f:
            f.write('\n'.join(context))
