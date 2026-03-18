#What is function?
# A function is a block of code that runs only when it is called.


#Syntax:
# def function_name():
# code
# Ex:
def greet():
    print("Helllo")
    greet()

# --------------------------------------------------------------------------------------

# Function with parameters
# Used to pass values
def greet(name):
     print(f"hello {name}")
     greet("Tulsi")
     greet("Shreyarth")
     greet("AICW")
# # OR
def greet(name="Student"): #by default parameter
    print(f"hello {name}")
greet()
greet("Shreyarth")
greet("AICW")

# --------------------------------------------------------------------------------------

# Function with return value
# Used when we want to send result back
def add(a , b):
   return a + b
result = add(2 , 3)
print(result)


# Task 1 
# create a function to check if a number is even or odd
# hint: use modulus operator (%)

def check_even_odd(num):
    if num% 2 == 0:
        reteun ="even"
        
    else:
        return"odd"
    check_even_odd(4)
    check_even_odd()
    
#Task 3
#create a function to find the factorial of a number

# hint use a loop or recusion
# input n=5
# output 120 (beacuse 5! * 4 * 3 * 2 * 1=120) 
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))
#or
def factorial (n):
    if n==0 or n ==1:
        return 1
    else: return n* factorial (n-1)
num = int(input("enter a number:"))
result = factorial(num)
print(result)
#Task 4
#create a function to find maximum of three number

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a=float(input("Enter a first number"))  
b=float(input("Enter a second number"))
c=float(input("Enter a third number"))
result = find_max(a,b,c)
print(f"the greatest number is :{result}")
# Output: 10
# use if-else
# input a-5,b-10,c-3

#task 5
#create a function to check if a string palindrome

def is_palindrome(input_str):
    for i in range(len(input_str)//2):
        if input_str[i] != input_str[len(input_str)-i-1]:
            return False
    return True

print(is_palindrome("Tulsi"))

def is_palindrome(s):
    s = s.replace("","").lower()
    return s == s[::1]
input_str = input ("enter a string")
result = is_palindrome(input_str)
if result:
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")


# input_str="madam"
#output = true ("madam " is same as "madam" when reversed) 


#Task 6
#create a function to calculate the area of circle
#hint : area =pi*^r^2 (use 3.14 for pi)
#radius = 5
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

# example
radius = 5
print(area_of_circle(radius))

#or
def area_of_circle(r):
    return 3.14 * r ** 2

radius = float(input("Enter radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle is:{area}")






