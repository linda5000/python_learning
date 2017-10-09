data = [
        ("animal", "bear"),
        ("animal", "duck"),
        ("plant", "cactus"),
        ("vehicle", "speed boat"),
        ("vehicle", "school bus")
    ]

groups = {}

# for (key, value) in data:
#     if key in groups:
#         groups[key].append(value)
#     else:
#         groups[key] = [value]

# dict.setdefault(key, default=None)
# 如果键不存在于字典中，将会添加键并将值设为默认值。

for (key, value) in data:
    groups.setdefault(key, []).append(value)

print(groups)

# 用 get 获取字典中的值
# dict.get(key, default=None)
# 函数返回指定键的值，如果值不在字典中返回默认值。

print(groups.get("people","chinese"))


from collections import defaultdict

# 这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型是function_factory的类实例，而且具有默认值。
# 比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.

groups = defaultdict(list)
for (key, value) in data:
    groups[key].append(value)

print(groups)


# 字典推导式
numbers = [1, 2, 3]
d = {number: number * 2 for number in numbers}
print(d)


# 用 fromkeys 将列表转换成字典
# dict.fromkeys(seq[, value]))
# 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。

d1 = {number:[] for number in numbers}
d2 = dict.fromkeys(numbers,[])

print(d1)
print(d2)

# fromkeys 延伸
# d = {number:[] for number in numbers}
# d = dict.fromkeys(numbers,[])
# 两种方法的差异

d1[1].append(1)
d2[1].append(1)
print('d1:',d1)
print('d2:',d2)

# Python 中 list 是可变类型，在作为参数传递的时候是传引用的。
# 所以 fromkeys 函数把所有 key 都指向了同一个空列表。改动其中任何一个，其他的都改掉了。

print('d1:',id(d1[1]),id(d1[2]))
print('d2:',id(d2[1]),id(d2[2]))