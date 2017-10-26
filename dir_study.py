def f1(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.isdir(os.path.join(path, i)):
            f1(os.path.join(path, i))
        else:
            print(i)

def f2(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.isfile(os.path.join(path, i)):
            print(i)
        else:
            f2(os.path.join(path, i))


path = 'E:\学习资料'
# f1(path)