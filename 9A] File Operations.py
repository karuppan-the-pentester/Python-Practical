f=open("file1.txt")
print(f.read())
f1=open("file2.txt",'w')
f1.write('God is Great \n')
f1.write('God is love \n')
f1.write('God is omnipresent \n')
f1.close()
import os
os.rename("file2.txt","file3.txt")
