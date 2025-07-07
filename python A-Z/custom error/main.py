# main.py created inside day 38
# raise custom error(we can create our own error to check evry steps of code & debugging  )
a=(input("enter any value between 2 and 9 or string 'quit': "))
if a=="quit":
    raise ValueError("only this string is acceptable")
elif(int(a)<2 or int(a)>9):
    raise ValueError("value not in range")
else:
    print("ohh! great,value in range")
