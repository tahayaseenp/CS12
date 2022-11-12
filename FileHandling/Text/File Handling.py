"""
#31/8/22

fobj=open("MY FIRST FILE.TXT")
#returns file object/ file handle/ file pointer
print(fobj.read())#returns string
--------
fobj=open("MY FIRST FILE.TXT")
print(fobj.read(10)) #fobj.read(n)- n chars frm current file pointer, after opening file pointer is always in the first character
print(fobj.read(5))
print(fobj.readline()) 
print(fobj.readline())
--------
fobj=open("MY FIRST FILE.TXT")
print(fobj.read())
print("end of file!")
print(fobj.read(5))
print(fobj.read(10))
#after read the pointer is at the end of the file therefore the codes after will give no output
--------
#output prediction
#1)no value
fobj=open("MY FIRST FILE.TXT")
str1=fobj.read()
str2=fobj.read(10)
print(str2)

#2)run everything and then the remaining is read
fobj=open("MY FIRST FILE.TXT")
str1=fobj.read(10)
str2=fobj.read(5)
str3=fobj.readline()
str4=fobj.read()
print(str4)
---------
filename="MY FIRST FILE.TXT"
fobj=open(filename)
s=fobj.readlines()
# return type is list of strings
print(s)
fobj.flush()
fobj.close()

filename = "MY FIRST FILE.txt"
fobj=open(filename)
s=fobj.read()
letter_count=0
for i in s:
    if i.lower=='o':
        letter_count += 1
print("Letter occurence: ", letter_count)
is_words = 0
if i.lower == 'my':
    is_words += 1

print("No. of words = ", len(s.split()))
print("No. of 'is' = ", is_words)

# CREATE A FILE
# open(filename, access_mode)

6 modes
r   - read (default)
r+  - read and write
w   - write
w+  - write and read
a   - append
a+  - append

fobj=open("MY FIRST FILE.txt")
fobj1=open("NEW TEXT FILE 1.txt", 'w')
fobj2=open("NEW TEXT FILE 2.txt", 'w+')
fobj3=open("NEW TEXT FILE 3.txt", 'a')
fobj4=open("NEW TEXT FILE 4.txt", 'a+')
# fobj5=open("NEW TEXT FILE 5.txt", 'r+' # FileNotFoundError because r and r+ requires file to exist
# fobj6=open("NEW TEXT FILE 6.txt", 'r') # FileNotFoundError because r and r+ requires file to exist

# INSERT INTO FILE
# write(str) or writelines(strs/seq obj)

fobj=open("NEW TEXT FILE 1.txt", 'w+')
fobj.write("My first file using text file handling")
fobj.flush()
fobj.close()
# CAUTION! w AND w+ OVERWRITES THE PREVIOUS CONTENT!!

fobj=open("NEW TEXT FILE 1.txt", 'a')
fobj.write("\nNew line")
fobj.flush()

fobj=open("NEW TEXT FILE 1.txt", 'a')
fobj.write("My first file using text handling\nNow refresh")
fobj.flush()

fobj=open("NEW TEXT FILE 1.txt", 'w')
fobj.writelines(['101', 'Joel John', '99.5'])
fobj.writelines(('\n102', 'Erick James', '59.75'))
fobj.writelines({'\n103':['Nanditha', '89.90']})
fobj.flush()
# seek() and tell() functions
# file_pointer.seek(offset, [, whence])
# offset -> read/write pointer
# whence -> 0 (default) - absolute positioning
#           1 - relative position
#           2 - relative position from end of file (negative offset required) - requires binary file handling
fobj=open("NEW TEXT FILE 1.txt", 'w')
fobj.write("My first file using\ntext file handling\nNow refresh")
fobj.flush()

fobj=open("NEW TEXT FILE 1.txt", 'r')
print(fobj.read(5))
print()
seek=fobj.seek(10)
print(fobj.read())
print(seek)
print(fobj.read(12))
print(fobj.tell())
seek=fobj.seek(0)
print("\n\nAfter seek(0): \n", fobj.read())
fobj.close()

fobj=open("NEW TEXT FILE 1.txt", 'r+b')
fobj.seek(1)
fobj.seek(3,1)
print(fobj.tell())
print(fobj.read())
"""

"""
r  mode - by default, read the file content if the file exists. Otherwise, throws a FileNotFoundError
r+ mode - read/write the file if the file exists, otherwise FileNotFoundError
w  mode - overwrite the file content if the file exists, or create a new file
w+ mode - read/overwrite the file contents if the file exists, or create a new file
a  mode - appends the file content if the file exists, or create a new file
a+ mode - read/append the file content if the file exists, or create a new file
"""

