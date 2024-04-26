# Library_Management_GUI_By_Sr
This is a Library Management GUI project that have so many feature like add book , delete , issuer name etc...  this text file with * specialy for python jupyter that i write for you all so it make easy for you all ....

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



# # Explanation:
# The sqlite.connect(‘library.db’) command is used to connect the Python script to the database provided as argument.
# The connector.cursor() line is used to assign a cursor to your database.
#

# # 2. Defining all the backend functions:




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
