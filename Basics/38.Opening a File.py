def CreatingASampleFile():
    SampleFile = open('sample file.txt', mode = 'w')
    SampleFile.write('One')
    SampleFile.write('\nTwo')
    SampleFile.write('\nThree')
    SampleFile.close()


import os
if os.path.exists('sample file.txt'):
    print("File successfully created!")
else:
    print("File not found!")

print("Current Working Directory:", os.getcwd()) 

# What is the Current Working Directory (CWD)?
# The Current Working Directory (CWD) is the folder where Python is currently operating. When you create or open a file without specifying a full path, Python saves or looks for it in the CWD.

os.chdir(r'C:\Users\Nike\Documents\Programming\Python\Basics')

print('The New Working Directory:', os.getcwd())

CreatingASampleFile()