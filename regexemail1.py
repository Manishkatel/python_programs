#For email malan@harvard.edu   and malan@cs50.harvard.edu

import re

email=input("Enter your email address: ")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
  print("Valid email address")
else:
  print("Invalid email address")


