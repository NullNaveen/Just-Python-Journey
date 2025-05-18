MyList = ["Shiva", 'chinnasamy', 'Selvam', "sowmya", "David"]

# for name in MyList:
#     if name.startswith("s") or name.startswith("S"):
#         print(f'Dear {name},\n\tHow are you doing?')

for name in MyList:
    if name.capitalize().startswith("S"):
        print(f'Dear {name},\n\tHow are you doing?')