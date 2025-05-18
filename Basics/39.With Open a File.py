with open(r'C:\Users\Nike\Documents\Programming\Python\Basics\sample file.txt','r') as file:
    print(file.read())

with open(r'C:\Users\Nike\Documents\Programming\Python\Basics\sample file.txt','r') as file:
    for i in file:
        print(i)

try:
    with open(r'sample_file.txt','r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(f"File not found: {e}")
    print('Error:', e)

with open(r'C:\Users\Nike\Documents\Programming\Python\Basics\sample_filu.txt', mode='w') as SampleFile:
    SampleFile.write('One\nTwo\nThree\n')