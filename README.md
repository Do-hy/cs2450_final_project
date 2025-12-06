# Multi-Brand Fashion Platform
Final Project – Stage 4 Submission  

---

## Overview

This project implements a Multi-Brand Fashion Platform where independent fashion brands can register, add products, and manage their inventory, while customers can browse available products and place orders. 
An Admin oversees the platform by approving brands and ensuring system integrity.

The project is built in Python using object-oriented design principles and includes modular architecture, a design pattern (Singleton), proper error handling, and full unit testing.

---

## Project Structure
fashion_platform/
│
├── main.py
│
├── src/
│   ├── users.py
│   ├── brands.py
│   ├── products.py
│   ├── orders.py
│   └── platform.py
│
├── tests/
│   ├── test_products.py
│   ├── test_orders.py
│   └── test_platform.py
│
└── docs/ (optional)


---

## ⚙️ How to Run the Program

### 1. Clone the repository

git clone https://github.com/Do-hy/cs2450_final_project.git
cd cs2450_final_project

### 2. Run the main application

python3 main.py


### 3. Example Usage
- The system loads sample data (admin, brand owner, customer, products)
- Customer can view product list
- Customer can enter:
<product_id> <quantity>

- Enter `q` to quit

---

## 🧪 Running Unit Tests

python3 -m unittest


This executes:
- test_products.py  
- test_orders.py  
- test_platform.py  

---

## Features

✔ User roles (Customer, BrandOwner, Admin)  
✔ Brand approval workflow  
✔ Product management  
✔ Order processing  
✔ Singleton design pattern for central platform control  

---

## Technologies Used
- Python 3
- unittest
- Git / GitHub

---

## Author
Southern Utah University  
CS 2450 – Software Engineering Fundamentals
