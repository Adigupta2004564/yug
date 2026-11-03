# from adi import check
# lst = [1,5,32,"hdhf","ahfkg"]
# print(check(lst))
# import random
# print(random.randint(1,45))
# import django
# import os
# os.makedirs('hdj')
# from adi import check
# lst = [1,5,32,"hdhf","ahfkg"]
# print(check(lst))
# x = "jdfjl"
# y = 5435
# try:
#     z = x+y
# except:
#     print("can not add x,y")
# a = 5
# b = 0
# try:
#     dev = a/b
#     # print(dev)
# except:
#     ("can not devide by zero")

# def fun(num):
#     if num < 4:
#         result = num/(num-3)
#     print(result)

# try:
#     fun(0)
#     fun(1)
#     fun(2)
#     fun(3)
# except NameError as n:
#     print(n)
# except:
#     print('not valid')
# my_dict = {'a' : '1', 'b' : '2', 'c' : '3'}

# try:
#     print(mydict)
# except NameError:
#     print('please check the spelling of dictionary name')
# except TypeError:
#     print('it seems that some of the dictionary values are not numeric')
# except AttributeError:
#     print('you should provide a python dictionary with numeric values')
# f = open("nstifile.txt", 'w')
# f.write('hello')
# f.close()
# f = open("nstifile.txt", 'a')
# f.write('hello')
# f.close()
# f = open("nstifile.txt", 'r')
# readline = f.readlines()
# print(readline)
# f.close()
# f = open('nstifile.dat' , 'wb')
# f.write(b"hello")
# f.close()
# class Animal:
#     def dog(self,name):
#         print(name)

#     def cat(self,name):
#         print(name)

# object = Animal()
# object.dog("labro")
# object.cat("sweety")
# class student:
#     student_name = "NSTI Dehradun"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_details(self):
#         print(f"student name is {self.name} and his age is {self.age}")
    
# o = student("hfdhk",45)
# o.get_details()
# class Animal:
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age

#     def dog(self):
#         return(self.name,self.age)

#     def get_details(self):
#         print(f"his name is {self.name} and age {self.age} year old")

# object = Animal("koko",4)
# (object.get_details())
# print(object.dog())
# f = open('file.txt','w')
# f.write('hello students\n')
# f.writelines(['i am aditya\n','learning aipa course'])
# f.close()
# f = open('file.txt','r')
# print(f.readlines())
# f.close()
# f = open('nsti.dat','wb')
# f.write(b'hello students\n ')
# f.writelines([b'i am aditya\n ',b'learning aipa course'])
# f.close()
# f = open('file.txt','rb')
# content = (f.readline())
# print(content)
# f.close()
# with open('file.txt','r') as l:
#     conte = l.readlines()
#     print(conte)

# def square(a):
#     return(a ** 2)

# print(square(5))

# def even(n):
#     return (n % 2 == 0)
# print(even(6))
# try:
#     num = float(input("enter a number: "))
# except:
#     print("Please enter a valid number")
# a = 5
# b = 0
# def save_divide (a,b):
#     try:
#         z = a/b
#         print(z)
#     except ZeroDivisionError:
#         print ("Cannot divide by zero")
    
# print(save_divide(1,0))


# try:
#     with open("data.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print(("file not found"))

# class grandfather:
#     def __init__(self,name):
#         self.name = name
#         self.surname = "sher"

# class father(grandfather):
#     def __init__(self,name,job):
#         super().__init__(name)
#         self.job = job

# class child(father):
#     def __init__(self,name,job,school):
#         super().__init__(name,job)
#         self.school = school

#     def output(self):
#         print(f"{self.name} {self.surname} {self.job} {self.school}")

# c = child("aarav","student","krp")
# c.output()
        

# class grandfather:
#     def __init__(self,name):
#         self.name = name
#         self.surname = "sher"

# class father():
#     def __init__(self,name,job):
#         super().__init__(name)
#         self.job = job

# class child(father,grandfather):
#     def __init__(self,name,job,school):
#         super().__init__(name,job)
#         self.school = school

#     def output(self):
#         print(f"{self.name} {self.job} {self.school}")

# c = child("aarav","student","krp")
# c.output()
        
# class BankAccount:
#     def __init__(self,account_num,holder_name,balance):
#         self.__account_num = account_num
#         self.__holder_name = holder_name
#         self.__balance = balance
    
#     def deposite(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"deposited ${amount} New balance is ${amount}")
#         else:
#             ("deposited amount must be positive")

#     def withdrawal(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"withdrawal ${amount} new balance is ${amount}")
#         else:
#             ("not enough amount")       
#     def get_balance(self):
#         return self.__balance
# Account = BankAccount(4654,"aditya",13321)
# Account.withdrawal(5000)
# Account.deposite(500000)


# print(f"final balance ${Account.get_balance()}") 

# class employee:
#     def __init__(self):
#         self.__salary = 1000000
    
#     def __upi(self,amount):
#         self.__salary -= amount

#     def __send_recipt(self):
#         print(f"current balance is {self.__salary}")

#     def main(self):
#         amount = int(input("enter a number: "))
#         self.__upi(amount)
#         self.__send_recipt()

# o = employee()
# o.main()


# import requests

# web_name = "https://www.meesho.com/"
# response = requests.get(web_name)

# response.headers
# print(response.headers)

# import requests
# from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# h3 = (soup.find("div", class_="product_price"))
# print(h3.p)









