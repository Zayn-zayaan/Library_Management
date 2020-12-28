class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database has been updated.You can take the book now.")

        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == "__main__":
    zayn = Library(['Harry potter and the deathly hallows part 2', 'Python', 'C++',
        'Data structures and Algo', 'Wings of fire'], "Takeiteasy")
    
    while True:
        print(f"Welcome to the {zayn.name} library. Enter your choice to continue: ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        choice = input()
        
        if choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            choice = int(choice)

        if choice == 1:
            zayn.displayBooks()

        elif choice == 2:
            book = input("Enter the name of the book u want to lend: ")
            user = input("Enter your name: ")
            zayn.lendBook(user, book)

        elif choice == 3:
            book = input("Enter the name of the book u want to add: ")
            zayn.addBook(book)

        elif choice == 4:
            book = input("Enter the name of the book u want to return: ")
            zayn.returnBook(book)
            print("Your book has been returned.Thankyou!!")

        else:
            print("Not a valid option")

        choice2 = ""

        while (choice2 != "c" and choice2 != "c"):
            choice2 = input("Press q to quit and c to continue: ")
            
            if choice2 == "q":
                print("Thankyou!!. Have a nice day")
                exit()
                
            elif choice2 == "c":
                continue


         



