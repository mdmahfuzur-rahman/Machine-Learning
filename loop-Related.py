#exercise 01:Print the first 10 natural numbers using for loop.
'''i = 1
while i <= 10:
    print (i)
    i += 1'''

#exercise 02: Python program to print all the even numbers within the given range.
'''
i = 0
while i <= 100:
    print (i)
    i += 2
'''

#using for loop

'''
given_range = 51
for i in range (given_range):
    if i % 2==0:
        print(i)
'''

'''
for i in range(10,0,-2):
    print(i)
'''
#exercise 03: Python program to calculate the sum of all numbers from 1 to a given number.
'''
given_number = 5
i = 1
sum=
while i<=given_number:
    sum = sum + i
    i+=1
print(sum)
'''
#using for loop

'''
given_number = 5
sum = 0
for i in range(1,given_number+1):
    sum+=i
print(sum)
'''
#exersice 04:Python program to calculate the sum of all the odd numbers within the given range.
'''
given_range = 20
i=1
sum = 0
while i<=given_range:
    sum += i
    i+=2
print(sum)
'''

#Using for loop

'''
given_number = 20
sum = 0
for i in range(1,given_number+1,2):
    sum+=i
print(sum)

'''

 #exersice 05:Python program to print a multiplication table of a given number
'''
given_number = 10
i = 0
multi = 0
while i <= 10:
    multi = given_number * i
    print(f"{given_number} * {i} =",multi)
    i+=1
    #print(f"{given_number} * {i} = {given_number * i}" )
'''

#using for loop

given_number = 12
multi = 0
for i in range (0,11,1):
    multi = given_number * i
    print(f"{given_number} * {i} =", multi)

#different formatting
'''given_number = 5

for i in range(11):
    print(given_number, " x", i, " =", 5 * i)

'''
#exersice 06: Python program to display numbers from a list using a for loop.

"""
list = [2,1,5,71]
for i in list:
     print(i)
"""

#exersice 07:Python program to count the total number of digits in a number.



