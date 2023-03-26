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

Karuppan = Student()
Karthik = Student()
Karuppan.fill_details('Karuppasamy K','ECE',2020)
Karthik.fill_details('Karthik Raja K','ECE','2020')
Karuppan.print_details()
Karthik.print_details()
