#Liesel Wong
#SoftDev
#K03 -- PythonNames/Python/Code which prints a random name from period 1 soft dev, and a random name from pd 2 soft dev
#2021-9-22

import random
#Lists of period 1 and 2
pd1 = ['Owen Yaggy', 'Haotain Gan', 'Ishraq Mahid', 'Kevin Cao', 'Ivan Lam', 'Michelle Lo', 'Christopher Liu', 'Michael Borzuk', 'Ivan Mijacika', 'Lucas Lee', 'Rayat Roy', 'Emma Buller', 'Andrew Juang', 'Renggeng Zheng', 'Annabel Zhang', 'Alejandro Alonso', 'Deven Mahehwari', 'David', 'Aryaman Goenka', 'Oscar Wang', 'Tami Takada', 'Yusuf Elsharawy', 'Ella Krechmer', 'Tomas Acuna', 'Tina Nguyen', 'Sadid Ethun', 'Shyne Choi', 'Shriya Anand', 'lol28', 'lol29', 'lol30', 'lol31']
pd2 = ['Patrick Ging', 'Raymond Yeung', 'Josephine Lee', 'Alif Abdullah', 'William Chen', 'Justin Zou', 'Andy Lin', 'Rachel Xiao', 'Yuqing Wu', 'Shadman Rakib', 'Liesel Wong', 'Daniel Sooknanan', 'Cameron Nelson', 'Austin Ngan', 'Thomas Yu', 'Yaying Liang Li', 'Jesse Xie', 'Eric Guo', 'Jonathan Wu', 'Zhaoyu Lin', 'Joshua Kloepfer', 'Noakai Aronesty', 'Yoonah Chang', 'Hebe Huang', 'Wen Hao Dong', 'Mark Zhu', 'lul26', 'lul27', 'lul28', 'lul29', 'lul30', 'lul31']
#random function to pick a random person in the class
a = random.randint(0,32)
b = random.randint(0,32)
#Prints the list indices corresponding to the random number 
print("pd1: " + pd1[a])
print("pd2: " + pd2[b])
