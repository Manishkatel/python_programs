import csv

name=input("What's your name?")
home=input("What's your home?")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name","house"])
  writer.writerow({"name":name,"house":home})