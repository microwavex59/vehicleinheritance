#operator overloading:
"""
class books:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __add__(self,other):
        return other.pages + self.pages
book1=books("War and Peace",1000)
book2=books("Anna Karenina",750)
totalpages=book1+book2        
print(totalpages)"
"""""
#method overloading
class calculator:
    def add(self,a,b=0,c=0):
        return a + b + c
    
calculator1=calculator()
print(calculator1.add(4))
print(calculator1.add(5,4))
print(calculator1.add(4 ,8,6))
