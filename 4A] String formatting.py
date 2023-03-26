s1=str(input("Enter first String : "))
s2=str(input("Enter second String : "))
print("First string is : ",s1);
print("Second string is : ",s2);
print("concatenations of two strings :",s1+s2);
print("Substring of given string :",s1[1:4]);
print("String repetition: ",s1*3)
i=0
while i < len(s1):
    letter = s1[i]
    print(letter)
    i = i + 1
