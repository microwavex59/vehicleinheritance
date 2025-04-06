class movie:
    def __init__(self,name,length):
        self.name=name
        self.length=length
    def __add__(self,other):
        return other.length + self.length
movie1=movie("Cinderella",76)
movie2=movie("Snow White",83)
totaltime=movie1+movie2        
print(totaltime)