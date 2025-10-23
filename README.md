# cs635-module-4-assignment
Module 4 Assignment

Referenced Repo Github Link:
https://github.com/caesarmario/online-banking-system-with-python/blob/main/Simple%20Online%20Banking%20System.py

Old code and README are located in src_old for reference.
Bew code is located in src and test suites are locaed in tests.

How to test project:
# Make sure that pytest is installed
python -m pip install pytest

# Run the tests
python -m pytest -q ./tests/database_tests.py
python -m pytest -q ./tests/models_tests.py
python -m pytest -q ./tests/services_tests.py