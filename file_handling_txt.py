# TXT File Handling in Python

try:
    # 1. Create and Write to a Text File
    file = open("student.txt", "w")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.close()
    print("Data written successfully!\n")

    # 2. Read File Contents
    file = open("student.txt", "r")
    print("Reading File:")
    print(file.read())
    file.close()

    # 3. Append Data
    file = open("student.txt", "a")
    course = input("Enter your course: ")
    file.write("Course: " + course + "\n")
    file.close()
    print("\nCourse appended successfully!\n")

    # 4. Read Again After Append
    file = open("student.txt", "r")
    print("Updated File Content:")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("Error occurred:", e)
