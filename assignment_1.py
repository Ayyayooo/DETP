# #Q1
# #Int
# a=8
# print('The variable is of type', type(a))
# #Float
# b=3.14
# print('The variable is of type', type(b))
# #String
# c='Pyhton'
# print('The variable is of type', type(c))
# #Boolean
# d=a>b
# print('The variable is of type', type(d))

# #Q2 Printing the full name and its length
# print('Enter your first name: ')
# first_name=input()
# print('Enter your last name: ')
# last_name=input()
# full_name= first_name + ' '+ last_name
# print('your name is', full_name )
# print('length of the name is: ', len(full_name))

#Q3 Currency converter
# usd = 0.96 
# amount = float(input("Enter amount in USD: "))
# print('Amount in Euro =', amount*usd)

#Q4 Arithmetic operations
# print('Enter a number: ')
# num= int(input())
# print('Square of the number is: ', num**2)
# print('Cube of the number is: ', num**3)
# print('square root of the number is: ', num**0.5)

#Q5 Comparison and logical operators
# print('Enter a number')
# num=int(input())
# if num > 0 and num % 2==0:
#     print("Number is positive and even")
# if num>10:
#     print("Number is greater than 10")
# elif num<-10:
#     print("Number is less than -10")
# if num < 0 and num % 5 !=0:
#     print("Number is neither positive nor divisible by 5")

# #Q6 Function to find area of rectangle
# def rectangle_area(l, b):
#     area=l*b
#     return area
# length = int(input("Length of rectangle"))
# breadth = int(input("breadth of rectangle"))
# area_of_rectangle = rectangle_area(length,breadth)
# print("Area of rectangle is:", area_of_rectangle)

# #Q7 Temperature Converter
# def tempareture_converter(f):
#     temp_celcius = (f-32)*(5/9)
#     return temp_celcius
# temp_faren=float(input("Enter the temperature in Farenheit: "))
# c= tempareture_converter(temp_faren)
# print("Temperature in celcius : ", c)

# #Q8 Simple interest
# def simple_interest(p,t,r):
#     i= (p*t*r)/100
#     return i
# principle=input("Principle amount: ")
# time=input("Time: ")
# rate=input("Interest rate: ")
# interest=simple_interest(1000,2,0.5)
# print('Interest: ', interest)

# #Q9 Fibbonocci
# a=0
# b=1
# num=int(input("Enter a number"))
# print(a)
# print(b)
# for i in range(2,num):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# #Q10 Multiplication table of a num
# num=int(input('enter a number'))
# i=1
# while(i<=10):
#     print(num, '*', i, '=',num*i )
#     i+=1
    
# #Q11 iterating to find even numbers
# num_list=[2,4,7,8,9,45,46,68,45,35.67,56.4]
# for i in num_list:
#     if i%2 == 0:
#        print(i)
        
        