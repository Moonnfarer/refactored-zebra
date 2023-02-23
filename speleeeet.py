


## battle stage-  lägg till flera attacker i respektive enemyklass. I battle stage läggs alla attacker in i en lista attack.random.choice([attack1(), attack2()])
#Lägg till flera taunts och kör randint bland dessa 


## lägg till speach med koppling till svordom 

## lägg till health, strength och magic reset

## lägg till reducering av strength och magic 





import random
import time 
#time.sleep(1)


#Parent class Hero 
class Hero:
    def __init__(self, name, health, strength, magic, speach): 
        self.name = name 
        self.health = health 
        self.strength = strength 
        self.magic = magic
        self.speach = speach 

    def stats(self): 
        print(f"Your character! \n Name: {self.name} \n Health: {self.health} \n Strength: {self.strength} \n Magic: {self.magic}")

    def melee(self): 
        print("Slap!")
        damage = 10
        return damage 
        

#Warrior   
class Warrior(Hero):
    def __init__(self, name, health, strength, magic, speach): 
        super().__init__(name, health, strength, magic, speach)
    
    def attack(self): 
        print("KAPOOWW!")
        damage = self.strength*1 
        return damage 

    def svordom(self):
        damage = self.speach*1
        return damage
        

#Wizard
class Wizard(Hero):
    def __init__(self, name, health, strength, magic, speach): 
        super().__init__(name, health, strength, magic, speach)
        
    def attack(self): 
        print("AVADA KADABRAAA!")
        damage = self.magic*1 
        return damage 
      
    def svordom(self):
        damage = self.speach*1
        return damage
 


#Parent class Enemy 
class ENEMY:
    def __init__(self, name, health, strength, magic): 
        self.name = name 
        self.health = health 
        self.strength = strength 
        self.magic = magic

    def enemy_stats(self): 
        print(f"Your enemy! \n Name: {self.name} \n Health: {self.health} \n Strength: {self.strength} \n Magic: {self.magic}")

    def melee(self): 
        print("Slap!")
        damage = self.strength/4 
        return damage 

# Enemy classes 
class enemy_warrior(ENEMY): 
    def __init__(self, name, health, strength, magic): 
        super().__init__(name, health, strength, magic)

    def attack(self): 
        print("här får du din lilla fitta!")
        damage = self.strength*1 
        return damage 
  

class enemy_wizard(ENEMY): 
    def __init__(self, name, health, strength, magic): 
        super().__init__(name, health, strength, magic)

    def attack(self): 
        print("smaka på den här!")
        damage = self.magic*1 
        return damage 



#Välj Hero 
def hero_select(): 
    choice = input("Välj class: \n 1. Warrior\n 2. Wizard ")
    if choice == "1": 
        hero_name = input("Namn: ")
        player = Warrior(hero_name, 120, 50, 0, 20) 
        player.stats() 

        return player
    if choice == "2": 
        hero_name = input("Namn: ")
        player = Wizard(hero_name, 100, 15, 50, 20) 
        player.stats() 

        return player


#Random enemy 
def enemy_select(): 
    enemy_random = random.randint(1,3)
    if enemy_random == 1: 
        enemy = enemy_warrior("Vilda Vera", 70, 30, 30) 
        #enemy.enemy_stats()
    
    if enemy_random == 2: 
        enemy = enemy_warrior("Fräcka Frida", 70, 30, 30) 
        #enemy.enemy_stats()

    if enemy_random == 3: 
        enemy = enemy_warrior("Taskiga Thea", 70, 30, 30) 
        #enemy.enemy_stats()
    
    return enemy 
    

## Battle stage /// loot /// Game over


def game_over(): 
    print("GAME OVER")
    restart = input("Restart: Press 1 \nQuit: Press 2")
    if restart == 1: 
        main() 
    elif restart == 2: 
        print("Tack för att du spelade!")
        

def loot():
    global player 
    loot = ["cider", "databasteknik-boken", "stringtrosor"]
    lootchance = random.randint(0,2)
    lootDrop = loot[lootchance]
    if loot == "cider": 
        player.strength += 15
        print("Din strength är nu ", player.strength)
    if loot == "databasteknik-boken": 
        player.magic += 20 
        print("Din magic är nu ", player.magic)
    if loot == "stringtrosor": 
        player.health += 15
        print("Ditt liv är nu ", player.health)
    return lootDrop


player = hero_select() 


def battlestate():
    global player  
    enemy = enemy_select()
    print("en vild ", enemy.name, "står framför dig!")
    print("du har 3 alternativ...")
    
    while enemy.health > 0:
        if player.health <= 0:  
            game_over()
            break 

        choice = input("1. klappa till henne\n2. Säg något taskigt\n3. Spriiiiing!")

        if choice == "1":
            print("Det samlar kraft och slår mot", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                
                enemy.health = enemy.health - player.attack() 
                player.strength -= 10
                player.magic -= 10
                print("du träffade mitt på kinden och hon har nu", enemy.health, " hp " )

                if enemy.health > 0 :
                    player.health = player.health - enemy.attack()
                    print(enemy.name, "blir arg och slår tillbaka och du har", player.health - enemy.attack())

                else: 
                    enemy.health = 70
                    
                    print("Du har besegrat ", enemy.name)
                    print("åååh det droppades något!")
                    lootDrop = loot()
                    print("Du fick en ", lootDrop, "....")
                    break
            else:
                print("Du missa.. nåb..")
                print(enemy.name, " Slår tillbaka hårt")
                player.health = player.health - enemy.attack()
                print("Du har nu ", player.health, "hp kvar")
                #break


        elif choice == "2":                 
            hitchance = random.randint(0,3)

            if hitchance == 0:
                svordomen = "logikfitta!"
                print("Du slänger ur dig '", svordomen, "' i hopp att skada ", enemy.name) 
                print("det var elakt men ", enemy.name, "inser att det stämmer och tar inte illa upp!")
                player.health = player.health - enemy.strength
                print(enemy.name, "blir arg och slår tillbaka och du har", player.health, "HP kvar")
                

            elif hitchance > 0: 
                svordomen = "knarklangare" 
                print("Du slänger ur dig '", svordomen, "' i hopp att skada ", enemy.name) 
                enemy.health = enemy.health - player.svordom() 
                print("Ajajaj det var elakt ", enemy.name, " tar illa upp och har nu ", enemy.health, "HP kvar.")
                
                if enemy.health > 0 :
                    player.health = player.health - enemy.strength
                    print(enemy.name, "blir arg och slår tillbaka och du har", player.health, "HP kvar")


                ### Reset Stats
                else: 
                    if enemy.name == "Vera":
                        enemy.health = 70
                    elif enemy.name == "Thea":
                        enemy.health = 70
                    elif enemy.name == "Frida":
                        enemy.health = 70

                    player = Wizard(player.name, 100, 15, 50) 
                    player = Warrior(player.name, 120, 50, 0) 

                    print("Du har besegrat ", enemy.name)
                    print("åååh det droppades något!")
                    lootDrop = loot()
                    print("Du fick en ", lootDrop, "....")

                    player 
                    break

        elif choice == "3":
            trillchans = random.randint(1,10)
            if trillchans > 7:
                print("Du springer som fan och lyckas komma undan, den här gången....")
                break 
            else:
                player.health = player.health - 20
                print("du trillar och skrapar ditt lilla knä, fyfan va ont! Nu har du bara ", player.health, "HP kvar")




### Lägg till story 


#battlestate() 


def main(): 
    battlestate() 



main() 
