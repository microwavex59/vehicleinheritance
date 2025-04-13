#Create a base class called Musician that represents general attributes and behaviors all musicians share:
#Name
#Genre
#Skill level
#Energy level
#Level (for progression)
#Common actions like practice(), rest(), and level_up()
#Use Encapsulation to protect private and protected attributes.
#Use Abstraction by making Musician an abstract 
# class and forcing child classes to implement a perform() method.
#Create subclasses of Musician for:
#Singer
#Guitarist
#Drummer Each should implement its own unique version of the perform() method.
#Use Polymorphism by allowing a function like studio_day()
# to accept any type of musician and run the same set of actions.

class Musician:
    def __init__(self,name, genre):
        self.name=name
        self.genre=genre
        self.skill=1
        self.energy=1
        self.level=1
    def practice(self,hours):
        self.skill=self.skill+(hours*2)
        self.energy-=hours*5
        print(f"{self.name}'s energy is now {self.energy}, their skill is now {self.skill}. They practiced for {hours} hours")
    def rest(self,hours):
        self.energy=self.energy+(hours*2)
        print(f"{self.name} has rested for {hours} hours. Their energy is now {self.energy}")
    def levelUp(self):
        level=level+1
        return level


class Guitarist(Musician):
    def practice(self,hours):
        self.skill=self.skill+(hours*3)
        self.energy-=hours*5
        print(f"{self.name}'s energy is now {self.energy}, their skill is now {self.skill}. They practiced for {hours} hours")
    def rest(self,hours):
        self.energy=self.energy+(hours*6)
        print(f"{self.name} has rested for {hours} hours. Their energy is now {self.energy}")
    

class Drummer(Musician):
    def practice(self,hours):
        self.skill=self.skill+(hours*2)
        self.energy-=hours*10
        print(f"{self.name}'s energy is now {self.energy}, their skill is now {self.skill}. They practiced for {hours} hours")
    def rest(self,hours):
        self.energy=self.energy+(hours*8)
        print(f"{self.name} has rested for {hours} hours. Their energy is now {self.energy}")
    
class Singer(Musician):
    def practice(self,hours):
        self.skill=self.skill+(hours)
        self.energy-=hours*2
        print(f"{self.name}'s energy is now {self.energy}, their skill is now {self.skill}. They practiced for {hours} hours")
    def rest(self,hours):
        self.energy=self.energy+(hours*9)
        print(f"{self.name} has rested for {hours} hours. Their energy is now {self.energy}")
    

if __name__=="__main__":
    musician1=Guitarist("Ethan","Classical")
    musician1.practice(10)
    print(musician1)
    musician3=Musician("Amy","Classical")
    musician3.practice(10)
    print(musician3)
    musician2=Guitarist("Bob","Classical")
    musician2.practice(10)
    print(musician2)
    musician4=Guitarist("Joe","Classical")
    musician4.practice(10)
    musician4.rest(7)
    musician3.rest(7)
    musician2.rest(7)
    musician1.rest(7)
    print(musician4)