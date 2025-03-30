class animal():
    def __init__(self, name,species):
        self.name=name
        self.species=species
    def animalnoise(self):
        print("Generic animal sound")
class dog(animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed
    def dogmsg(self):
        print("Dog is chasing ball")
class cat(animal):
    def __init__(self, name, species, color ):
        super().__init__(name,species)
        self.color=color
    def catmsg(self):
        ("Cat is scratching furniture")
class bird(animal):
    def __init__(self,name, species, wingspan):
        super().__init__(name,species)
        self.wingspan=wingspan
    def birdmsg(self):
        print("bird is flying")

namebird=bird("Eagle","Bird","15 CM")
namecat=cat("Persian","cat","red")
nameanimal=animal("animal","living")
namedog=dog("dog","canine","german shepherd")


if __name__=="__main__":
    namebird.birdmsg()
    namecat.catmsg()
    namedog.dogmsg()
    nameanimal.animalnoise()
