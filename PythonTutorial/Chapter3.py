x = 'Krishna'
print(x[0])
print(x[1])
print(x[6])
print(x[0:4])
print(x[3:7])
print(x[:])
print(x[:4])
print(x[5:len(x)])

# STRING FUNCTIONS
print(x.lower())
print(x.capitalize())
print(x.upper())
print(x.replace('a','Z'))

# SPLIT 
a = "Krsnarupa,Gaura,Das"
mylist = a.split(",")
print(mylist)

a = "Krsnarupa Gaura Das"
mylist = a.split(" ")
print(mylist)


# COUNT 
statement = " hare Krishna, how r u ? I am Krsnarupa Gaura Das also know as Krishna"
print('Krishna count = ', statement.count('Krishna'))

# is numeric
var1 = 'Krishna'
var2 = '7'
print(var1, type(var1), var1.isnumeric())
print(var2, type(var2), var2.isnumeric())


