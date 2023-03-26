class Person(object):
    def get_name(self,name):
        self.name = name
    def get_details(self):
        return self.name
class Student(Person):
    def fill_details(self,name,branch,year):
        self.name = name
        self.branch = branch
        self.year = year

    def get_details(self):
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Year: ",self.year)

class Teacher(Person):
    def fill_details(self,name,branch):
        self.name = name
        self.branch = branch
    def get_details(self):
        print("Name: ",self.name)
        print("Branch: ",self.branch)

person1=Person()
student1=Student()
teacher1=Teacher()
person1.get_name("Yamuna")
student1.fill_details("Karuppasamy","ECE",2)
teacher1.fill_details("Karthik","ECE")
print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
