a = 0
while a<=5:
    print(a)  #the code will execute until the condition becomes false . In this case, it will keep executing as
    a += 1

while a<10:
    print("Nicky")
    a += 1

#infinite loop
b = 1
while  True: #True is always true, so the loop will never stop.
    if b % 2 == 0:
        print(f"{b} is even.")
    else:
        print(f"{b} is odd.")
    b += 1
    if b == 5:   #if statement to break out of infinite loop when b equals 5.
        break


while b<10:
    c=a+b
    d=c-a
    e=d/b
    f="The result of {}+{} is {}, and when we subtract {}, we get {}. The answer is {}"\
      .format(a,b,c,a,d,e)
    print(f)
        
    a+=1
    b+=1

# while a<100:
#     print(a)  
#     b=a+5
#     a += 1
#     print(a)
#     print(b)
#     if b>95:
#         break
#     else:
#         a+=6
# print("Loop ended")



