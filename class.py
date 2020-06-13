#class Player(): 
#
#    def __init__(self):
#        print("I have started")
#
#    def move(self, dir, speed, position):
#        print(self)
#        if dir == "right":
#            position["x"] += speed
#        elif dir == "left":
#            position["x"] -= speed
#        elif dir == "up":
#            position["y"] -= speed
#        elif dir == "down":
#            position["y"] += speed
#
#player1 = Player ()
#player2 = Player ()
#
#position = {"x":0, "y":10}
#
#player1.move("left",10, position)
#print(position)
#
#player2.move("left",10, position)
#print(position)




#print("\n")
#
#class Player(): 
#
#    def __init__(self):
#        print("I have started")
#        self.speed = 10
#        self.position = {
#            "x:":0,
#            "y:":0
#        }
#        self.name = name
#
#    def move(self, dir):
#        if dir == "right":
#           self.position["x"] += self.speed
#        elif dir == "left":
#            self.position["x"] -= self.speed
#        elif dir == "up":
#            self.position["y"] -= self.speed
#        elif dir == "down":
#            self.position["y"] += self.speed
#
#player1 = Player ("Amy")
#print(player1.position)
#player1.move("left")
#print(player1.position)
#player1.speed = 100
#print(player1.position)
#player1.move("up")
#print(player1.position)
#
#
#
#player2 = Player ("Carlos")
#player2.move("left")
#print(player2.position)
#print(player1.position)
#print(player2.position)
#

print("\n")

class Character():
    def __init__(self, name, position, speed=10, health=100, attack_power=5):
         self.name = name
         self.position = position
         self.health = health
         self.speed = speed
         self.attack_power = attack_power
         self.position = position
         #self.position{      #this threw out an error channged to self.position = position             
          #  "x":0,
           # "y":0
        #}
    def attack(self):
        return self.attack_power

    def move(self, dir):
        if dir == "right":
            self.position["x"] += self.speed
        elif dir == "left":
            self.position["x"] -= self.speed
        elif dir == "up":
            self.position["y"] -= self.speed
        elif dir == "down":
            self.position["y"] += self.speed
class Player(Character):                  #Subclass One.  Player inherits the attributes of Characters
    def heal(self):
        self.health += 25

class Enemy(Character):
    def __init__(self, name, position):
            super().__init__(name, position)
            self.health = 50
            self.speed =4
        #print("This is doing something")
        #self.name = name
        #self.health = 50
        #self.speed = 4
        #self.position = position

def roll(self):
#self.position["x"] -=25                     #Second subclass.  Also with all the attributes of Character + ability to roll
    def roll(self):
        self.position["x"] -= 25

enemy1 = Enemy("Bad Guy", {"x":0, "y":100})
player1 = Player("Mimz", {"x":10, "y":200})
print(player1.position)
player1.heal()
print(player1.health)
enemy1.roll()
print(enemy1.position)
print(enemy1.attack())
print(enemy1.health)
#print(enemy1.speed)

