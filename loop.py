# # # Basic - Print all integers from 0 to 150.

# # for i in range(0,151):
# #     print(i)

# # # Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# # for i in range(5,1000,5):
# #     print(i)

# # # Print integers 1 to 100. 
# # # If divisible by 5, print "Coding". 
# # # If divisible by 10, print "Coding Dojo".

# # for i in range(0,101):
# #     if i%10 == 0:
# #         print('Coding Dojo')
# #     elif i%5 == 0:
# #         print('Coding Dojo')
# #     else:
# #         print(i)


# # #Add odd integers from 0 to 500,000, and print the final sum.

# # # what i coded
# # for number in range(0,500,000+1):
# #     if(number % 1 !=0):
# #         print("{0}".format(number))

# # solution
# sum = 0 
# for i in range(1,500001,2):
#     sum +=i 
# print(sum)


# # Countdown by Fours 
# # Print positive numbers starting at 2018, counting down by fours.

# # What I coded 
# for number in range(0,2018):
#     if number % 2 !=0:
#         print("{0}".format(number))

# # Solution 
# for i in range(2018,0,-4):
#     print(i)



#Set three variables: 
# lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


# Solution  

low = 2
high = 9 
mult = 3 

for  i in range(low,high +1):
    if i % mult == 0:
        print(i)