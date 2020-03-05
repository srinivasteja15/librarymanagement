class Library:
    def __init__(self,books,libname):
        self.books = books
        self.name = libname
        self.lbooks = {}
    def display(self):
        i = 1
        print(f"\nBooks available in {self.name} Library are -:")
        for book in self.books:
            print(f" {i}.{book} ")
            i += 1

    def lendbook(self):
        id = input("Enter Your name/id : ")

        bn = input("\nEnter name of book you want: ")
        if bn in self.books:
            self.books.pop(self.books.index(bn))
            self.lbooks[bn] = id

            print("\nTQ for lending")
        elif bn in self.lbooks.keys():
            print(f"{self.lbooks[bn]} had lended {bn} book earlier")
        else:
            print("Oops,book is not available")

    def addbook(self):
        bookname = input("Enter name of book you want to add : ")
        if bookname not in self.books:
            self.books.append(bookname)

        else:
            print("We already have this book")

        l = input("Want to add one more? : ")
        if  l == "y" or l == "yes":
            self.addbook()



    def returning(self):
        usrname = input("Your Name : ")
        bokname = input("Name of Book to return : ")
        if bokname in self.lbooks.keys():
            del self.lbooks[bokname]
            print("Thanks for returning")
        elif bokname in  self.books:
            print("You have returned it")
        else:
            print("We did not lend you book")


list = ["English","Chemistry","Maths","Hindi","Biology"]
obj = Library(list,"Python & Coding")
print(f"\t\t\t\t----Welcome to {obj.name} Library---- ")
print("Enter any of the following")
print("enter D to Display")
print("enter L to lend")
print("enter A to add books")
print("enter R to return")
key = input("What you want to Do : ")

while 1:
    if key == 'd' or key == 'D':
        obj.display()
        key = input(" How can we help you (D/L/A/R): ")

    if key == 'l' or key == 'L':
        obj.lendbook()
        key = input(" How can we help you (D/L/A/R): ")

    if key == 'r' or key == 'R':
        obj.returning()

        key = input(" How can we help you (D/L/A/R): ")

    if key == 'a' or key == 'A':
        obj.addbook()
        key = input(" How can we help you (D/L/A/R): ")
    else:
        print("Invalid key ! ")
        u = input("Want to exit (y/n) : ")
        if u == "y" or u == "Y":
            break
        else:
            key = input(" How can I help you (D/L/A/R): ")
 

