# list
mylist = ['Krishna','Radha','Jagannath']
print(mylist)

for i in mylist:
    print(i)

print(mylist[2])

print("====================")
for i in mylist:
    if(i.upper() == 'KRISHNA'):
        print(i, " is my name")

for i in range(1,11):
    print(i)

print("====================")
for i in mylist:
    print(i)
    for j in i:
        print(j)

print("====================")
for i in mylist:
    if(i.upper() == 'KRISHNA'):
        print(i, "is my name")
        break

print("====================")
for i in mylist:
    if(i.upper() == 'KRISHNA'):
        break
    print(i, "is my name") # this statement will not execute


print("====================")
x = 1 
while (x<10):
    print(x)
    x+=1 # x = x+1

x = 1
while (x<5):
    print('krishna')
    x=x+1

print("====================")
print("====================")

my_lis = [1,2,3,4,[7,8,9],'Krishna','Radha','Sudevi',5]
print(my_lis)
print(my_lis[3])
print(my_lis[4])
print(my_lis[4][0])
print(my_lis[-3])
print(my_lis[3:7])
print("====================")
my_lis.append("Govardhan")
print(my_lis)

my_lis.insert(1,'Sudarshan')
print(my_lis)

my_lis.pop()
print(my_lis)

my_lis.reverse()
print(my_lis)

my_lis.remove(1)
print(my_lis)


print("====================")
my_list = [1,2,3,4,5,6,7]
print(my_list)
new_list = []
for i in my_list:
    new_list.append(i*i)
    # new_list.append(i*i*i)

print(new_list)

print("====================")
new_list1 = [i*i for i in my_list]
print(new_list)

new_list1 = [i*i for i in my_list if (i%2) == 0]
print(new_list1)
