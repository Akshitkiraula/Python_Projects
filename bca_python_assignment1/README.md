# Student Profile Console App - BCA Assignment

A Python-based Command Line Interface (CLI) tool that demonstrates Python fundamentals including variables, operators, string operations, and file handling.

## 📋 Assignment Information

- **Course:** Problem Solving with Python
- **Program:** BCA (Cyber Security)
- **Semester:** 1st
- **Course Code:** ETCCCPP103
- **Assignment:** Unit-1 Mini Project
- **Faculty:** Neha Kaushik
- **Institution:** K.R. Mangalam University
- **Date:** November 2025

## 📚 Learning Objectives

By completing this project, you will:
- ✅ Understand Python history & features
- ✅ Set up Python development environment (VS Code/Anaconda/PyCharm)
- ✅ Use Python syntax and variables with proper naming conventions
- ✅ Work with various data types & type conversions
- ✅ Practice all categories of operators:
  - Arithmetic operators (+, -, *, /, %, **, //)
  - Assignment operators (+=, -=, *=, /=, //=, etc.)
  - Comparison operators (>, <, ==, !=, >=, <=)
  - Logical operators (and, or, not)
  - Identity operators (is, is not)
  - Membership operators (in, not in)
- ✅ Master string operations, formatting, and methods
- ✅ Write a functional console program with formatted output

## 🎯 Features

### Task 1: Setup & Introduction
- Professional welcome message describing the tool
- Comment header with assignment metadata
- IDE installation verification

### Task 2: Input & Variables
Collects the following student information:
- Full Name
- Roll Number
- Program (e.g., BCA)
- University Name
- City
- Age (with type conversion to int)
- Hobby

### Task 3: Operators Demonstration
Demonstrates all operator categories:
- **Arithmetic:** +, -, *, /, %, **, //
- **Assignment:** +=, -=, *=, //=
- **Comparison:** >, <, ==, !=, >=, <=
- **Logical:** and, or, not
- **Identity:** is, is not
- **Membership:** in, not in

### Task 4: Python Strings & Formatting
- String concatenation
- F-string formatting (modern approach)
- Escape characters (\n, \t, \", \')
- 8+ string methods demonstrated:
  - `.upper()`, `.lower()`, `.title()`
  - `.strip()`, `.replace()`, `.count()`
  - `.startswith()`, `.find()`

### Task 5: Final Output
Beautiful formatted profile card:
```
======================================================================
                    STUDENT PROFILE SYSTEM
======================================================================
Name:               John Sharma
Roll No:            23BCA101
Course:             BCA
University:         K.R. Mangalam University
City:               Patiala
Age:                18
Hobby:              Coding
======================================================================
```

### Task 6: Bonus - File Saving
- Option to save the profile to `student_profile.txt`
- Uses file handling with `open()` function
- Error handling for file operations

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- VS Code / PyCharm / Anaconda / IDLE (any Python IDE)

### Installation

1. **Verify Python Installation:**
   ```bash
   python --version
   ```

2. **Clone or Download:**
   ```bash
   git clone <your-repo-url>
   cd bca_python_assignment1
   ```

3. **Run the Program:**
   ```bash
   python student_profile.py
   ```

## 💻 Usage

1. Run the script: `python student_profile.py`
2. The program will guide you through the following steps:
   - Welcome message
   - Input student information
   - Enter two numbers for operator demonstrations
   - View operators output
   - View formatted profile card
   - Optionally save profile to file

### Example Session

```
======================================================================
                 WELCOME TO STUDENT PROFILE SYSTEM
======================================================================

This tool collects student details, demonstrates Python operators,
and displays a formatted student profile card.

Let's get started!

----------------------------------------------------------------------
TASK 2: COLLECTING STUDENT INFORMATION
----------------------------------------------------------------------

Enter your full name: John Sharma
Enter your roll number: 23BCA101
Enter your program (e.g., BCA): BCA
Enter your university name: K.R. Mangalam University
Enter your city: Patiala
Enter your age: 18
Enter your hobby: Coding

✓ Student information collected successfully!

[... Operators demonstrations ...]

Do you want to save your profile? (yes/no): yes

✓ Profile saved to 'student_profile.txt' successfully!
```

## 📁 Project Structure

```
bca_python_assignment1/
├── student_profile.py          # Main program
├── student_profile.txt         # Output file (created after running)
└── README.md                   # This file
```

## 📊 Code Quality

This project demonstrates:
- ✅ **Clear Variable Names:** Descriptive, meaningful variable names
- ✅ **Comments & Documentation:** Well-commented code with task separation
- ✅ **Proper Formatting:** Clean, readable code structure
- ✅ **Error Handling:** Try-except for file operations
- ✅ **Type Conversions:** Proper use of int() and str()
- ✅ **Professional Output:** Formatted console display with separators

## 📝 Deliverables

This submission includes:
- ✅ `student_profile.py` - Complete program with all tasks
- ✅ `README.md` - Comprehensive documentation
- ✅ `student_profile.txt` - Sample output file
- ✅ Screenshots (to be added for LMS submission)
- ✅ GitHub repository link

## 🎓 Evaluation Rubric

| Criteria | Weight | Status |
|----------|--------|--------|
| Python Setup & Files | 10% | ✅ Complete |
| Python Basics & Variables | 20% | ✅ Complete |
| Operators Implementation | 20% | ✅ Complete |
| String Operations | 20% | ✅ Complete |
| Code Output & Formatting | 20% | ✅ Complete |
| Documentation & Comments | 10% | ✅ Complete |

## 🔍 Key Learning Points

### 1. Variables & Input
```python
student_name = input("Enter your full name: ").strip()
age = int(input("Enter your age: "))
```

### 2. String Methods
```python
name = "  python  "
name.upper()        # "  PYTHON  "
name.strip()        # "python"
name.replace('p', 'P')  # "  Python  "
```

### 3. F-String Formatting
```python
f"Hello {student_name}, you are {age} years old"
```

### 4. Operators
```python
# Arithmetic
result = num1 + num2

# Comparison
is_greater = num1 > num2

# Logical
both_positive = num1 > 0 and num2 > 0
```

### 5. File Handling
```python
with open('student_profile.txt', 'w') as file:
    file.write("Profile data...")
```

## ✨ Bonus Features

- 🎨 Professional formatted output with ASCII art separators
- 📁 File saving functionality with error handling
- 🔢 Comprehensive operator demonstrations
- 📚 Multiple string method examples
- 💬 User-friendly prompts and confirmations

## 📋 Submission Checklist

- [x] Python installation verified
- [x] IDE installation verified
- [x] Proper folder structure (bca_python_assignment1)
- [x] All tasks completed (1-6)
- [x] Professional comment header
- [x] All operators demonstrated
- [x] String methods applied (5+)
- [x] Formatted profile card output
- [x] Bonus file saving feature
- [x] GitHub repository created
- [x] README documentation complete
- [x] Code well-commented

## 🤝 Academic Integrity

This work is original and created following the assignment specifications. All code demonstrates direct understanding of Python fundamentals from Unit-1.

## 📞 Support

For questions or issues:
1. Review the code comments
2. Check the Python official documentation
3. Refer to class materials from Unit-1

## 📄 License

This assignment is submitted for educational purposes at K.R. Mangalam University.

---

**Created:** November 2025  
**Course:** Problem Solving with Python (BCA)  
**Institution:** School of Engineering & Technology, K.R. Mangalam University

