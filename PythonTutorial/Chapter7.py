print("===== FUNCTIONS =====")
def my_fn():
    print("krishna")

my_fn()


for i in range(0,5):
    print("in loop")
    my_fn()

print("===== AGE VERIFICATION FUNCTIONS =====")
def age_fns(age):
    print(age)
    if(age >= 18 and age < 60):
        print("eligible for driving license")
    elif(age < 0):
        print("not born yet")
    elif(age > 60):
        print("too old to drive, give the test again")
    else:
        print("you are yet to become an adult")

age_fns(70)



print("===== SQUARE FUNCTIONS =====")
def sq_fns(px):
    return px*px

# n = 7
# sq = sq_fns(n)
print(sq_fns(9))