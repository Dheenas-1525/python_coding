# def students(name, rollno, batch, year):
#         d = {"name":name,
#              "rollno":rollno,
#              "batch":batch,
#              "year":year
#              }
#         print("the result is :  {}".format(d))
#         return d
# name = input("enter name : ")
# rollno = int(input("enter the rollno : "))
# batch = int(input("enter the batch : "))
# year = int(input("enter year of joining : "))

# result1 = (name, rollno, batch, year)
# for i in result1(10):
# 	print(students(name, rollno, batch, year))
def students(name, rollno, batch, year):
    d = {
        "name": name,
        "rollno": rollno,
        "batch": batch,
        "year": year
    }
    print("The result is: {}".format(d))
    return d
all_students = []
# Collect multiple student entries
for i in range(2):  # 10 students
    print(f"\nEnter details for student {i+1}:")
    name = input("Enter name: ")
    rollno = int(input("Enter the rollno: "))
    batch = int(input("Enter the batch: "))
    year = int(input("Enter year of joining: "))
    
    result = students(name, rollno, batch, year)
    all_students.append(result)
print("\n all students data")
print("=============================================================")


for students in all_students:
        print(students)




print("==============================================================y")

