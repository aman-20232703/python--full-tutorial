# main.py created inside day 51
# seek() & tell()
with open('myfile3.txt','r') as f:
    print(type(f))
    
    f.seek(10) # allow you to move the current position within a file to specific position (move to the 10th byte in the file)
    data=f.read(8)
    print(data)
    
    print(f.tell())  # function return the current position within the file or tell which position we seek
    
with open('myfile3.txt','w') as f:
    f.write("hello world")
    f.truncate(4)    # help to read and write file after truncate

with open('myfile3.txt','r') as f:
    print(f.read())
