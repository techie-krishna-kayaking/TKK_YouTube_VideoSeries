print("=========== dictionary ===========")
# dictionary
my_dic = {'Apple':100, 'Mango':80,'Pineapple':40}
print(my_dic)
print(my_dic['Apple'])
# my_dic.pop('Apple') # delete the apple
print(my_dic)
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())

my_dic1 = {'Apple':100, 'Mango':{'mango1':80,'mango2':95,'mango3':55},'Pineapple':40}
print(my_dic1['Mango'])
print(my_dic1['Mango']['mango1'])

print("=========== SETS ===========")
# SETS
a = {1,2,3,5,7,11,11,11}
print(a)
b = {8,9,10,5,7}

print(a.union(b))
print(a.intersection(b))

a.remove(2)
print(a)
a.add(12)
print(a)

print(type(a))

print("=========== TUPLES ===========")
my_tup = (1,2,3,4,5,6,7,7,7)
print(my_tup, type(my_tup))
my_tup_lis = list(my_tup)
print(my_tup_lis, type(my_tup_lis))
my_tup_lis.pop()

my_reverse_tup = tuple(my_tup_lis)
print(my_reverse_tup)