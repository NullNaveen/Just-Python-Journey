#we can use optional else in for loop, the else condition will be executed only if the loop successfully finished 
# and if no break statement is encountered//

for i in range(4):
    print(i)
else:
    print("Loop ended")


for i in range(10, 20):
    print(i)
    if  i == 15:
        break
    else:
        (print("This will never be executed"))
else:
    print('done')
print("Outside loop")

print('\nfor loop with else tutorial is over\n')

for i in range(5):  
    print("Value of i =",i)  
    j=0 
    while True:        
        j+=1               
        if (j==5):                        
            break                      
print("Outside the loop")        
# In this example, the outer for loop runs five times. Inside each iteration of the outer loop, a nested while loop runs until the

# Output: Value of i =  0
#          Value of i =  1
#          Value of i =  2
#          Value of i =  3
#          Value of i =  4
# Outside the loop




#In this code we are using a loop to find the factorial of a number.//
#We will use a while loop instead of for loop because it is more suitable in this case.  

def factorial(n): 
    i = 1
    fact = 1
    
    # We continue until n becomes zero or negative
    while (i <= n):  
        fact *= i  
        i += 1  
        
    return fact  

num = int(input("Enter a positive integer: "))
print("The factorial of", num, "is", factorial(num))