# main.py created inside day 50
# read and write line using readlines()-Python readlines() is used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then split it into separate lines.
#  writelines()-
f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
    print(line)
    
f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of student {i} in science is {m1}")
    print(f"marks of student {i} in english is {m2}")
    print(f"marks of student {i} in mathematics is {m3}")
    print(line)
    
f=open('myfile2.txt','w')
line=['line 1\n','line 2\n','line 3\n']
f.writelines(line)
f.close()