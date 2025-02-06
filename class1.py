class Student:
  ...

def main():
  student=get_student()
  print(f"{student.name} from {student.house}")

def get_student():
  student= Student()
  name= input("Name: ")
  house= input("House: ")
  Student(name,house)
  return student

if __name__=="__main__":
  main()
  