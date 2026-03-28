# Assignment 3 - Error Identification, Testing and Debugging

This project focuses on identifying and fixing bugs in a Python-based order management system. The goal is to apply debugging strategies, improve code quality, and implement unit and integration testing.

## Project Files

- **BuggyCode.py**  
  Original version of the program containing bugs.

- **BuggyCode_Fixed.py**  
  Updated version with bug fixes applied.

- **test_buggy_code.py**  
  Test file including:
  - Unit tests for total calculation
  - Unit tests for discount validation
  - Integration test for full order workflow

## Features

- Calculate total order price
- Apply discount codes
- Add and remove items from an order
- Display order summary

## Testing Approach

- Multiple test cases were used instead of a single input to improve test coverage.
- Summary tables were added to clearly show expected vs actual results.
- Tests were designed to continue running even if one case fails.
- Integration testing was used to validate the full workflow.

## Bugs Identified

- Incorrect total calculation logic
- Invalid discount codes returning `None` instead of `0`
- Incorrect order total after adding/removing items

## Debugging Strategy

A bottom-up debugging approach was used:
- Test individual functions first
- Then test the full system workflow
- Identify where incorrect values were introduced

## Note

- **BuggyCode.py** is the version that still contains bugs (only syntax errors were fixed so the program can run and show failed test cases).

- **BuggyCode_Fixed.py** is the fully corrected version with all bugs fixed.

- In `test_buggy_code.py`, you can switch between the two by changing the import:

```python
from BuggyCode import Order        # to test buggy version (fail cases)
# from BuggyCode_Fixed import Order  # to test fixed version (pass cases)
