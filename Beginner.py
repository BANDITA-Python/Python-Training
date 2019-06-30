#Using cmd run program
print("Hello, my first python file")

x = "I will Print this!!"
print(x)

x='test me'
print(x)

#Syntax Error
#x=test me
#print(x)

#Converting the first Char as Upper case, full string UpperCase, Full String lower Case
x="testme"
y="HELP"
print(x.title())
print(x.upper())
print(y.lower())

#Print - String Concatenation
print(x + " "+ y)

#String - Remove Extra space from start, middle and end
s = "  This is sample     Test "
print(f"Before remove Space: " + s)
print(f"After remove Leading Space: " + s.lstrip())
print(f"After remove Trailing Space: " + s.rstrip())
print(f"After remove Both Space: " + s.strip())
print(f"After remove all Space: " + s.replace(" ", ""))

#Numbers - int, float, complex
x = 23.3
y = 123
z = 5+3j
print(type(x))
print(type(y))
print(type(z))
print (x + y)
print (y + z)

