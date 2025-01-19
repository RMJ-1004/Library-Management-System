import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Dummy librarian credentials (replace with your actual credentials)
librarian_username = "1111"
librarian_password = "100"

# Create the main window
root = tk.Tk()
root.title("Library Management System")

# Librarian login function
def librarian_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == librarian_username and password == librarian_password:
        login_frame.destroy()
        create_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create a login frame
login_frame = ttk.Frame(root)
login_frame.grid(row=0, column=0, padx=10, pady=10)

# Create labels and entry widgets for librarian login
username_label = ttk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0)
username_entry = ttk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = ttk.Entry(login_frame, show="*")  # Show asterisks for password
password_entry.grid(row=1, column=1)

login_button = ttk.Button(login_frame, text="Login", command=librarian_login)
login_button.grid(row=2, column=0, columnspan=2)

# Function to create the main menu
def create_menu():
    menu_frame = ttk.Frame(root)
    menu_frame.grid(row=0, column=0, padx=10, pady=10)

    def add_record():
        def add_data():
            book_id = book_id_entry.get()
            book_name = book_name_entry.get()
            author = author_entry.get()
            genre = genre_entry.get()
            shelf_no = shelf_no_entry.get()
            row_no = row_no_entry.get()
        
            try:
                # Connect to the MySQL database
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="books"
                )
                
                cursor = db.cursor()
                
                # Insert data into the MySQL database
                insert_query = "INSERT INTO shelf_1 (Book_ID, Book_Name, Author_Name, Genre, Shelf_No, Row_No) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (book_id, book_name, author, genre, shelf_no, row_no)
                cursor.execute(insert_query, data)

                db.commit()
                messagebox.showinfo("Success", "Record added successfully.")
        
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        
            finally:
                if db.is_connected():
                    cursor.close()
                    db.close()
        
        # Create the main window
        add_window = tk.Toplevel(root)
        add_window.title("Book Record Entry")

        # Create labels and entry widgets for book details
        book_id_label = tk.Label(add_window, text="Book ID:")
        book_id_label.grid(row=0, column=0)
        book_id_entry = tk.Entry(add_window)
        book_id_entry.grid(row=0, column=1)

        book_name_label = tk.Label(add_window, text="Book Name:")
        book_name_label.grid(row=1, column=0)
        book_name_entry = tk.Entry(add_window)
        book_name_entry.grid(row=1, column=1)
        
        author_label = tk.Label(add_window, text="Author:")
        author_label.grid(row=2, column=0)
        author_entry = tk.Entry(add_window)
        author_entry.grid(row=2, column=1)

        genre_label = tk.Label(add_window, text="Genre:")
        genre_label.grid(row=3, column=0)
        genre_entry = tk.Entry(add_window)
        genre_entry.grid(row=3, column=1)

        shelf_no_label = tk.Label(add_window, text="Shelf No:")
        shelf_no_label.grid(row=4, column=0)
        shelf_no_entry = tk.Entry(add_window)
        shelf_no_entry.grid(row=4, column=1)

        row_no_label = tk.Label(add_window, text="Row No:")
        row_no_label.grid(row=5, column=0)
        row_no_entry = tk.Entry(add_window)
        row_no_entry.grid(row=5, column=1)

        # Create a button to add the book record
        add_button = tk.Button(add_window, text="Add Record", command=add_data)
        add_button.grid(row=6, column=0, columnspan=2)

    def update_record():
        def update_data():
            book_id = book_id_entry.get()
            new_row_no = new_row_no_entry.get()

            try:
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="books"
                )
                cursor = db.cursor()

                # Update the ROW_NO based on the user's input
                sql = f"UPDATE SHELF_1 SET ROW_NO = {new_row_no} WHERE BOOK_ID = '{book_id}'"
                cursor.execute(sql)

                db.commit()
                messagebox.showinfo("Success", "Record Updated")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

            finally:
                if db.is_connected():
                    cursor.close()
                    db.close()

        # Create the main window
        update_window = tk.Toplevel(root)
        update_window.title("Update Book Record")

        # Create labels and entry widgets for Book ID and new Row No
        book_id_label = tk.Label(update_window, text="Book ID:")
        book_id_label.pack()
        book_id_entry = tk.Entry(update_window)
        book_id_entry.pack()

        new_row_no_label = tk.Label(update_window, text="New Row No:")
        new_row_no_label.pack()
        new_row_no_entry = tk.Entry(update_window)
        new_row_no_entry.pack()

        # Create a button to update the book record
        update_button = tk.Button(update_window, text="Update Record", command=update_data)
        update_button.pack()

    def search_record():
        def search_data():
            book_name = book_name_entry.get()
    
            try:
                # Connect to the MySQL database
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="books"
                )

                cursor = db.cursor()

                # Execute a SELECT query to search for the book record by name
                select_query = "SELECT * FROM shelf_1 WHERE Book_Name = %s"
                cursor.execute(select_query, (book_name,))
                record = cursor.fetchone()

                if record:
                    # Display the record in a messagebox
                    record_str = "Book ID: {}\nBook Name: {}\nAuthor: {}\nGenre: {}\nShelf No: {}\nRow No: {}".format(*record)
                    messagebox.showinfo("Search Result", record_str)
                else:
                    messagebox.showinfo("Search Result", "Book not found")
    
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
    
            finally:
                if db.is_connected():
                    cursor.close()
                    db.close()

        # Create the main window
        search_window = tk.Toplevel(root)
        search_window.title("Book Data Retrieval")

        # Create a new frame for the search section
        search_frame = ttk.Frame(search_window)
        search_frame.pack(pady=10)

        # Create a new entry widget for the book name
        book_name_label = ttk.Label(search_frame, text="Book Name:")
        book_name_label.grid(row=1, column=0)
        book_name_entry = ttk.Entry(search_frame)
        book_name_entry.grid(row=1, column=1)

        # Create a button to search for a book record by name
        search_button = ttk.Button(search_frame, text="Search Record", command=search_data)
        search_button.grid(row=2, column=0, columnspan=2)

    def delete_record():
        def del_data():
            book_id = book_id_entry.get()

            try:
                # Connect to the MySQL database
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="books"
                )

                cursor = db.cursor()

                # Execute a DELETE query to delete the book record
                delete_query = "DELETE FROM shelf_1 WHERE Book_ID = %s"
                cursor.execute(delete_query, (book_id,))

                db.commit()
                messagebox.showinfo("Success", "Record Deleted")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

            finally:    
                if db is not None and db.is_connected():
                    cursor.close()
                    db.close()

        # Create the main window
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Book Record")

        # Create a label and entry widget for Book ID
        book_id_label = tk.Label(delete_window, text="Book ID:")
        book_id_label.grid(row=0, column=0)
        book_id_entry = tk.Entry(delete_window)
        book_id_entry.grid(row=0, column=1)

        # Create a button to delete the book record
        delete_button = tk.Button(delete_window, text="Delete Record", command=del_data)
        delete_button.grid(row=1, column=0, columnspan=2)

    def display_record():
        def display_data():
            try:
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="books"
                )
                cursor = db.cursor()
                cursor.execute("SELECT * FROM shelf_1")
                results = cursor.fetchall()

                # Create a new tkinter window to display the results in a table
                result_window = tk.Toplevel()
                result_window.title("Book Records")

                # Create a Treeview widget to display the data in tabular form
                columns = ("Book ID", "Book Name", "Author", "Genre", "Shelf No", "Row No")
                tree = ttk.Treeview(result_window, columns=columns, show="headings")

                # Set column headings
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=100)

                # Insert the fetched data into the Treeview
                for record in results:
                    tree.insert("", "end", values=record)

                tree.pack() 

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

            finally:
                if db.is_connected():
                    cursor.close()
                    db.close()

        # Create the main window
        display_window = tk.Toplevel(root)
        display_window.title("Book Data Retrieval")

        # Create a button to fetch data
        fetch_button = tk.Button(display_window, text="Fetch Book Data", command=display_data)
        fetch_button.pack()

    # Create buttons for menu options
    add_button = ttk.Button(menu_frame, text="Add Record", command=add_record)
    add_button.grid(row=0, column=0)

    update_button = ttk.Button(menu_frame, text="Update Record", command=update_record)
    update_button.grid(row=0, column=1)

    search_button = ttk.Button(menu_frame, text="Search Record", command=search_record)
    search_button.grid(row=0, column=2)

    delete_button = ttk.Button(menu_frame, text="Delete Record", command=delete_record)
    delete_button.grid(row=0, column=3)

    display_button = ttk.Button(menu_frame, text="Display Record", command=display_record)
    display_button.grid(row=0, column=4)

# Main loop
root.mainloop()
