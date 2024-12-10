import mysql.connector
import matplotlib.pyplot as plt

def create_database():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS bookstore")
        conn.close()
        print("Database created successfully!")
    except Exception as e:
        print(f"Error creating database: {e}")

def connect_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="",
            database="bookstore"
        )
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                price FLOAT NOT NULL
            )
        """)
        db.commit()
        return db
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def add_book(db):
    book = {
        'title': input("Enter book title: "),
        'author': input("Enter author name: "),
        'quantity': int(input("Enter quantity: ")),
        'price': float(input("Enter price: "))
    }
    
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, quantity, price) 
        VALUES (%s, %s, %s, %s)
    """, (book['title'], book['author'], book['quantity'], book['price']))
    db.commit()
    print("Book added successfully!")

def search_book(db):
    search_term = input("Enter book title or author to search: ")
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM books 
        WHERE title LIKE %s OR author LIKE %s
    """, (f"%{search_term}%", f"%{search_term}%"))
    
    results = cursor.fetchall()
    if results:
        for book in results:
            print(f"\nID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Quantity: {book[3]}")
            print(f"Price: ${book[4]:.2f}")
    else:
        print("No books found!")

def show_availability_chart(db):
    cursor = db.cursor()
    cursor.execute("SELECT title, quantity FROM books")
    results = cursor.fetchall()
    
    if results:
        titles = [book[0] for book in results]
        quantities = [book[1] for book in results]
        
        plt.figure(figsize=(10, 6))
        plt.bar(titles, quantities)
        plt.title('Book Availability Chart')
        plt.xlabel('Books')
        plt.ylabel('Quantity')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No books to display!")

def main():
    create_database()
    db = connect_db()
    
    if db:
        while True:
            print("\n=== Book Management System ===")
            print("1. Add Book")
            print("2. Search Book")
            print("3. Show Availability Chart")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                add_book(db)
            elif choice == '2':
                search_book(db)
            elif choice == '3':
                show_availability_chart(db)
            elif choice == '4':
                db.close()
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()