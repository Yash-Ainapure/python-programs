# wap that reads a value of n and check the no. is 0 or non zero value
"""val=int(input("enter a number"))
if(val==0):
   print("the no. is zero")
else:
   print("the no. is non zero")"""



# wap that read a no. and check the no. is +ve or -ve
"""val2=int(input("enter a no."))
if(val2<0):
   print("the no. is negative")
else:
   print("the no. is positive")"""   



# wap to check entered character is vowel or consonent
"""val4=input("enter a single character")
val3=val4.lower()
if(val3=='a'or val3=='e'or val3=='i'or val3=='o'or val3=='u'):
   print("the character is a vowel")
else:
   print("the character is a constant")"""   



# wap to check wether a number is even or odd
"""val5=int(input("enter a no."))
if(val5%2==0):
   print("value is even")
else:
   print("value is odd") """ 



# wap to check the year is a leap or not
"""year=int(input("enter the year"))
if(year%400==0 or year%4==0):
   print("it's a leap year")
else:
   print("it is not a leap year")"""



# prg to find the smallest no. among the three
"""lst=[]
for i in range(3):
   lst.append(int(input(f"enter a number {i+1}: ")))

print("min: ",min(lst))
print("max: ",max(lst))"""


# wap to evaluate the student performance as 
""">=80 -->verygood
>=60 --> average
else -->less"""

grade=int(input("enter your grade marks in percentage"))
if grade in range(80,101):
   print("very good")
elif grade in range(60,80):
   print("average")   
else:
   print("less")   