# main.py created inside day 89
# request module --> The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.

#pip install request
import requests
from bs4 import BeautifulSoup

#get request
r=requests.get('https://www.google.com/')
print(r.text)

#Post Request
import requests
url = "https://api.example.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json"
}
data = {
    "username": "myusername",
    "password": "mypassword"
}
response = requests.post(url, headers=headers, json=data)
print(response.text)

#bs4 Module- There is another module called BeautifulSoup which is used for web scraping in Python.
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all('a'):
    print(heading.text)