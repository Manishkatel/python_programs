#Writing and appending in a file

name=input("What's your name?")

with open("file1.txt", "a") as file:
  file.write(f"{name}\n")
  
