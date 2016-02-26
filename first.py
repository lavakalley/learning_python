import math

mystring = 'Hi Person How are you?'
for i in mystring:
    print(i)

print ("Print every number for 1 to 100")
for i in range(1 , 101):
    print (i)

print ("***********************************")
print ("Print every power of 2 from 1-50")
for i in range(10):
    print (i*i)
print ("***********************************")
num1=int(input("first number is ? "))
num2=int(input("Second number is ? "))

greater = 0
if num1>num2:
    greater=num1
elif num2>num1:
    greater=num2

print(greater ," is greater")
print ("***********************************")
print ("find the area and circumference of circle: ")
radius=int(input("What is the redius of circle ? "))
area= math.pi * math.pow(radius,2)
print ("Your area is -> ",area)
circumference = 2*radius
print ("Your Circumference is -> ",circumference)
    
print ("***********************************")
result = 0
print("Simple calculator")
oper = input("What would you like to do(add,subtract,divide, or multiply: ")

num1 = int(input("What is your first number ?"))
num2 = int(input("What is your second number ?"))
if oper == "add":
    result = num1+num2
elif oper == "subtract":
    result = num1-num2
elif oper == "divide":
    result = num1/num2
elif oper == "multiply":
    result = num1*num2
    
print("result =",result)









    




