# def palindrom(name):
#     reverse_str=name[::-1]
#     if name==reverse_str:
#         print("palindrom string")
#     else:
#         print("not palindrom")

# str="madam"
# palindrom(str)        



# def check(c):
#     if len(c)!=1:
#         return "Please enter only a single character."
    
#     if c.isalpha():
#         if c.lower() in 'aeiou':
#             return "Vowel Numbers"
#         else:
#             return "Consonant"
#     elif c.isdigit():
#         return "Digit Numbers"
#     else:
#         return "Special Characters"
# xyz=input("Enter a character")
# Result=check(xyz)
# print("The REsult is:",Result)




# Fibonacci series: [0, 1, 1, 2, 3, 5, 8]
# def fibonacci(n):
#     a,b=0,1
#     result=[]

#     for _ in range(n):
#         result.append(a)
#         a,b=b,a+b
#     return (result)    
# num = int(input("Enter the number of terms in the Fibonacci series: "))
# if num<=0:
#     print("Please enter a positive integer.")
# else:
#     s=fibonacci(num)
#     print("Fibonnaci Series",s)






# name=['Python','C++','Java','.Net']
# for i in range(1,len(name)+1):
#     print(f"{i}.{name[i-1]}")




# count same data in string
# l1 = "a,a,b,b,b,b,b,b,b,b,c,c,c,c,c,c"
# l1=l1.split(',')
# l2=[]
# l3=[]
# for i in l1:
#     if i not in l3:
#         l2.append(f"{i}{l1.count(i)}")
#         l3.append(i)
# print(l2)



# name=("My","Company","Name","is","Codevibe")
# a=''
# for i in name:
#     a=a+i
# print(a)


#  ------ check prime number or not------
# n=int(input("Enter number ="))
# l=[]
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# print(f"{n} is divisable by {l}")
# if len(l)==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")



# student=int(input("enter number of student"))
# averagedata=[]
# student_name=[]
# for i in range(1,student+1):
#     stu_name=input("Enter student name = ")
#     print("Result of ",stu_name)
#     student_name.append(stu_name)
#     s1=int(input("Enter marks of Hindi = ")) 
#     s2=int(input("Enter marks of English = "))
#     s3=int(input("Enter marks of Gujarati = "))

#     avg=(s1+s2+s3)/3
#     averagedata.append(avg)
#     if avg>=40:
#         print("PASS")
#     else:
#         print("FAIL")
# # print(averagedata)
# # print(student_name)
# result=max(averagedata)
# r=averagedata.index(result)
# # print(r)
# toper_name=student_name[r]
# print("Higest scorer is",toper_name)
# print("Higest score of class is ",result)




# i=0
# while i==0:
#     n=input("Enter one character(digit/alphabets/special character)")
#     if len(n)!=1:
#         print("Enter only one character")
#     else:
#         if n.isalpha():
#             if n.islower():
#                 if n in "aeiou":
#                     print(n,"is vowels (lower case)")
#                 else:
#                     print(n,"is consonant (lower case)")
#             else:
#                 if n in "AEIOU":
#                     print(n,"is vowels (UPPER case)")
#                 else:
#                     print(n,"is consonant (UPPER case)")
#         elif n.isdigit():
#             if int(n)<0:
#                 print(n,"is negative digit")
#             elif int(n)>0:
#                 print(n,"is positive digit")
#             elif int(n)==0:
#                 print(n,"is zero")
#             else:
#                 print("Invalid data")
#         else:
#             print(n,"is special character")
#     ch=input("Enter choice yes/no = ").strip().lower()
#     if ch=='yes':
#         i=0
#     else:
#         i=1


marks = 85 
if marks >= 90: 
    print("Grade: A") 
elif marks >= 80: 
    print("Grade: B") 
elif marks >= 70: 
    print("Grade: C") 
elif marks >= 60: 
    print("Grade: D") 
else: 
    print("Grade: F") 