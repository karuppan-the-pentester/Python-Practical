class Student:
 'student details'
 def fill_details(self,name,branch,year):
 self.name = name
 self.branch = branch
 self.year = year
 print("A Student detail object is created")
 def print_details(self):
 print("Name ",self.name)
 print("Branch: ",self.branch)
 print("Year: ",self.year)
s1 = Student()
s2 = Student()
s1.fill_details('Reka','ECE',2020)
s2.fill_details('Karthick','ECE','2020')
s1.print_details()
s2.print_details()
