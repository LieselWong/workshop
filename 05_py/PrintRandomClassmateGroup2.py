#Liesel Wong
#SoftDev
#K05 -- Sept-24-MakeupCW/Python Random Classmate Generator with Group 2/Revised our original solutions to the random classmate problem
#2021-09-24

#What we discussed: We decided to send each other the code we had with our original trios. We then chose to pick the parts of the code that would make the program do as little work as possible to give us a random name, while also making the code as easy to read and understand as possible. To this end, we chose to store our names in two seperate arrays, choose a random index and store those results in two variables, and then print out a name from either one of the periods. Each of these three sections of code were taken from our individual programs.
#Discoveries: One of the group members did not know Kevin Cao was in period 2, and put Kevin in period 1. That was resolved.
#Questions: None, really
#Comments: The refactoring and combination process was rather fun, mixing and matching code to create a representative program.

#Start of code
import random

#Dictionary containing names of people in each period
names = {
    'pd1' : ['Owen Yaggy', 'Haotain Gan', 'Ishraq Mahid', 'Ivan Lam', 'Michelle Lo', 'William Chen', 'Christopher Liu', 'Michael Borzuk', 'Ivan Mijacika', 'Lucas Lee', 'Rayat Roy', 'Emma Buller', 'Andrew Juang', 'Renggeng Zheng', 'Annabel Zhang', 'Alejandro Alonso', 'Deven Mahehwari', 'David', 'Aryaman Goenka', 'Oscar Wang', 'Tami Takada', 'Yusuf Elsharawy', 'Ella Krechmer', 'Tomas Acuna', 'Tina Nguyen', 'Sadid Ethun', 'Shyne Choi', 'Shriya Anand'],
    'pd2' : ['Patrick Ging', 'Raymond Yeung', 'Josephine Lee', 'Alif Abdullah', 'Justin Zou', 'Andy Lin', 'Rachel Xiao', 'Yuqing Wu', 'Shadman Rakib', 'Liesel Wong', 'Daniel Sooknanan', 'Cameron Nelson', 'Austin Ngan', 'Thomas Yu', 'Yaying Liang Li', 'Jesse Xie', 'Eric Guo', 'Jonathan Wu', 'Zhaoyu Lin', 'Joshua Kloepfer', 'Noakai Aronesty', 'Yoonah Chang', 'Hebe Huang', 'Wen Hao Dong', 'Mark Zhu', 'Kevin Cao']
}
#Variables used to hold randomly selected indeces from both lists in the names dictionary
pd1Chosen = random.randint(0,len(names['pd1'])-1)
pd2Chosen = random.randint(0,len(names['pd2'])-1)

#Printing a randomly selected name, chosen by the variables above, from one of the two lists within the names dictionary above, as determined by the code below.
if (random.randint(0, 1) == 0):
    print("Period 1 Name: " + names['pd1'][pd1Chosen])
else:
    print("Period 2 Name: " + names['pd2'][pd2Chosen])
