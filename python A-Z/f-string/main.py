# main.py created inside day 28
#f-string(we can put variables within string)
letter="my name is {0} and i am from {1}"   #using indexing
name="aman kumar"
country="India"
print(letter.format(name,country))              # (country,name)reverse the order of name and country
print(f"my name is {name} iam from {country}")  # using f-string

# we can retain our f-string as it is by-- print(f"my name is {{name}} iam from {{country}}")

txt="for only {price:.2f} dollars!"  #using 2 decimal places
price=49.99999
print(txt.format(price=49.99999))
print(f"for only {price:.2f} dollars!")    # using f-string
