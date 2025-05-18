# def fibonacci_sequence(limit):
#     # Starting values for the Fibonacci sequence
#     fib_sequence = [0, 1]
    
#     # Generate Fibonacci numbers up to the given limit
#     while fib_sequence[-1] + fib_sequence[-2] <= limit:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
#     return fib_sequence

# # Example usage
# limit = 100  # Define the limit up to which the Fibonacci sequence should be generated
# fib_sequence = fibonacci_sequence(limit)


fib_sequence = [0, 1]
while True:
    if (fib_sequence[-1] + fib_sequence[-2])>1000000:
        break
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(fib_sequence)