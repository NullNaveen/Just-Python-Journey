def factorial(n):
    if n==0 or n==1: #base condition, if there is no base condition, then the recursion will excute infinetely
        return 1
    return n * factorial(n-1)
a=int(input('Enter the number: '))
print(factorial(a))

print('--------------------------------')

#chatgpt version with a user input value
def factorial():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial()
if result is not None:
    print("Factorial:", result)

#recursion with a loop from blackbox

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

num = 5
print("Factorial of", num, "is", factorial(num))

#The iterative approach is more efficient than recursion for factorials because it avoids the overhead of multiple function calls and uses a simple loop to calculate the factorial.
