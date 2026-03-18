# what is loop?
# a loop is used to repeat a block of code multiple
# times until a condition is met.

# types of loop in python
# 1. for loop
# used when we know how many times we want to repeat

#syntx 
# for variable in sequence:
# # code

# range() function is commonly used to genrate a sequnce of numbers.

# range come with 3 parameters
# 1.start(inculsive) 
# 2.stop(excluisve)
# 3.step(optional,default is 1)
# range (start, stop-1,step)
#Example :
for i in range (1,6):
    print(i)
# key point :
# 1. range(start,stop) genrates numbers
# 2. loop runs fixed number of times
#-----------------------------------------------------------------------------------------------

#2.while loop
# used when we repeat until a condition becomes false

# syntax:
# while condition:
#    #code

#example:
i = 1
while i <= 5:
    print (i)
    i += 1
# output:
# 1 2 3 4 5

# key points:
# 

#loop control

# 1. break
# stop the loop immediately

# ex:
for i in range (1, 6):
  if i==3:
    break
print(i)

#output:
# 1 2

#2.continue
# skip current itretaion
# for i in range iteration
for i  in range (1,6):
   if i==3:
        continue 
print(i)
    
#output:
# 1 2 4 5

#3. pass
# does nothing (place holder)
# for i in range (5): 
# pass
#----------------------------------------------------------------------------------------------


#Task 1
# print number from 1 to 10 using a for loop.
for i in range (1,11):
 print(i)
    
#Task 2
# print even number from 1 to 20.
# output :
# 2 4 6 8 10 12 14 16 18 20
 
for i in range (1, 21):
 if i % 2 == 0:
    print (i, end=" ")

  # or
for i in range (2, 21, 2):
  print (i, end=' ')  
      
#Task 3
#print odd number 1 to 15
for i in range (1, 16, 2):
 print(i, end=' ')   
   
# Task 4
# print each character of string.

text = "python"

for ch in text:
    print(ch)
# Task 5
# print all items in the list

data =["data","science","AI"]
for item in data:
    print(item)
# output
# data 
# science 
# AI

# Task 6
# find the sum of numbers 1 to 10
sum = 0
for i in range(1, 11):
   sum +=  i
print(sum)
# output
# 55

# task 7
# print multiplication table of 5.
for i in range (1,11):
    print("5 *",i,"=",5 * i)
    # f = format string allows embeddings expression 
    # inside string literals using{}
# Task 8
# count how many vowels are in a string
text = "Hello  World"
count = 0
for ch in text:
    if ch.lower() in "aeiouAEIOU":
        count += 1

print("number of vowel:",count)

#Task 9
# print numbers in reverse order from 10 to 1
for i in range (10,0,-1):
    print(i)
# Task 10
# print square of numbers from 1 to 5.
for i in range(1, 6):
    print(i ** 2)
# output 
# 1 
# 4
# 9
# 10
