# 05_08_hello_admin.py

usernames = ['admin', 'brandon', 'autumn']

for user in usernames:
    if user == 'autumn':
        print("Hello , would you like to see a status report?")
    else:
        print(f"Hello {user}, welcome back!")