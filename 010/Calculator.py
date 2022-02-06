from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  calculate_again = "y"
  first_number = float(input("What's the first number?: "))
  for key in operations:
    print(key)

  while calculate_again == "y":
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))
    function = operations[operation]
    result = function(first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {result}")
    calculate_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    first_number = float(result)
    if calculate_again == "n":
      calculator()

calculator()