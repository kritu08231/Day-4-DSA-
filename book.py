#define a class bokk with instance class object variables bookid,title, price. initialise them via __init() method also define method to show book variable.

class Book:
    def __init__(self,id=None,title=None,price=None):
        self.bookid=id
        self.booktitle=title
        self.bookprice=price
    def setbookid(self,id):
        self.bookid=id
    def setbooktitle(self,title):
        self.booktitle=title
    def setbookprice(self,price):
        self.bookprice=price
    def getbookid(self):
        return self.bookid
    def getbooktitle(self):
        return self.booktitle
    def getbookprice(self):
        return self.bookprice
    def showbook(self):
        return self.bookid,self.booktitle,self.bookprice

b1=Book()
b1.setbookid(67)
b1.setbooktitle("python")
b1.setbookprice(200)
print(b1.showbook())
B2=Book(21,"java",300)
print(B2.getbooktitle())