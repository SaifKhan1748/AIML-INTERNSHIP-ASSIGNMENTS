'''
Assignment_01 - 7th Feb 2026
Create a strong code for password authentication using python. 
'''

correct_username = "admin"
correct_password = "Strong@123"


username = input("Enter username: ")
password = input("Enter password: ")


if username == correct_username and password == correct_password:
    print("✅ Login Successful! Welcome.")
elif username != correct_username and password == correct_password:
    print("❌ Wrong username.")
elif username == correct_username and password != correct_password:
    print("❌ Wrong password.")
else:
    print("❌ Username and password both are incorrect.")