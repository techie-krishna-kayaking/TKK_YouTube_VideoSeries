# numeric operations
# print(3+4)

a = 7
b = 5

c = a + b
print('c=',c)

print('a+b=',a+b)
print('a-b=',a-b)
print('axb=',a*b)
print('a/b=',a/b)
print('a%b=',a%b)

c = 7
d = '7'
print(c, type(c))
print(d, type(d))


# indentations
result = 10 + 11 - 15 * 5 \
      / 100 + 5 + 6 - 100 * 500 

print(" hi this is krishna \n \
\t I am doing good")


# type casting
# implicit
x = 7
y = 7.7
print(type(x), type(y), type(x+y), x+y)

# explicit
x = '7'
y = 7
print(type(x), type(y), type(int(x)+y), (int(x)+y))