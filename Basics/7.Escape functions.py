#Escape sequence characters
#Sequence of characters after  the backslash (\) that represents a special character or an action.

print("Hello\nWorld")     #Newline is represented by \n
                          #In Python, print adds a newline at the end automatically.

print("\tHello\tWorld")   #Tab is represented by \t
                          #Tabs are usually used to align things in output.

print("\\\Backslash",           #Backslash itself is escaped using another backslash.
      "\'Single Quote\'",      
      "\"Double Quote\""       #Both single and double quotes can be escaped using the same quote type.
     )

#Other Escape Sequences:
#\a	Alert (bell)
#\b	Backspace
#\f	Form feed
#\n	New line
#\r	Carriage return
#\t	Horizontal tab
#\v	Vertical tab


print("\aThis is an alert sound.")    #ALert Sound

print("\bThis is a backspace.",end="")  #Backspace

print("\fThis is a formfeed page break.") #Form Feed Page Break

print("\nThis is a new line.",end="")   #New Line

print("\rThis is a carriage return.",end="") #Carriage Return