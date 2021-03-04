#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ("WELCOME TO MY CALCULATOR")
print ("-------")
print ("PLEASE ENTER TWO NUMBERS WHEN PROMPTED TO DO SO")

number1 = int(input("What is the first number? "))
number2 = int(input("What is the second number? "))

print ("Choose from the following list\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")
result=0
whattodo = input("Please enter your choice : ")

if whattodo == '1':
    result=number1+number2

elif whattodo == '2':
    result = (number1-number2)

elif whattodo=='3':
    result = (number1*number2)

elif whattodo=='4':
    result = (number1/number2)
    
else:
    result = print ("CHOOSE BETWEEN 1-4")
    
print(result)

