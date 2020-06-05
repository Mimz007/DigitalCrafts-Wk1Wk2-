lotus_name = input(id_message)
name_length = len(lotus_name)

if lotus_name < 6:
    print('Too Short.')
elif lotus_name > 12:
    print('Too Long')

confirmation_message = "Confirm your password!"
confirmed_password = input(confirmation_message)

if confirmed_password == password:
    print("Success! Your passwords match")

if confirmed_password != password:
    print("Oops! Your password does not match")
