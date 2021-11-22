import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["db"]

Pytech = db["Pytech"]


def find():
    docs = db.Pytech.find({})
    print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
    for doc in docs:
        print(f"Student ID: {doc['Student ID']}\nFirst Name: {doc['First Name']}\nLast Name: {doc['Last Name']}\n")


def find_one():
    print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
    student = Pytech.find_one({"Student ID":"1007"})
    print(f"Student ID: {student['Student ID']}\nFirst Name: {student['First Name']}\nLast Name: {student['Last Name']}\n")




def main():
    find()
    find_one()
    print("End of program, press any key to exit...")


if __name__ == "__main__":
    main()

    