# For loop with range function
for i in range(0,10):
    print(i)


# For loop in lists
names = ["mostafa", "masume", "zahra"]

for name in names:
    print(name)
    
print(names)

# For loop in dictionaries
students = {'mostafa':17 , 'masume':20, 'zahra':15, 'ali':20}
best_students = []

for key,value in students.items():
    if value == 20:
       best_students.append(key)

print(best_students)



