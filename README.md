## CS635 Module 4 Assignment: Real-World Refactoring 

# Group: The Defense
Members: Leo Paredes, Brandon Reynolds

# Abstract
The purpose of this assignment is apply refactoring techniques to a repository to improve quality, maintainability, and performance. 

The repo we have decided to refactor is linked below. 
- https://github.com/caesarmario/online-banking-system-with-python/blob/main/Simple%20Online%20Banking%20System.py

# What does this repository do ?
This repository is a banking system that allows the customer and the bank to perform transactions. It simulates the transaction management system. 

# Original Repository Structure 
```
├─ README.md                  
├─ Simple Online Banking System.py
├─ admin_db.txt
├─ customer_db.txt
└─ transaction_db.txt
```

# Refactored Repository Structure 
```
├─ src/
│  ├─ database.py          
│  ├─ main.py          
│  ├─ models.py             
│  ├─ services.py           
│         
├─ tests/
│  ├─ database_tests.py     
│  ├─ models_tests.py  
│  ├─ service_tests.py     
|
└─ README.md             
```

# Getting Started with Refactored Banking System


