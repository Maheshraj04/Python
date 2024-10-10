# creating a tuple
# color=("red","green","blue")
# creating a tuple with one element
# a=("red",)

# another way is 
# a=tuple(("red"))

# cheaking leng of tuple
# print(len(color))

#acessing the item in tuple
# print(color[1]) #positive indexing
# print(color[-1])#negative indexing
# print(color[1:3])#range indexing and also we take +1 to print whole  tuple
# print(color[-2:])#negative indexing


#reversing the tuple
# ituple=(1,2,3,4,5,6)
# list=[]
# for x in reversed(ituple):
#     list.append(x)
# otuple= tuple(list)
# print(otuple)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n *factorial(n-1)
# # factorial()


# r, k = map(int, input().split())

# if r>k:
#     print("Ram is heavier than Karan")
# elif  r<k:
#     print("Karan is heavier than Ram")
# else:
#     print("Ram & Karan have the same weight")#split function is used to  take multiple input in one line

student1, student2 = input().split()
p1,p2=map(float,input().split())
if p1>p2:
    print(student1)
elif p1<p2:
    print(student2)
else:
    print("equal")
    
