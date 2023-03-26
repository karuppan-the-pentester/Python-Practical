class Parent:
    def ovr_method(self):
        print ("This is in Parent Class")
class Child(Parent):
    def ovr_method(self):
        print ("This is in Child Class")
a=Parent()
a.ovr_method()
c = Child()
c.ovr_method()
