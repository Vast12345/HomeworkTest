def Addition(a, b):
  adding = a + b
  return adding

def Subtraction(a, b):
  subtracting = a - b
  return subtracting

def Multiplication(a, b):
  multiplying = a * b
  return multiplying

def Division(a, b):
  dividing = a / b
  return dividing 

while True:
  print("Which operation would you like to choose:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Stop")

  operation = input()

  if operation == '1':
    addNumber = int(input("Choose which number you would like to add "))
    addNumber2 = int(input("Choose the second number you would like to add "))

    addResult = Addition(addNumber, addNumber2)
    print(addResult)
  elif operation == '2':
    subNumber = int(input("Choose which number you would like to subtract "))
    subNumber2 = int(input("Choose the second number you would like to subtract "))

    subResult = Subtraction(subNumber, subNumber2)
    print(subResult)
  elif operation == '3':
    multNumber = int(input("Choose which number you would like to multiply "))
    multNumber2 = int(input("Choose the second number you would like to multiply "))

    multResult = Multiplication(multNumber, multNumber2)
    print(multResult)
  elif operation == '4':
    divNumber = int(input("Choose which number you would like to divide "))
    divNumber2 = int(input("Choose the second number you would like to divide "))

    divResult = Division(divNumber, divNumber2)
    print(divResult)
  elif operation == '5':
    break
  else:
    print("Invalid Choice.")



  