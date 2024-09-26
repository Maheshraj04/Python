#wap right angle traingle
n=int(input("Enter the number:"))

for i in range (1,n+1):
    print("*"*i)


#print from left to right
n=int(input("Enter the number :"))
for i in range(1,n+1):
     print(" "*(n-i)+"*"*i)

#inverted right angle traingle
n=int(input("Enter the number:"))
for i in range (1,n+1):
    print("*"*(n-i+1))

#pyramid pattern
n=int(input("Entar the number:"))
for i in range(1,n+1):
    print((" "*(n-i)+"*"*(2*i-1)))


   
     