import random
from output import Output

# 用户类
class User:
    def __init__(self,name=None,age = None,sex = None):
        self.name = name
        self.age = age
        self.sex = sex


# 生成用户集合
class Create_user_set:
    def __init__(self,n):
        self.n = n

    # 模拟用户数据集
    def moni(self,sequence):
        user_set = []

        while True:
            name = self.name(sequence)
            age = self.age()
            sex = self.sex()
            is_exist = 0
            for i in user_set:
                if name == i.name:
                    is_exist = 1
                    break
            if is_exist == 0:
                u = User(name, age, sex)
                user_set.append(u)
                if  len(user_set) == self.n:
                    break

        return user_set



    # 构造人名
    def name(self,sequence,k=None):
        if k == None:
            k = random.choice((2,3))
        sample = random.sample(sequence,k)
        name = ''.join(sample)
        return name



    # 构造年龄
    def age(self):
        age = str(random.randint(10, 100))
        return age


    # 构造性别
    def sex(self):
        sex = random.choice(("男", "女"))
        return sex

    #真实用户数据集
    def real(self,db_config):
        user_set = []
        # 用sql读取数据库用户数据，暂不实现
        # for i in list:
        #     u = User(name=,age=,sex=)
        #     user_set.append(u)
        return user_set


s = ['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨','朱','秦','尤','许']
n = 100
mus = Create_user_set(n).moni(s)
output_file = 'user_info.txt'

context = []
for i in mus:
    print(i.name,i.age,i.sex)
    context.append(i.name + ',' + i.age + ',' + i.sex)

Output().write_list(output_file, context)





