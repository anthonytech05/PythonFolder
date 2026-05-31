def checkproduct(product_name, product_list):
    if product_name in product_list:
        return product_list.index(product_name) + 1
    return - 1

products = ["Rice", "Beans", "Oil", "Sugar"]

print(checkproduct("Beans", products))
print(checkproduct("Oil", products))
print(checkproduct("Sugar", products))
print(checkproduct("Rice", products))



def findStudent(student_name, list_of_student):
    if student_name in list_of_student:
        return list_of_student.index(student_name) + 1
    return - 1

students = ["Mary", "John", "Anthony", "Bayo"]

print(findStudent("Bayo", students))
print(findStudent("Anthony", students))
print(findStudent("Mary", students))
print(findStudent("John", students))