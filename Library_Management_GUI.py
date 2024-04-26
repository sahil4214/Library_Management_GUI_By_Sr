#!/usr/bin/env python
# coding: utf-8

# # Library Management System Project

# * In this Python project, we will build a GUI-based Library Management System project using the Tkinter library, SQLite3 API, and messagebox modules of Tkinter. It is an intermediate-level project, where you will get to learn about some exciting features of database management in Python and apply them in real life. Let’s get started!
#
# * About Library Management Systems:
# * Library Management Systems are used to manage information about contents in a library. They are used to manage information relating to books, their names, codes, author names, whether they have been issued or not and if so, who has issued them and what their card’s ID is; a library management system is used to store and manage all this information.
#
# * About the Python Library Management System project:
# * The objective of this is to create a GUI based Library Management System. To build this, you will need intermediate understanding of the SQLite API and its commands, intermediate understanding of Tkinter library, Ttk module’s Treeview, and basic understanding of messagebox module.
#
# * Python Library Management Project Prerequisites:
# * To build this project, we will need the following Python libraries:
#
# * 1. Tkinter – To create the GUI
# * a. messagebox – To display boxes showing information or error or asking yes or no.
# * b. Ttk.Treeview – To display all the information in the GUI window.
# * c. simpledialog – To use pre-defined simple dialog boxes provided by Tkinter.
#
# * 2. SQLite – To connect to the database and perform operations in it
#
# * The SQLite3 library does not come pre-installed so you will need to run the following command to install it:

# # Library Management System Project File Structure:
# Here are the steps you will need to execute to build this Library Management System project:
#
# Importing all necessary modules and connecting to the database
# Initializing the GUI window and placing all its components
# Defining all the data storage and manipulation functions
# Let’s take a closer look at these steps:
#
#

# # 1. Importing all necessary modules and connecting to the database:

# In[1]:


from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import sqlite3

# Connecting to Database
connector = sqlite3.connect('library.db')
cursor = connector.cursor()

# Update table schema to include ISSUER_NAME column
connector.execute(
    'CREATE TABLE IF NOT EXISTS Library (BK_NAME TEXT, BK_ID TEXT PRIMARY KEY NOT NULL, AUTHOR_NAME TEXT, BK_STATUS TEXT, CARD_ID TEXT, ISSUER_NAME TEXT)'
)



# # Explanation:
# The sqlite.connect(‘library.db’) command is used to connect the Python script to the database provided as argument.
# The connector.cursor() line is used to assign a cursor to your database.
#

# # 2. Defining all the backend functions:
#

# In[2]:


# Functions
def issuer_card():
    Cid = sd.askstring('Issuer Card ID', 'What is the Issuer\'s Card ID?\t\t\t')

    if not Cid:
        mb.showerror('Issuer ID cannot be zero!', 'Can\'t keep Issuer ID empty, it must have a value')
    else:
        return Cid

def display_records():
    global connector, cursor
    global tree

    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM Library')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)

def clear_fields():
    global bk_status, bk_id, bk_name, author_name, card_id, issuer_name

    bk_status.set('Available')
    for i in ['bk_id', 'bk_name', 'author_name', 'card_id', 'issuer_name']:
        exec(f"{i}.set('')")
    bk_id_entry.config(state='normal')
    try:
        tree.selection_remove(tree.selection()[0])
    except:
        pass

def clear_and_display():
    clear_fields()
    display_records()



# # Explanation:
# * These are the functions that will repeatedly be used in our data storage and manipulation of the inventory, and will play an important role in those functionalities, but are not explicit functionalities in the system.
# * issuer_card():
# * We will use this function when the book selected isn’t available (i.e. it has been issued).
# * This function will be initiated whenever we are adding/updating our book details to add the Card ID of whoever is issuing the book.
# * In this function, we use sd.askstring() to ask the user for a string that we will store as our book issuer’s card ID. If the string is empty, we will display an error.
# * display_records():
# * This function will be used to display all the records from our database to our table in the GUI window, whenever we are making any changes to the data in our database (as the data is not automatically updated in the table).
# * First, we delete everything from our table (referred to as “tree” in our code) and then we use SQL’s SELECT * query to get everything from the table, that we will insert in our table to update it for any changes.
# * clear_fields():
# * This function will be used whenever there are some values in our entry boxes in our window, which will be removed using this.
# * This is the only functionality in this group that is also available as a button.
# * In this, all we will do is set all our StringVar objects to an empty string (our StringVar objects manipulate all the entry fields) and set the state of the box_id_entry to normal (we will do this because we disable it when updating the book details).
# * clear_and_display():
# * This function is a combination of the clear_fields() and the display_records() to help our code become cleaner and less lengthier.
# * view_record():
# * This function is used to display the details of a selected record (row) in our table.
# * This function will first check if there is a record that has been selected. If not, it will display an error box. If yes, it takes the values in that record, and assigns them to our StringVar variables, which in turn displays it on the entry fields.

# # 3. Defining all the data storage and manipulation functions:

# In[3]:


def add_record():
    global connector
    global bk_name, bk_id, author_name, bk_status, card_id, issuer_name

    if bk_status.get() == 'Issued':
        card_id.set(issuer_card())
    else:
        card_id.set('N/A')
        issuer_name.set('N/A')

    surety = mb.askyesno('Are you sure?', 'Are you sure this is the data you want to enter?\nPlease note that Book ID cannot be changed in the future')

    if surety:
        try:
            connector.execute(
                'INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID, ISSUER_NAME) VALUES (?, ?, ?, ?, ?, ?)',
                (bk_name.get(), bk_id.get(), author_name.get(), bk_status.get(), card_id.get(), issuer_name.get()))
            connector.commit()

            clear_and_display()

            mb.showinfo('Record added', 'The new record was successfully added to your database')
        except sqlite3.IntegrityError:
            mb.showerror('Book ID already in use!', 'The Book ID you are trying to enter is already in the database, please alter that book\'s record or check any discrepancies on your side')

def view_record():
    global bk_name, bk_id, bk_status, author_name, card_id, issuer_name
    global tree

    if not tree.focus():
        mb.showerror('Select a row!', 'To view a record, you must select it in the table. Please do so before continuing.')
        return

    current_item_selected = tree.focus()
    values_in_selected_item = tree.item(current_item_selected)
    selection = values_in_selected_item['values']

    bk_name.set(selection[0])
    bk_id.set(selection[1])
    bk_status.set(selection[3])
    author_name.set(selection[2])
    try:
        card_id.set(selection[4])
        issuer_name.set(selection[5])
    except:
        card_id.set('')
        issuer_name.set('')

def update_record():
    def update():
        global bk_status, bk_name, bk_id, author_name, card_id, issuer_name
        global connector, tree

        if bk_status.get() == 'Issued':
            card_id.set(issuer_card())
        else:
            card_id.set('N/A')

        cursor.execute('UPDATE Library SET BK_NAME=?, BK_STATUS=?, AUTHOR_NAME=?, CARD_ID=?, ISSUER_NAME=? WHERE BK_ID=?',
                       (bk_name.get(), bk_status.get(), author_name.get(), card_id.get(), issuer_name.get(), bk_id.get()))
        connector.commit()

        clear_and_display()

        edit.destroy()
        bk_id_entry.config(state='normal')
        clear.config(state='normal')

    view_record()

    bk_id_entry.config(state='disable')
    clear.config(state='disable')

    edit = Button(left_frame, text='Update Record', font=btn_font, bg=btn_hlb_bg, width=20, command=update)
    edit.place(x=50, y=425)

def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    cursor.execute('DELETE FROM Library WHERE BK_ID=?', (selection[1], ))
    connector.commit()

    tree.delete(current_item)

    mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

    clear_and_display()

def delete_inventory():
    if mb.askyesno('Are you sure?', 'Are you sure you want to delete the entire inventory?\n\nThis command cannot be reversed'):
        tree.delete(*tree.get_children())

        cursor.execute('DELETE FROM Library')
        connector.commit()
    else:
        return

def change_availability():
    global tree, connector

    if not tree.selection():
        mb.showerror('Error!', 'Please select a book from the database')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    BK_id = values['values'][1]
    BK_status = values["values"][3]

    if BK_status == 'Issued':
        surety = mb.askyesno('Is return confirmed?', 'Has the book been returned to you?')
        if surety:
            cursor.execute('UPDATE Library SET bk_status=?, card_id=?, issuer_name=? WHERE bk_id=?', ('Available', 'N/A', 'N/A', BK_id))
            connector.commit()
        else:
            mb.showinfo('Cannot be returned', 'The book status cannot be set to Available unless it has been returned')
    else:
        card_id.set(issuer_card())
        cursor.execute('UPDATE Library SET bk_status=?, card_id=? WHERE bk_id=?', ('Issued', card_id.get(), BK_id))
        connector.commit()

    clear_and_display()
# Variables
lf_bg = 'LightSkyBlue'
rtf_bg = 'DeepSkyBlue'
rbf_bg = 'DodgerBlue'
btn_hlb_bg = 'SteelBlue'

lbl_font = ('Georgia', 13)
entry_font = ('Times New Roman', 12)
btn_font = ('Gill Sans MT', 13)

# Initializing the main GUI window
root = Tk()
root.title('SR_GUI_Project: Library Management System')
root.geometry('1200x600')
root.resizable(0, 0)


Label(root, text='LIBRARY MANAGEMENT SYSTEM', font=("Noto Sans CJK TC", 15, 'bold'), bg=btn_hlb_bg, fg='White').pack(side=TOP, fill=X)



# # Explanation:
# * In this step, we will define all the functions that will manipulate the data in the table (GUI window) and the database.
# * add_record():
# * This is the book addition functionality of our system. When this function is initiated, it will read all the entry fields, and then add those to our SQL table using the INSERT query and then use the display_records() function we defined earlier to add that to our GUI tree as well.
# * We start off by adding a condition that if the bk_status (status of the book, whether it is available or has been issued) has been set to “Issued”, we will get the card_id using the previously defined issuer_card() function, else we’ll set it to N/A (not applicable because the book is available), and then issue a warning that book ID cannot be changed so be sure (because we will be saving the changes in a book’s details using it’s book ID so it must not be changed). After the user is sure, we will insert it to the database by using the cursor.execute() and connector.commit() commands, where we will pass the SQL query as an argument to the former.
# * remove_record():
# * This is the book deletion functionality of our system. When this function is initiated, it will read the selected record in our GUI table, and then delete from both, our GUI table and SQL database table using the tree.delete() method and DELETE query respectively. We will get the values from the currently selected item of the table in the GUI window (if there is no selected record, we will issue an error box), we will remove that item from the table by using the execute-commit combo and from the GUI data table by uniquely identifying it by the book ID value.
# * delete_inventory():
# * This is the inventory deletion functionality of our system that will remove everything from both our tables.
# * We will ask the user if they are sure of erasing everything in the database. If they are, we will delete everything from the database and the table and print an info message late, but if they are not, we will abort the process.
# * update_record():
# * This is the book details update functionality of our system. This function, when initiated, makes some changes to our GUI window and activates the update() sub-function when the new button on our input field has been pressed (that button should be pressed when changes have been made).
# * update():
# * This sub-function to the update_record() function, we do something similar to the add_record() function but we use the UPDATE query rather than the INSERT query, and then we revert back the changes on the window to the original.
# * change_availability():
# * This is the issue/return book functionality of your system. This function will change an available book to an issued book (and add the issuer’s card ID using the issuer_card() function) and vice-versa.
# * We first check if there is a record selected in our GUI table (if there isn’t, we issue an error box). If the status is Issued, we ask the user if the return is confirmed and then update the record with status as Available as ID as ‘N/A’. If the book is Available, we use the issuer_card() function to enter the card ID of the issuer and then update the SQL table. Then we display the changes on the GUI table as well.

# # 4. Initializing the GUI window and placing all its components:

# In[4]:


# StringVars
bk_status = StringVar()
bk_name = StringVar()
bk_id = StringVar()
author_name = StringVar()
card_id = StringVar()
issuer_name = StringVar()

# Frames
left_frame = Frame(root, bg=lf_bg)
left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

RT_frame = Frame(root, bg=rtf_bg)
RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

RB_frame = Frame(root)
RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

# Left Frame
Label(left_frame, text='Book Name', bg=lf_bg, font=lbl_font).place(x=98, y=25)
Entry(left_frame, width=25, font=entry_font, textvariable=bk_name).place(x=45, y=55)

Label(left_frame, text='Book ID', bg=lf_bg, font=lbl_font).place(x=110, y=105)
bk_id_entry = Entry(left_frame, width=25, font=entry_font, textvariable=bk_id)
bk_id_entry.place(x=45, y=135)

Label(left_frame, text='Author Name', bg=lf_bg, font=lbl_font).place(x=90, y=185)
Entry(left_frame, width=25, font=entry_font, textvariable=author_name).place(x=45, y=215)

Label(left_frame, text='Status of the Book', bg=lf_bg, font=lbl_font).place(x=75, y=265)
dd = OptionMenu(left_frame, bk_status, *['Available', 'Issued'])
dd.configure(font=entry_font, width=12)
dd.place(x=75, y=300)

Label(left_frame, text='Issuer Name', bg=lf_bg, font=lbl_font).place(x=85, y=340)
Entry(left_frame, width=25, font=entry_font, textvariable=issuer_name).place(x=45, y=370)

submit = Button(left_frame, text='Add new record', font=btn_font, bg=btn_hlb_bg, width=20, command=add_record)
submit.place(x=50, y=475)

clear = Button(left_frame, text='Clear fields', font=btn_font, bg=btn_hlb_bg, width=20, command=clear_fields)
clear.place(x=50, y=525)

# Right Top Frame
Button(RT_frame, text='Delete book record', font=btn_font, bg=btn_hlb_bg, width=17, command=remove_record).place(x=8, y=30)
Button(RT_frame, text='Delete full inventory', font=btn_font, bg=btn_hlb_bg, width=17, command=delete_inventory).place(x=178, y=30)
Button(RT_frame, text='Update book details', font=btn_font, bg=btn_hlb_bg, width=17, command=update_record).place(x=348, y=30)
Button(RT_frame, text='Change Book Availability', font=btn_font, bg=btn_hlb_bg, width=19, command=change_availability).place(x=518, y=30)

# Right Bottom Frame
Label(RB_frame, text='BOOK INVENTORY', bg=rbf_bg, font=("Noto Sans CJK TC", 15, 'bold')).pack(side=TOP, fill=X)

tree = ttk.Treeview(RB_frame, selectmode=BROWSE, columns=('Book Name', 'Book ID', 'Author', 'Status', 'Issuer Card ID', 'Issuer Name'))

XScrollbar = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
YScrollbar = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
XScrollbar.pack(side=BOTTOM, fill=X)
YScrollbar.pack(side=RIGHT, fill=Y)

tree.config(xscrollcommand=XScrollbar.set, yscrollcommand=YScrollbar.set)

tree.heading('Book Name', text='Book Name', anchor=CENTER)
tree.heading('Book ID', text='Book ID', anchor=CENTER)
tree.heading('Author', text='Author', anchor=CENTER)
tree.heading('Status', text='Status of the Book', anchor=CENTER)
tree.heading('Issuer Card ID', text='Card ID of the Issuer', anchor=CENTER)
tree.heading('Issuer Name', text='Issuer Name', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=225, stretch=NO)
tree.column('#2', width=70, stretch=NO)
tree.column('#3', width=150, stretch=NO)
tree.column('#4', width=105, stretch=NO)
tree.column('#5', width=132, stretch=NO)
tree.column('#6', width=132, stretch=NO)

tree.place(y=30, x=0, relheight=0.9, relwidth=1)

clear_and_display()

# Finalizing the window
root.update()
root.mainloop()


# # Explanation:
# * In this step, we will create our entire GUI window.
# * We have a top head label which has the name of our project.
# * We then have a frame on the left-side of the window, named left_frame where we have all our entry fields that store the book’s name, its ID according to the library, author’s name, whether it is issued or available and if it issued, it also stores the card ID of the person who has issued it. Also we have a button that takes all the fields’ data and puts them in the table when pressed.
# * On the right side of the window, we have 2 windows: one on the top and the other on the bottom.
# * The one on the bottom is called the RB_frame (short for ‘right bottom frame’) where we have a head label packed to the top of the frame and the table (Treeview instance) where all our data from the database table has been sorted into columns which is controlled by two scrollbars on the right and bottom sides of it.
# * The one on the top, called the RT_frame, has all the buttons to perform operations on the tree and the database.
#
# # Library Management System Project Output

# **Summary
# Congratulations! You have now created your own Library Management System project using only the Tkinter and SQLite libraries of Python.**
#
# **You can ask the librarians in your community to use this project to manage all the books in her library. They will be effectively able to manage without any hassles. Also you can ask your school to use this system.**
#
# **However, this project is not the ultimate best. There are a lot of updates that can be made to this, and you should keep on evolving this project.**
#
# **Have fun coding!**

# In[ ]:





# In[ ]:




