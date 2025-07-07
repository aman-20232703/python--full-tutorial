# main.py created inside day 49
# file handling(file modes), syntax-- (filename,mode), here mode is default not need to write
# https://www.geeksforgeeks.org/file-mode-in-python/
# ‘r’(read)	Open text file for reading. Raises an I/O error if the file does not exist.
f=open('myfile3.txt','r')
print(f)

# ‘r+’	Open the file for reading and writing. Raises an I/O error if the file does not exist.
text=f.read()
print(text)
f.close()

# ‘w’(write)	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
f=open('myfile.txt','w')
text1=f.write("hello ")
print(text1)
f.close()

# ‘w+’	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.

# ‘a’(append)	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
f=open('myfile.txt','a')
text1=f.write("hello ")
print(text1)
f.close()

with open('myfile.txt','a') as f:
    f.write("hello")   # by using this we need not to close file

# ‘a+’	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
# ‘rb’	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
# ‘rb+’	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
# ‘wb’	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘wb+’	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘ab’	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
# ‘ab+’	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
