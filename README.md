# 🔐 Password Strength & Cracking Simulator

A comprehensive, Python-based CLI application that analyzes password entropy and simulates both Dictionary and Brute-Force attacks. 

This project was built to bridge the gap between **Computer Science algorithms**, **Software Testing methodologies**, and **Cybersecurity (AppSec)** principles.

## 🚀 Features

* **Information-Theoretic Entropy Calculation:** Calculates the mathematical strength of a password using the $E = L \times \log_2(R)$ formula.
* **Optimized Dictionary Attack:** Implements an $O(1)$ time-complexity search using Python Hash Tables (`set`) to instantly scan through million-line leaked password files (e.g., `rockyou.txt`).
* **Brute-Force Attack Simulation:** Uses `itertools.product` generators for memory-efficient ($O(1)$ space complexity) exhaustive key searches.
* **Performance Metrics:** Built-in benchmarking to measure the exact time and iterations required to crack a hash/string.

## 🛠️ Tech Stack & Concepts Applied

* **Language:** Python 3.x
* **Core Libraries:** `math`, `time`, `itertools`, `sys`
* **Concepts:** Data Structures (Hash Tables), Time/Space Complexity, Exception Handling, Clean Code, CI/CD readiness.

## 💻 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/password-strength-simulator.git](https://github.com/your-username/password-strength-simulator.git)
2. Unzip the included rockyou.txt.zip file to the root directory of this project.
3. Run the application
   ```bash
   python passwordcheck.py
    
