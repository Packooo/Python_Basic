current_users = ['john', 'jane', 'doe', 'smith', 'james']
new_users = ['john', 'jane', 'tyson', 'sarah', 'giant']


for user in new_users:
    if user in current_users:
        print(f"Sorry, the username '{user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")
    

##make comparation in case insensitive manner
current_users = ['JOHN', 'jane', 'doe', 'smith', 'james']
new_users = ['john', 'JANE', 'tyson', 'sarah', 'giant']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")
