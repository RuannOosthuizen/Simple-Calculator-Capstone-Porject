# Simple Calculator

This is a simple calculator program written in Python. It allows users to perform basic mathematical operations such as addition, subtraction, multiplication, and division.

## Usage

To use the calculator, run the `calculator()` function. The program will display a menu with available operations and prompt you to enter numbers for calculation.

```python
calculator()
```

The calculator supports the following operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

## Functions

The program defines several functions for performing calculations:

### `add(n1, n2)`

This function takes two numbers as input and returns their sum.

### `subtract(n1, n2)`

This function takes two numbers as input and returns the result of subtracting the second number from the first number.

### `multiply(n1, n2)`

This function takes two numbers as input and returns their product.

### `divide(n1, n2)`

This function takes two numbers as input and returns the result of dividing the first number by the second number.

### `calculator()`

This is the main function of the calculator. It displays the calculator's logo, prompts the user for input, performs the requested operation, and displays the result. It also allows the user to continue with the result or start a new calculation.

## Dependencies

The program imports the `logo` variable from the `simple_calculator_art` module. Make sure you have the `simple_calculator_art.py` file in the same directory as this script.

## Example

Here's an example of how to use the calculator:

```python
from simple_calculator_art import logo

# Rest of the code...

calculator()
```

## Notes

Please note that the division operation `/` uses the `divide()` function, not the `devide()` function as mentioned in the code comments.

Feel free to modify the code and add more functionality to suit your needs. Enjoy calculating!