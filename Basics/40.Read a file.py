with open(r'C:\Users\Nike\Documents\Programming\Python\Basics\sample file.txt','r') as file:
    print(file.read())
    print('--------------------')
    file.seek(0)
    print(file.read(2))
    print(file.read(3))
    print('--------------------')
    file.seek(0)
    print(file.readline())
    print('--------------------')
    file.seek(0)
    print(file.readlines())
    print('--------------------')
    file.seek(0)
    for x in file:
        print(x)
    
    
    