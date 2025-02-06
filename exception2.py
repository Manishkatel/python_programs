# Using while True keeps looping untill the user enters a valid integer

while True:
  try:
    x=int(input("What's x?"))
  except ValueError:
    print("x is not an integer")
  else:
    break

print(f"x is {x}")

