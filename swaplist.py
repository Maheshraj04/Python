n=int(input("enter the size of the list:"))
list=[]

for _ in range(n):
    num=int(input())
    list.append(num)
print(list)

ind1=int(input("Enter the index1:"))
ind2=int(input("Enter the inxex2:"))
#swapping the value in list
temp=list[ind1]
list[ind1]=list[ind2]
list[ind2]=temp
print(list)