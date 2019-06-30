#List - Index 0,1,2,3,4 - Order starts with index 0
bicycles = ['hero','xyz','abc','def','pqr']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

#Assign a new Value for Index 1
bicycles[1]='Alpha'
print(bicycles)

#List - Append an item at end
bicycles.append('Beta')
print(bicycles)

# Insert an Item at Index 2
bicycles.insert(2,'Gamma')
print(bicycles)

# Delete Item
bicycles.pop()
print(f"After Delete Last Item:")
print(bicycles)
bicycles.pop(2)
print(f"After Delete Item from Index 2:")
print(bicycles)

#Sorting
bicycles.sort()
print(f"After Sorting:")
print(bicycles)