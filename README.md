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

# Getting Started with the Refactored Banking System
To use this banking system, run 'main.py' under the 'src' folder by using the command at the top level: python -m src.main
- To start, use option 3 to create new admin as the first user and then afterwards log in as admin with option 1. From there on you can add customers and more.

# How To Run Tests 
The refactored repository uses Pytest for unit testing. There are a total of 9 tests between database tests, models tests, and service tests. All tests can be found under the "tests" folder in the repository. 

To use Pytest to run all the tests follow the instructions below:
- At the root of the repository enter the command in terminal: python -m pip install pytest
- To run database tests, enter the command: python -m pytest -q ./tests/database_tests.py
- To run models tests, enter the command: python -m pytest -q ./tests/models_tests.py
- To run services tests, enter the command: python -m pytest -q ./tests/services_tests.py