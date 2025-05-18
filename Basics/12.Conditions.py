a=int(input('Enter the number: '))
b=int(input('Enter the number: '))
c=int(input('Enter the number: '))
d=int(input('Enter the number: '))

List= sorted([a, b, c, d])
print("The smallest and largest numbers are {} and {}" .format(List[0], List[-1]))
print(type({}))

if a>b and a>c and a>d:
    print(f"{a} is the largest number")
elif b>a and b>c and b>d:
    print(f"{b} is the largest number")
elif c>a and c>b and c>d:
    print(f"{c} is the largest number")
elif  d>a and d>b and d>c:
     print(f"{d} is the largest number")
else:
    print("There is no largest number")


if a>b:
    LargNum1=a
else:
    LargNum1=b

if c>d:
    LargNum2=c
else:
    LargNum2=d

if LargNum1>LargNum2:
    print('Largest number is', LargNum1)
else:
    print(f"Largest number is {LargNum2}")