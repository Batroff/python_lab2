# БСБО-05-19 Савранский Сергей

users = []
while (user := input("User >> ")) != "":
    users.append(user)

passwords = input("Passwords >> ").split(";")

for user in users:
    user_data = user.split(":")
    if user_data[1] in passwords:
        print(f'To: {user_data[0]}\n'
              f'{user_data[4].split(",")[0]}, ваш пароль слишком простой, смените его.')
