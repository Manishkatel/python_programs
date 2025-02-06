names=[]

with open("file1.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):
  print(f"hello,{name}")
  
  