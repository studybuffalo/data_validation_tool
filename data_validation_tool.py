#!/usr/bin/env python3

"""Tool to validate data extracted from other SB programs

    Last Update: 2017-Mar-31

    Copyright (c) Notices
	    2017	Joshua R. Torrance	<studybuffalo@studybuffalo.com>
	
    This program is free software: you can redistribute it and/or 
    modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of 
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, 
    see <http://www.gnu.org/licenses/>.

    SHOULD YOU REQUIRE ANY EXCEPTIONS TO THIS LICENSE, PLEASE CONTACT 
    THE COPYRIGHT HOLDERS.
"""

class ProgramData(object):
    def __init__(self, title):
        self.title = title
        self.tables = []

class TableData(object):
    def __init__(self, title, name, colData, colNames):
        self.title = title
        self.name = name
        self.columns = colData
        self.columnNames = colNames
        self.select = ("SELECT %s FROM %s ORDER BY %s ASC LIMIT 10" 
                       % (", ".join(colNames), name, colNames[0]))

class ColumnData(object):
    def __init__(self, title, name, width, valid, copy, search):
        self.title = title
        self.name = name
        self.width = width
        self.valid = valid
        self.copy = copy
        self.search = search

def collect_table_info(conf, log):
    # TO DO: NEED TO ADD ERROR HANDLING FOR NON-EXISTANT DATA
    # Collect the overall program names
    progSects = conf.get("programs", "sects").split(",")

    # For each program, find names of each table
    programList = []

    for prog in progSects:
        # Set the program config section name
        progSect = "prog_%s" % prog

        # Get the title of the entire program
        progTitle = conf.get(progSect, "title")
        
        # Compile data into object
        program = ProgramData(progTitle)

        # Get the names 
        tabSects = conf.get(progSect, "sects").split(",")
        
        # For each table, collected the needed info
        for tab in tabSects:
            # Set the table config section name
            tabSect = "table_%s_%s" % (prog, tab)

            # Get the title of the table section
            tabTitle = conf.get(tabSect, "title")

            # Get the MySQL name of the table
            tabName = conf.get(tabSect, "name")

            # Get the column config section names
            colSects = conf.get(tabSect, "sects").split(",")
            
            # For each column, collect the needed information
            colData = []
            colNames = []

            for col in colSects:
                # Set the column config section name
                colSect = "col_%s_%s_%s" % (prog, tab, col)

                # Get the title of the column
                colTitle = conf.get(colSect, "title")

                # Get the MySQL name of the column
                colName = conf.get(colSect, "name")

                # Get the display width of the column
                colWidth = conf.getint(colSect, "width")

                # Get whether to validate the column section
                colVal = conf.getboolean(colSect, "validate")

                # Get whether to add a copy button to the section
                colCopy = conf.getboolean(colSect, "copy")

                # Get whether to add a search button to the section
                colSearch = conf.getboolean(colSect, "search")

                # Compile data into object
                column = ColumnData(colTitle, colName, colWidth, colVal, 
                                    colCopy, colSearch)

                # Add finished column object to list
                colData.append(column)
                colNames.append(colName)
            
            # Compile data into object
            table = TableData(tabTitle, tabName, colData, colNames)

            # Add finished table object to list
            program.tables.append(table)

        # Add finished program object to list
        programList.append(program)

    return programList

def collect_icons():
    """Collects all program icons and saves them in object"""
    class Icons(object):
        def __init__(self, copy, search, upload, val, inval):
            self.copy = copy
            self.search = search
            self.upload = upload
            self.val = val
            self.inval = inval

    copyP = r"E:\My Documents\GitHub\data_validation_tool\icons\copy.png"
    copyImage = PhotoImage(file=copyP)

    searchP = r"E:\My Documents\GitHub\data_validation_tool\icons\search.png"
    searchImage = PhotoImage(file=searchP)

    uploadP = r"E:\My Documents\GitHub\data_validation_tool\icons\upload.png"
    uploadImage = PhotoImage(file=uploadP)

    valP = r"E:\My Documents\GitHub\data_validation_tool\icons\validated.png"
    valImage = PhotoImage(file=valP)

    invalP = r"E:\My Documents\GitHub\data_validation_tool\icons\invalid.png"
    invalImage = PhotoImage(file=invalP)

    return Icons(copyImage, searchImage, uploadImage, valImage, invalImage)

def clear_frame(frame):
    for child in frame.winfo_children():
        child.destroy()

def create_menu_bar(root, db, programInfo):
    root.option_add("*tearOff", FALSE)

    menubar = Menu(root)

    menuFile = Menu(menubar)
    menuFile.add_command(
        label="Return to main menu", 
        command=lambda: create_main_page(root, db, programInfo)
    )
    menuFile.add_command(label="Close", command=root.quit)
    menuAbout = Menu(menubar)
    menubar.add_cascade(menu=menuFile, label="File")
    menubar.add_cascade(menu=menuAbout, label="About")

    root.config(menu=menubar)

def copy_text(text):
    log.debug("Copying %s to clipboard" % text)
    root.clipboard_clear()
    root.clipboard_append(text)

def search_text(text):
    """Searches the Google.ca for the text"""
    log.debug("Searching for %s on Google.ca" % text)

    # Replace all white space with "+" for the search query
    search = text.replace(" ", "+")
    url = "https://www.google.ca/search?q=%s&adtext=off" % search

    # Open the browser in a new tab (if possible)
    webbrowser.open_new_tab(url)

def create_validation_frame(root, db, table):
    log.debug("Creating the validation window for %s" % table.title)
    
    # Collect database data
    data = database.retrieve_table_data(db.cursor, table.select, 
                                        table.columnNames, log)

    # Remove old content
    clear_frame(dashboard)

    # Font Styles and Label Styles
    fontTitle = font.Font(size=16, weight="bold")
    fontH1 = font.Font(size=13, weight="bold")
    
    # Set program bar title
    root.title(table.title)

    # Variables to hold grid locations
    x = 0
    y = 0

    # Create the title
    pageTitle = ttk.Label(dashboard, text=table.title, font=fontTitle)
    pageTitle.grid(column=x, row=y, sticky=(N, W), pady=(0,10))
    y = y + 1

    horSep1 = ttk.Separator(dashboard,orient=HORIZONTAL)
    horSep1.grid(column=x, row=y, sticky=(E, W), pady=5)
    y = y + 1

    # Create the headers
    for col in table.columns:
        # Determine colspan
        span = 1

        if col.valid:
            span = span + 1

        if col.copy:
            span = span + 1

        if col.search:
            span = span + 1

        # Create label
        colLabel = ttk.Label(dashboard, text=col.title, font=fontH1)
        colLabel.grid(column=x, row=y, sticky=(N, W), pady=5, padx=10, columnspan=span)

        # Advance to next label position
        x = x + span

    # Adjust the colspans for the title and separator
    pageTitle.grid_configure(columnspan=x)
    horSep1.grid_configure(columnspan=x)

    x = 0
    y = y + 1
    i = 0

    for row in data:
        for i in range(0, len(row)):
            # Use a message widget for the original info?
            width = table.columns[i].width
            valid = table.columns[i].valid
            copy = table.columns[i].copy
            search = table.columns[i].search

            if i == 0:
                elem = ttk.Label(dashboard, text=row[i], width=width)
                elem.grid(column=x, row=y, sticky=(N, W, S), pady=5, padx=10)
            else:
                elem = ttk.Entry(dashboard, width=width)
                elem.insert(0, row[i])
                elem.grid(column=x, row=y, sticky=(N, S, W), pady=5, padx=10)

            x = x + 1

            # Validation BSRF label
            if valid:
                valLabel = ttk.Label(dashboard, image=icons.inval)
                valLabel.grid(column=x, row=y, pady=5, padx=2)
                x = x + 1

            # Copy BSRF button
            if copy:
                copyBut = ttk.Button(
                    dashboard, image=icons.copy, 
                    command=lambda text=row[i]: copy_text(text)
                )
                copyBut.grid(column=x, row=y, pady=5, padx=2)
                x = x + 1

            # Search BSRF button
            if search:
                searchBut = ttk.Button(
                    dashboard, image=icons.search, 
                    command=lambda text=row[i]: search_text(text)
                )
                searchBut.grid(column=x, row=y, pady=5, padx=2)
                x = x + 1

        x = 0
        y = y + 1

    horSep2 = ttk.Separator(dashboard,orient=HORIZONTAL)
    horSep2.grid(column=x, row=y, sticky=(E, W), columnspan=5, pady=5)

def create_main_page(root, db, programInfo):
    root.title("Study Buffalo Data Validation Tool")
    
    # Variables to hold grid positions
    x = 0
    y = 0

    # Remove old content
    clear_frame(dashboard)

    # Font Styles and Label Styles
    fontTitle = font.Font(size=16, weight="bold")
    fontH1 = font.Font(size=13, weight="bold")
    fontH2 = font.Font(size=13, slant="italic")
    fontStats = font.Font(size=13)

    # Create a title
    appTitle = ttk.Label(dashboard, text="Study Buffalo Data Validation Tool", font=fontTitle)
    appTitle.grid(column=x, row=y, sticky=(N, W), pady=(0,10), columnspan=5)
    y = y + 1

    horSep1 = ttk.Separator(dashboard,orient=HORIZONTAL)
    horSep1.grid(column=x, row=y, sticky=(E, W), columnspan=5, pady=5)
    y = y + 1

    # Cycle through the table info and generate the navigation sections
    for program in programInfo:
        x = 0

        # Title
        abcLabel = ttk.Label(dashboard, text=program.title, font=fontH1)
        abcLabel.grid(column=x, row=y, sticky=(N, E), pady=5, padx=10)

        # Stats Label
        abcStat = ttk.Label(dashboard, text="Current Stats", font=fontH2)
        abcStat.grid(column=x, row=y + 1, sticky=(N, E), pady=5, padx=10)

        x = x + 1

        # Cycle through each table and created button
        for table in program.tables:

            # Table title (as a button)
            button = ttk.Button(
                dashboard, text=table.title, 
                command=lambda tab=table: create_validation_frame(root, db, tab)
            )
            button.grid(column=x, row=y, sticky=N, pady=5, padx=10)

            # Stats on how many entries need to be verified
            statsEntry = 0
    
            if statsEntry > 1:
                statsText = "%s entries" % statsEntry
                statsColour = "red"
            elif statsEntry == 1:
                statsText = "%s entry" % statsEntry
                statsColour = "red"
            else:
                statsText = "0 entries"
                statsColour = "green"

            statsLabel = ttk.Label(dashboard, text=statsText, font=fontStats, 
                                    foreground=statsColour)
            statsLabel.grid(column=x, row=y + 1, sticky=N, pady=5, padx=10)

            x = x + 1

        y = y + 2


import sys
from unipath import Path
import configparser
import python_logging
from tkinter import *
from tkinter import ttk, font
import webbrowser
from modules import database

# APPLICATION SETUP
# Set root path to allow retrieval of other files
root = Path(sys.argv[1])

# Setup the public config file
pubCon = configparser.ConfigParser()
pubCon.read(root.child("data_validation_config.cfg").absolute())

# Setup the private config file
priCon = configparser.ConfigParser()
priCon.read(Path(pubCon.get("misc", "private_config")).absolute())

# Setup the logging object
log = python_logging.start(priCon)

# Set up database connection
db = database.setup_db_connection(priCon, log)

# Collect all the relevant data information
programInfo = collect_table_info(pubCon, log)

# Setting up the program window
root = Tk()

# Icon Images
icons = collect_icons()

# Set to maximize
root.wm_state('zoomed')

# Creating Menu Bar
create_menu_bar(root, db, programInfo)

# Create the frame
dashboard = ttk.Frame(root, padding="3 3 12 12")
dashboard.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)

# Start initial program window
create_main_page(root, db, programInfo)

root.mainloop()