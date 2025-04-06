class Book:
    def __init__(self,title, author):
        self.title=title
        self.author=author
        self.__availablility=True
   
    def  isAvailable(self):
        return self.__availabity
    def borrow(self):
        if self.__availablility:
            self.__availability=False
            return True
        else:
            return False
    def returnbook(self):
        self.__availability=True
    def __str__(self):
        status="avalible" if self.__availability else "checked out"
        return (f"{self.title} by {self.author}, {status}")
class User:
    def __init__(self,name):
        self.name=name
        self.borrowedbooks=[]
    def borrowbook(self,book):
        if book.borrow():
            self.borrowedbooks.append(book)
            print(f"{self.name} has borrowed {book.title}")
        else:
            print("error")
    def return_book(self,book):
        if book in self.borrowedbooks:
            book.return_book()
            self.borrowedbooks.remove(book)
            print(f"{self.name} has returned {book.title}")
        else:
            print("error")
    def showborrowedbooks(self):
        print(f"{self.name}'s borrowed books:")
        if not self.borrowedbooks:
            print("No books borrowed")
        else:
            for book in self.borrowedbooks:
                print(f"-{book.title}")
class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def addbooks(self,book):
        self.books.append(book)
    def showbooks(self):
        print(f"books in {self.name}")
        for book in self.books:
            print(f"-{book}")
    def findbook(self,title):
        for book in self.books:
            if book.title.lower()==title.lower(): 
                return book
        return None
if __name__=="__main__":
    myLibrary=Library("Central Library")



    book1=Book("War and Peace","Lev Tolstoy")
    book2=Book("Anna Karenina","Lev Tolstoy")
    book3=Book("1984","George Orwell")
    myLibrary.addbooks(book1)
    myLibrary.addbooks(book2)
    myLibrary.addbooks(book3)
    user1=User("Sarah")
    user2=User("Bob")
    myLibrary.showbooks()