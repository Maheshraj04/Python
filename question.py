#Question1: Take positive integer input and tell if it is a four digit number or not.
# a=int(input("enter the number:-"))
# if a>0:
#     if len(str(a))==4:
#         print("four digit number")
#     else :
#         print("not a four digit number")


#Question2: Take positive integer input and tell if it is divisible by 5 and 3.

# a =int(input("enter the number :-"))
# if a>0:
#     if a%3==0 and a%5==0:
#         print("divisible by 3 and 5")
#     else:
#         print("not divisible")


#Question: Take positive integer input and tell if it is divisible by 5 or 3.
# n=int(input("enter the number:-"))
# if n>0:
#     if n%5==0 or n%3==0:
#         print("divisible by 3 or 5")
#     else:
#         print("not divisible by 3 or 5")

# #Question: Take 3 positive integers input and print the greatest of them.
# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=int(input("enter the number: "))
# if a>0 and b>0 and c>0:
#     if a>b and a>c:
#         print("a is greatest")
#     elif b>a and b>c :
#         print("b is greatest")
#     else:
#         print("c is greatest")


#Question: Determine whether the year is a leap year or not
# n=int(input("enter the year:-"))
# if (n%4==0 and n%100!=0) or(n%400==0):
#     print("leap year")
# else:
#     print("not leap year")


# #Question: Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.

# number = int(input("Enter a positive integer: "))
 
# # Checking divisibility conditions using nested if-else
# if number % 15 == 0:
#     print("The number is divisible by 15.")
# else:
#     if number % 5 == 0 or number % 3 == 0:
#         print("The number is divisible by 3 or 5 but not by 15.")
#     else:
#         print("The number is neither divisible by 3 nor by 5.")



#Question: Take 3 positive integers input and print the greatest of them (without using multiple condition)
  # Taking three positive integer inputs from the user
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# num3 = int(input("Third number: "))
 
# # Comparing the numbers to find the greatest using nested if-else
# if num1 >= num2:
#     if num1 >= num3:
#         greatest = num1
#     else:
#         greatest = num3
# else:
#     if num2 >= num3:
#         greatest = num2
#     else:
#         greatest = num3
 
# # Printing the greatest number
# print("\nThe greatest number is:", greatest)


# Question: Take input percentage of a student and print the Grade according to marks:
# 1) 81-100 Very Good
# 2) 61-80 Good
# 3) 41-60 Average
# 4) <=40 Fail

# a=int(input("Enter the number:-"))
# if a>=100:
#        print("invalid")
# elif a>=81:
#     print("Very Good")
# elif a>=61:
#         print("Good")
# elif a>=41:
#         print("Average")
# else:
#         print("Fail")

#Question: Write a program to check if number is odd or even using ternary operator.
# a=int(input("enter the number:-"))
# print("Even")  if a%2==0 else print( "odd")


#Question: Print hello world ‘n’ times. Take ‘n’ as input from user.
# n=int(input("enter the number:-"))
# for i in range(n):
#     print("Hello World")


#Question: Print numbers from 1 to 100
# a=int(input("Enter the number:-"))
# for i in range(1,101):
#     print(i)

#Question: Display this AP - 1,3,5,7,9.. upto ‘n’ terms.?
# n = int(input("Enter the number of terms: "))

# ap = []
# for i in range(n):
#     ap.append(1 + 2*i)

# print(ap)



#write the code for G.P?

# a= (float(input("First term of the G.P.")))
# r =(float(input( "Common ratio of the G.P.")))
# n =(int(input("Term number to calculate.")))

# gp=[]
# for i in range(n):
#     gp.append(a*(r**i))
# print(gp)


#calculate factorial
# n=int(input("enter the number:"))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)


import math
a=int(input("enter the value1:-"))
b=int(input("enter the value2:-"))
c=int(input("enter the value3:"))
print(math.gcd(a,b,c))


