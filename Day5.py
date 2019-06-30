#For loop Using List
students = ['Ram','lak','siv','anu']
for stud in students:
	print(stud)

for stud in students:
	print(f"{stud.title()}, is python certified")
print("All the best")



#Numeric List Range
num=list(range(1,5))
print("Print Range 1 to 5:")
print(num)

#List Square
squares=[]
print("Print square of Range 1 to 16")
for val in range(1,16):
	square=val**2
	squares.append(square)
print(squares)