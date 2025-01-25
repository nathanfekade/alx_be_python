class Book:

    def __init__(self, title, author):
        
        self.title = title
        self.author = author
        self._is_checked_out = False
   
    def check_out(self):
        
        if not self._is_checked_out:
            self._is_checked_out = True
        return
            

    
    def return_book(self):
        
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."
    
    def is_available(self):
        
        return not self._is_checked_out
        


class Library:

    
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self,title):
        
        for book in self._books:
            if book.title == title:
                book1 = Book('',title)
                book1.check_out()

    def return_book(self,title):

        for book in self._books:
            if book.title == title:
                book1 = Book('', title)
                book1.return_book()
    
    def list_available_books(self):

        for book in self._books:
            print(f"{book.title} by {book.author}")

        
    
        