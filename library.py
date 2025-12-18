class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def listBook(self):
        self.file.seek(0)
        books_data = self.file.read()
        books_list = books_data.splitlines()
        if not books_list:
            print("There is no book in the list.")
        else:
            for book in books_list:
               print(book)
        
    def addBook(self):
        name = input("Book Name: ")
        author = input("Author: ")
        year = input("Release Year: ")
        pagenumber = input("Pages: ")

        with open("books.txt", "a+") as f:
            f.write(f"{name}, {author}, {year}, {pagenumber}\n")
    
    def removeBook (self):
        name = input("Book Name: ")
        with open ("books.txt", "r") as f:
            books = f.readlines()
        
        books_list = []
        for line in books :
            books_list.append(line.strip())

        index_to_remove = None
        for i, book in enumerate(books_list):
            if name in book:
                index_to_remove = i
                break
      
        if index_to_remove is not None:
            del books_list[index_to_remove]
            open("books.txt", "w").close() 
            with open("books.txt", "a+") as f:
                for book in books_list:
                    f.write(book + "\n")
            print(f"Book '{name}' removed successfully.")
        else:
            print(f"Book '{name}' not found.")    


    def __del__(self):
        self.file.close()    
   
def user_request () :
    lib = Library()
    while True :
        request = input("***MENU*** \n 1)List Books \n 2)Add Book \n 3)Remove Book \n ")
        if request == "1" :
            lib.listBook() 
        elif request == "2" :
            lib.addBook() 
        elif request == "3" :
            lib.removeBook()
        elif request == "Q" :
            break
        else :
            print("Please write 1,2,3 or Q")

user_request()






