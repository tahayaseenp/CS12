from pickle import *

# dump(object, file_object)
# dump saves data to the file
# Return type is None

# picke.load(file_object)
# load() reads data from the file


def insertRec():  # Write to file
    while 1 == 1:
        rollno = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
    
        # Creating the dictionary
        rec = {'Roll No': rollno, 'Name': name, 'Marks': marks}

        # Writing the dictionary
        f = open("student.dat", 'ab+')
        dump(rec, f)
        f.close()
        ch = input("Would you like to continue? (y/n): ")
        if ch.lower() != 'y':
            break


def readRec():  # Read from file
    f = open("student.dat", "rb")
    while True:
        try:
            rec = load(f)
            print("Roll No: ", rec['Roll No'], end="\t")
            print("Name: ", rec['Name'], end="\t")
            print("Marks: ", rec['Marks'])
        
        except EOFError:
            break

    f.close()


insertRec()
print()
readRec()