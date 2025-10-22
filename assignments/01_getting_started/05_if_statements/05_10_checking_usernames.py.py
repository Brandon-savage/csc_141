# 05_10_checking_usernames.py

current_users = ['brandon', 'autumn', 'bri', 'admin']
new_users = ['brandon', 'autumn', 'bri', 'admin']

for user in new_users:
    if user.lower() in [u.lower() for u in current_users]:
        print(f"Username '{user}' is already taken. Choose a different one.")
    else:
        print(f"Username '{user}' is available.")