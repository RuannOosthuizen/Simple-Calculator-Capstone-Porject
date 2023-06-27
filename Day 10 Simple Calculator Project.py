from simple_calculator_art import logo

# Defined functions for calculations:
# Add
def add(n1, n2):
  """The function returns the sum of two added numbers."""
  return n1 + n2

# Subtract
def subtract(n1, n2):
  """The function returns the sum of two subtracted numbers."""
  return n1 - n2

# Multiply
def multiply(n1, n2):
  """The function returns the sum of two multiplied numbers."""
  return n1 * n2

# Devide
def devide(n1, n2):
  """The function returns the sum of two devided numbers."""
  return n1 / n2

# Starting a new fresh calculation
def calculator():
  """The function of the base calculator."""
  print(logo)
  # Code to perform inputs from user and calculations
  num1 = float(input("Please input first number.\n: "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operations_symbol = input("Pick an operation.\n: ")

    num2 = float(input("Please input next number.\n: "))

    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operations_symbol} {num2} = {answer}")

    if input(f"Type 'y' to contiue calculating with {answer} or type 'n' to start a new calcultion.\n: ").lower() == "y":
      num1 = answer

    else:
      should_continue = False
      calculator()

calculator()

# Defined dictionary
operations = {
  "+": add,
  "-": devide,
  "*": multiply,
  "/": devide
}