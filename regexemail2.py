import re

name=input("What's your name?").strip()             # *=gap does not matter
matches= re.search(r"^(.+), *(.+)$",name)
if matches:
  name=matches.group(2)+""+matches.group(1)
print(f"Hello, {name}")

