import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["db"]

PyTech = db["Pytech"]

student1 = { "Student ID":"1007","First Name":"Thorin","Last Name":"Oakenshield"}
student2 = { "Student ID":"1008","First Name":"Bilbo","Last Name":"Baggins"}
student3 = { "Student ID":"1009","First Name":"Frodo","Last Name":"Baggins"}

students = [student1,student2,student3]
def insert():
    print("-- INSERT STATEMENTS --")
    for student in students:
        student_id = PyTech.insert_one(student).inserted_id
        print(f"Inserted student record {student['First Name']} {student['Last Name']} into the students collection with document_id {student_id}")
    print("\n")    
    print("End of program, press any key to exit...")

insert()



