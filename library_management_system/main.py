import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library_db"
)
mycursor = mydb.cursor()

# Create a table named `books` (if it doesn't exist)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    isbn VARCHAR(255)
    )
                 """)

print("Table created successfully")

def AddBook(title, author, isbn):
    sql = "INSERT INTO books(title, author, isbn) VALUES (%s, %s, %s)"
    val = (title, author, isbn)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, " book(s) titled", title,"added successfully")

def ListBooks():
    sql = "SELECT * FROM books"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        print("\nLibrary Book List:")
        for row in myresult:
            print(f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | ISBN: {row[3]}")
    else:
        print("\nNo books available in the library.")

    mycursor.close()
    mydb.close()

def DeleteBook(isbn):
    mydb = mysql.connector.connect()
    sql = "DELETE FROM books WHERE isbn = %s"
    val = (isbn)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, " book(s) deleted successfully")

def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Search Book by Title")
        print("3. List All Books")
        print("4. Delete Book by ISBN")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            AddBook(title, author, isbn)
        elif choice == "2":
            search_term = input("Enter title to search: ")
            search_books_by_title(search_term)
        elif choice == "3":
            ListBooks()
        elif choice == "4":
            try:
                isbn = int(input("Enter book ISBN to delete: "))
                DeleteBook(isbn)
            except ValueError:
                print("Invalid ISBN. Must be an integer.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")

if __name__ == "__main__":
    main()