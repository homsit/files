"""
- Create a class that represents Author. Each author has:
(fname, lname, email) and the following methods:

	__str__: takes no input and returns a string representation of the author.

	equals: takes an author as input and returns True if they are equal; False otherwise.

- Create a class that represents Book. Each book has:
(ISBN, title, authors, year, publisher) and the following methods:

	__str__: takes no input and returns the APA representation of the book.

	equals: takes a book as input and returns True if they are equal; False otherwise.

- Create a class that represents Library. Each library has a (list_of_books) and the following methods:

	add_book: takes a book as input, adds it to the list_of_books and returns nothing.

	search: takes a book as input and returns a tuple that cosists of the location of the book in the list_of_books, and the book itself if found, -1 otherwise.

	remove_book: takes a book as input, removes it from the list_of_books and returns True if the book was removed correctly, False otherwise.

	-backup: takes filename as input and save the list of books into the file. 

	-restore: takes a filename as input and restores books data from the file (replaces the current ones).

- Using previous classes, create a program that can be used in the library to do the following:
	(1) Add new Book
	(2) Search for a book
	(3) Delet a book
	(4) Backup
	(5) Restore
	(6) Exit
"""