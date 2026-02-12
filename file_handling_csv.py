import csv

try:
    # 1. Create and Write CSV File
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Course"])  # Header
        writer.writerow(["Bhavya", 20, "CSE"])
        writer.writerow(["Rahul", 21, "ECE"])
        writer.writerow(["Anu", 19, "IT"])

    print("CSV file created successfully!\n")

    # 2. Read CSV File
    print("Reading CSV File:")
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except Exception as e:
    print("Error:", e)
