from college import *
class student():
    def Student(self):
        self.number=int(input("Enter Student Number :"))
        self.name=input("Enter Student Name :")
        self.course=input("Enter Student Course Name :")
    def get_Student(self):
        print("Student Details")
        print("Student Number",self.number)
        print("Student Name",self.name)
        print("Student Course",self.course)