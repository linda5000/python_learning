import jieba

string = '其实大家买手机就是看个心情，没必要比来比去的。'
seg = jieba.cut(string)

l = []
for i in seg:
    l.append(i)
print(l)