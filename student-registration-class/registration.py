class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number
    
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")


student1 = Student("Nabaggala Racheal", "M23B13/")
student1.display_info()


