def move_player(dir, speed, position):
    if dir == "right":
        position["x"] += speed
    elif dir == "left":
        position["x"] -= speed
    elif dir == "up":
        position["y"] -= speed
    elif dir == "down":
        position["y"] += speed

player = {
    "position":{
        "x":0,
        "y":0
    }
}


move_player("left",10, player["position"])
print(player["position"])

#EXERCISE
#Make a Function
#Run Function
#Make variable that is assigned the actual function
#Call variable to run function

#def the_weather():
#    print("It's Gloomy")
#the_weather()
#the_weather_is_terrible = the_weather
#the_weather_is_terrible()
#
#create a simple dictionary
#item = {
#    "func":myfunction
# }
#item["function"]()

#def thedict():
#    print("This is her dictionary")
#name = {
#    "lisa Marie",
#    "James Madox",
#    "Rita Marley"
#}
#name[theddict]()


