# Python program to display all the prime numbers within an interval

import datetime

lower =  999999999
upper = 1100000099

print("Prime numbers between", lower, "and", upper, "are:")

st = datetime.datetime.now()
print("Start Time:-", st.strftime("%H:%M:%S:%f"))

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           #print("num = ", num, " i = ",i)
           if (num % i) == 0:
               #print(num,"is not a prime number")
               #print(i,"times",num//i,"is",num)
               break
       else:
            print(num,"is a prime number")

et = datetime.datetime.now()
print("End Time:-", et.strftime("%H:%M:%S:%f"))

elapsed = et-st

print("Total Time is", elapsed)