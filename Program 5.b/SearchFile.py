#Develop a python program that could search the text in a file for phone numbers
#(+919900889977) and email addresses (sample@gmail.com)
with open(r'C:\Users\Prathik\Documents\GitHub\21CSL46-PythonLabPrograms-ALL\Program 5.b\text.txt', 'r') as file:          #Enter the file path and the file name
    text = file.read()                      
import re
phone_numbers = re.findall(r'\+91\d{10}', text)
email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
print("Phone numbers found:", phone_numbers)
print("Email addresses found:", email_addresses)