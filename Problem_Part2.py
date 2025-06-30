# Factorial of a number
# f=1
# n=3
# for i in range(1,n+1):
#     f=f*i
#     print(f)
n=int(input("Enter a number"))
factorial=1
for i in range(1,n+1):# n+1 tkay n 5 tk jaskay
    factorial= factorial* i

print(f"The factorial of {n} is {factorial}") # we have to remove indent beofre printing or else it will print iteration values