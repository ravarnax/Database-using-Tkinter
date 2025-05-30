# ############ 19. Database using Tkinter ##############
from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry('500x400')



# Create table
# c.execute("""CREATE TABLE addresses (
#          first_name text,
#          last_name text,
#          address text,
#          city text,
#          state text,
#          zipcode integer
#          )""")

# Create a Edit function to Update a Record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    
    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
              first_name = :first,
              last_name = :last,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid""",
              {
                'first': f_name_editor.get(),
                'last': l_name_editor.get(),
                'address': address_editor.get(),
                'city': city_editor.get(),
                'state': state_editor.get(),
                'zipcode': zipcode_editor.get(),
                'oid': record_id
              }
            )
    
    # Commit changes
    conn.commit()
    
    # Close connection
    conn.close()
    
    editor.destroy()
    

def edit():
    global editor
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry('400x400')
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    
    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT *, oid FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    # Create Global Variables for text box names
    global f_name_editor, l_name_editor, address_editor, city_editor, state_editor, zipcode_editor 
    
    # Create entry textbox
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label_editor = Label(editor, text='First Name')
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text='Last Name')
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text='Address')
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text='City')
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text='State')
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text='Zipcode')
    zipcode_label_editor.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])    
        l_name_editor.insert(0, record[1])    
        address_editor.insert(0, record[2])    
        city_editor.insert(0, record[3])    
        state_editor.insert(0, record[4])    
        zipcode_editor.insert(0, record[5])    

    # Create a Save Button to Save edited record
    edit_btn = Button(editor, text='Save Record', command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
        
        
# Create function to Delete a Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # Create cursor
    c = conn.cursor()
    
    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid="+ delete_box.get())
    
    # Commit cursor 
    conn.commit()
    
    # Close connection
    conn.close()
    
# Create Submit function for database
def submit():
# Database

    # Cr`eate a database or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # Create cursor
    c = conn.cursor()
    
    # Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })
    # Commit cursor
    conn.commit()
    
    # Close connection
    conn.close()
    
    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    
    # Loop through Results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1])  + " " + "\t" + str(record[6]) +  "\n"
        
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# Create entry textbox
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State')
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text='Select ID')
delete_box_label.grid(row=9, column=0, pady=5)

# Create submit Button
submit_btn = Button(root, text='Add record to database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text='Delete Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create an Update Button
edit_btn = Button(root, text='Edit Record', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

root.mainloop()
