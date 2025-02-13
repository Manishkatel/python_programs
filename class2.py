class Student:
  def __init__(self,name,house):
    if not name:
      raise ValueError("Missing name")  #Ican create my own error like ManishKatel
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]:
        raise ValueError("Invalid House")
    self.name=name
    self.house=house

def main():
  student= get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  name= input("Name:")
  house= input("House: ")
  return Student(name,house)

if __name__=="__main__":
  main()

