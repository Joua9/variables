'''
For this assignment you should read the task, then below the task do what it asks you to do
EXAMPLE TASK:
'''
#EX) Check if 4 is equal to 5 and store the answer in variable a
a = (4==5)

'''
END OF EXAMPLE
'''

'''
START HERE
'''

#1) Check if "dog" is equal to "cat" and store the answer in variable b
print ("dog" == "cat")
b = "dog" == "cat" 
#flase 

#2) Check if 1.24 is equal to 1.25 and store the answer in variable c
print (1.24 == 1.25)
c = 1.24 == 1.25
#false 

#3) Check if True is equal to False and store the answer in variable d
print (True == False)
d = True == False 
#false

#4) Check if [1,2,3] is equal to [1,2,3] and store the answer in variable e
print ([1,2,3] == [1,2,3])
e= [1,2,3] == [1,2,3]
#true

#5) Check if 1 is less than or equal to 2 and store the answer in variable f
print (1 <= 2)
f = 1 <= 2
#true

#6) Check if 1 is greater than or equal to 2 and store the answer in variable g
print (1 >= 2)
g = 1 >= 2
#false 

#7) Check if 1.66 is greater than or equal to 1.67 and store the answer in variable h
print (1.66>= 1.67)
h = 1.66 >= 1.67
#false
#8) Check if 1.66 is less than or equal to 1.67 and store the answer in variable i
print (1.66 <= 1.67)
i = 1.66 <= 1.67
#true 

#9) Check if 1 is less than 2 and store the answer in variable j
print (1<2)
j = 1<2 
#true 

#10) Check if 1 is greater than 2 and store the answer in variable k
print (1>2)
k = 1>2 
#false

#11) Check if 11 divided by three 3 is less than 100 divided by 33 and store the answer
#  ) in variable l
print (11/3 < 100/33)
l = 11/3 < 100/33 
#false 

#12) Check if 9 times 7 is greater than 8 times 8 and store the answer in variable m
print (9*7 > 8*8)
m = 9*7 > 8*8
#false

#13) Check if the square root of 3 is less than 1.15 squared and store the answer in
#  ) variable n
print (3**(1/2) < 1.15**2) 
#false 
#14) Multiple 8 by 3 and store that in variable o, then divide 56 by 2 and store that
#  ) in variable p, finally check if o is greater then p and store the answer in variable q.
o = 8*3 
p = 56/2 
print (8*3 > 56/2)
q = 8*3 > 56/2
#false

#15) Take the square root of 96 and store that in variable r, then square 8.6 and store
#  ) that in variable s, finally check if r is greater than or equal to s and store the
#  ) answer in t
r = 96**(1/2)
s = 8.6**2
print (r >= s)
t = r >= s 
#false
'''
For the next section, you will be reading comparison statements and determining their answer
EXAMPLE:
'''
#EX) 4 == 5
False

'''
END OF EXAMPLE
'''

'''
START HERE
'''

#1) 4 == 5
False

#2) 5 == 5
True
#3) 3 == 3
True
#4) a = 2
# ) a == 2
True 
#5) a = 3
# ) b = 2
# ) a == b
False 
#6) a = 4
# ) b = 4
# ) a == b
True
#7) a = 6
# ) b = (12/2)
# ) a == b
True
#8) a = (3/3)
# ) b = (13/13)
# ) a == b
True
#9) a = 3
# ) b = math.sqrt(9)
# ) a == b
print (a==b)
True
#10) a = "word"
#  ) b = "Word"
#  ) a == b
False 
#11) (10/5) == (12/6)
print((10/5)==(12/6))
True
#12) (14/7) == (15/5)
print ((14/7)==(15/5))
False
#13) a = 10
#  ) b = 5
#  ) (a/b) == 2
True
#14) a = 10
#  ) b = 5
#  ) (a/b) == (12/6)
True
#15) a = 10
#  ) b = 5
#  ) c = 12
#  ) d = 6
#  ) (a/b) == (12/6)
True
#16) a = "something"
#  ) b = "some thing"
#  ) a == b
print (a==b)
Flase
#17) a = "word"
#  ) b = "word"
#  ) a == b
print (a==b)
True
#18) a = True
#  ) a == True
True
#19) a = True
#  ) b = False
#  ) a == b
False
#20) a = True
#  ) A = False
#  ) b = False
#  ) A == b
True
