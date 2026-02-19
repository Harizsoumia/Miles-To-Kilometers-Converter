**Author:** Soumia Hariz  
**Language:** Python 3

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Usage Example](#usage-example)

---

## 📌 About the Project

This program takes a distance value entered by the user in **miles** and converts it to **kilometers** using the standard algebraic formula:

```
km = miles × 1.60934
```

It is designed to be simple to use, hard to break, and easy to read — making it a great example of clean beginner Python code.

---

## ✅ Features

- **Interactive menu** — the user chooses to convert or exit, making the experience intuitive
- **Full input validation** — handles non-numeric input and negative numbers gracefully without crashing
- **Loops until the user decides to exit** — no need to restart the program for multiple conversions
- **Clean separation of concerns** — each function has one single responsibility
- **Proper indentation and documentation** — every function has a docstring explaining its purpose

---

## ⚙️ How It Works

The program is built around **3 functions** and **2 loops**:

### Functions

| Function             | Role                                               |
| -------------------- | -------------------------------------------------- |
| `miles_to_km(miles)` | Pure calculation — takes miles, returns kilometers |
| `get_miles()`        | Asks the user for input and validates it           |
| `main()`             | Controls the program flow with the menu            |

### The 2 Loops

**Loop 1 — Program Loop** (inside `main()`):  
Keeps the program running after each conversion. The user can convert as many times as they want. Only exits when the user selects **Exit** from the menu.

**Loop 2 — Validation Loop** (inside `get_miles()`):  
Keeps asking for input until the user enters a valid positive number. If the user types letters, symbols, or a negative number, the program shows a warning and asks again instead of crashing.

---

## 🗂️ Project Structure

```
Miles-To-Km-Converter/
│
├── Converter.py       # Main program file
└── README.md          # Project documentation
```

---

## ▶️ How to Run

### Requirements

- Python 3 installed on your machine
- No external libraries needed — uses only built-in Python

---

### 🪟 Windows

**Step 1 — Check Python is installed:**

```bash
python --version
```

If not installed, download it from [python.org](https://www.python.org/downloads/)

**Step 2 — Navigate to the project folder:**

```bash
cd C:\Users\YourName\Desktop\Miles-To-Km-Converter
```

**Step 3 — Run the program:**

```bash
python Converter.py
```

> ⚠️ Run it in the **Terminal** (not the Output panel in VS Code).  
> To open the terminal in VS Code press `` Ctrl + ` ``

---

### 🍎 Mac / Linux

**Step 1 — Check Python is installed:**

```bash
python3 --version
```

If not installed, run `brew install python` (Mac) or `sudo apt install python3` (Linux)

**Step 2 — Navigate to the project folder:**

```bash
cd ~/Desktop/Miles-To-Km-Converter
```

**Step 3 — Run the program:**

```bash
python3 Converter.py
```

---

## 💻 Usage Example

```
========================================
   Miles to Kilometers Converter
========================================

1. Convert
2. Exit
Choose: 1
Enter miles: 10
✅ 10.0 miles = 16.0934 km

1. Convert
2. Exit
Choose: 1
Enter miles: -5
⚠ Cannot be negative. Try again.
Enter miles: hello
⚠ Invalid input. Please enter a numeric value.
Enter miles: 5
✅ 5.0 miles = 8.0467 km

1. Convert
2. Exit
Choose: 2
Goodbye! 👋
```

---

*Made with ❤️ by Soumia Hariz*ad input — keeps asking until the user types a valid number. It's a **validation loop**.
**Loop 1** handles the repeat — keeps the program running after each successful conversion. It's the **program loop**.
proper indentation.
