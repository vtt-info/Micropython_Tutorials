# A function without returning a value
# def get_best_students(students):
#     
#     best_students = []
# 
#     for key,value in students.items():
#         if value == 20:
#            best_students.append(key)
# 
#     print(best_students)
# 
# students_class_a = {'mostafa':17 , 'masume':20, 'zahra':15, 'ali':20}
# students_class_b = {'human':18, 'reyhane':19, 'reza':20, 'nazanin':20}
# 
# get_best_students(students_class_a)
# get_best_students(students_class_b)


# A function with returning a value
def get_best_students(students):
    
    best_students = []

    for key,value in students.items():
        if value == 20:
           best_students.append(key)

    return best_students


students_class_a = {'mostafa':17 , 'masume':12, 'zahra':15, 'ali':17}

best_students_of_class_a = get_best_students(students_class_a)
if len(best_students_of_class_a) > 0:
    print(best_students_of_class_a[0])
else:
    print("Not a good class!")
