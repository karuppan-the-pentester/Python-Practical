class MyClass: # defining class
__a = 0;
def sum(self, increment):
 self.__a += increment
 print (self.__a)
b=MyClass()
print(b.sum(2))
print(b.sum(5))
