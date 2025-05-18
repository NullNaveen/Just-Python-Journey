a=int(input('Enter the number: '))
b=int(input('Enter the number: '))
c=int(input('Enter the number: '))
d=int(input('Enter the number: '))

if a>b and a>c and a>d : 
    print ("{}, Your number is an Amstrong number".format (a))
elif b>a and b>c and b>d:
    print ("{}, Your number is an Amstrong number".format (b))
else: 
    n = a
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(n // digit))
        temp //= 10
    if sum == n:
        print ("{} ,Your number is an Armstrong number".format(n))
    else:
        print ("{} ,Your number is not an Armstrong number".format(n))


if a>b and a<c:
    print ("{} is between {} and {}".format (a, b ,c))
elif b>a and b<c:
    print ("{} is between {} and {}". format (b, a, c))


if a>b and a>c and a>d:
    print ("{}, {}, and {} are the three largest numbers". format (a, b, c))
elif b>a and b>c and b>d:
    print ("{} is the largest number. The other three numbers are {} and {}" .format (b, a, c))


if a>b:
   if c>d:
       print(f"{c} is in between {a} and {d}")
   else:
        print(f"{d} is  in between {a} and {c}")
elif b>a:
      if d>c:
          print(f"{d} is in between {b} and {c}")
      else:
           print(f"{c} is in between {b} and {d}")  #</s>* Copyright (C) 2013-2014 Canonical Ltd