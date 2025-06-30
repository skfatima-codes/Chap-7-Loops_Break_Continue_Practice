# ✅ Q1: Print numbers from 10 to 1 using a while loop
# i=10
# while(i>=1):
#     print(i)
#     i=i-1

# ✅ Q2: Print the square of numbers from 1 to 5
# i=1
# while(i<=5):
#     print(i*i)
#     i+=1

# ✅ Q3: Check if a number is even or odd using if
# a=0
# if(a%2==0):
#     print("a is a even no")
# elif(a%3==0):
#     print("a is a odd no")
# else:
#     print("a is neither odd or even")

# ✅ Q5: Find sum of even numbers from 1 to 20 using for loop
# i=2
# sum=0
# while(i<=20):
#     sum=sum+i
#     print(sum)
    # i+=2

# i = 1
# while i <= 3:
#     j = 1
#     while j <= 2:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1

# Reverse a string using for loop
# name="Fatima"
# reversed_name=""
# for r in range(5,-1,-1):## loop from 5 to 0
#     reversed_name+=name[r]
#     print(reversed_name)

text = "hello"
reversed_text = ""

for i in range(4, -1, -1):  # loop from 4 to 0
    reversed_text += text[i]

print("Reversed:", reversed_text)



