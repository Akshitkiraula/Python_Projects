# ---------------------------------------------------------------
# Name: Akshit kirula
# Roll No: 2501660011
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: <DATE>
# ---------------------------------------------------------------

# Welcome Message (Task-1)
print("==============================================")
print("     WELCOME TO THE STUDENT PROFILE SYSTEM    ")
print("==============================================\n")


# ---------------------------------------------------------------
# TASK 2: INPUT & VARIABLES
# ---------------------------------------------------------------

name = input("Enter your full name: ")
roll_no = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))      # type conversion
hobby = input("Enter your hobby: ")

print("\n✅ Details collected successfully!\n")


# ---------------------------------------------------------------
# TASK 3: OPERATORS DEMONSTRATION
# ---------------------------------------------------------------

print("\n========= OPERATOR DEMONSTRATION =========")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Arithmetic Operators ---")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}")

print("\n--- Assignment Operators ---")
a = num1
a += 5
print(f"a = num1 → a += 5 → {a}")
a -= 2
print(f"a -= 2 → {a}")

print("\n--- Comparison Operators ---")
print(f"{num1} > {num2} → {num1 > num2}")
print(f"{num1} < {num2} → {num1 < num2}")
print(f"{num1} == {num2} → {num1 == num2}")

print("\n--- Logical Operators ---")
print(f"num1 > 0 and num2 > 0 → {num1 > 0 and num2 > 0}")
print(f"num1 > 0 or num2 < 0 → {num1 > 0 or num2 < 0}")
print(f"not(num1 < num2) → {not(num1 < num2)}")

print("\n--- Identity Operators ---")
print(f"num1 is num2 → {num1 is num2}")
print(f"num1 is not num2 → {num1 is not num2}")

print("\n--- Membership Operators ---")
sample_text = "student profile system"
print(f"'student' in '{sample_text}' → {'student' in sample_text}")
print(f"'python' not in '{sample_text}' → {'python' not in sample_text}")


# ---------------------------------------------------------------
# TASK 4: STRING OPERATIONS & FORMATTING
# ---------------------------------------------------------------

print("\n========= STRING OPERATIONS =========")
print("Uppercase Name:", name.upper())
print("Lowercase City:", city.lower())
print("Title Case University:", university.title())
print("Hobby with spaces removed:", hobby.strip())
print("Replace spaces in name with _ :", name.replace(" ", "_"))
print("Count of 'a' in your name:", name.count("a"))

# Escape characters demonstration
print("\nEscape Characters:")
print("Name:\t", name)
print("City:\t", city)
print("University:\t", university, "\n")


# ---------------------------------------------------------------
# TASK 5: FINAL PROFILE CARD
# ---------------------------------------------------------------

print("\n----------------------------------------")
print("\t   STUDENT PROFILE SYSTEM")
print("----------------------------------------")

print(f"Name:\t\t{name}")
print(f"Roll No:\t{roll_no}")
print(f"Course:\t\t{program}")
print(f"University:\t{university}")
print(f"City:\t\t{city}")
print(f"Age:\t\t{age}")
print(f"Hobby:\t\t{hobby}")

print("----------------------------------------")
print("Welcome to Python Programming!")
print("----------------------------------------\n")


# ---------------------------------------------------------------
# TASK 6: BONUS — SAVE TO TEXT FILE
# ---------------------------------------------------------------

save_choice = input("Do you want to save your profile? (yes/no): ").lower()

if save_choice == "yes":
    with open("student_profile.txt", "w") as f:
        f.write("STUDENT PROFILE\n")
        f.write("----------------------------------\n")
        f.write(f"Name: {name}\n")
        f.write(f"Roll No: {roll_no}\n")
        f.write(f"Course: {program}\n")
        f.write(f"University: {university}\n")
        f.write(f"City: {city}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Hobby: {hobby}\n")
    print("\n✅ Profile saved to student_profile.txt")
else:
    print("\nProfile not saved.")

print("\n🎉 THANK YOU FOR USING THE STUDENT PROFILE SYSTEM!")
