star_wars_name = input(id_message)

if star_wars_name:
    ship_name = input(id_message)
    if ship_name:
        print(accepted_message % (star_wars_name, ship_name))
    else:
        print("You must enter your ship name to proceed!")
else:
     print("You must enter and ID to proceed!)
print("End of Transmission >>>")   