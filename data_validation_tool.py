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
def create_menu_bar(root):
    root.option_add("*tearOff", FALSE)

    menubar = Menu(root)

    menuFile = Menu(menubar)
    menuFile.add_command(label="Close", command=root.quit)
    menuAbout = Menu(menubar)
    menubar.add_cascade(menu=menuFile, label="File")
    menubar.add_cascade(menu=menuAbout, label="About")

    root.config(menu=menubar)

def abc_validation(root, dashboard):
    log.debug("Creating the validation window")
    
    # Remove old content
    dashboard.destroy()
    root.title("Study Buffalo Data Validation Tool - ABC DBL Validation")

    abc = ttk.Frame(root, padding="3 3 12 12")

def close_program():
    log.debug("Closing program")

def create_dashboard(root):
    root.title("Study Buffalo Data Validation Tool")

    dashboard = ttk.Frame(root, padding="3 3 12 12")
    dashboard.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)
    dashboard.columnconfigure(0, weight=1)
    dashboard.columnconfigure(0, weight=1)

    titleFont = font.Font(size=16, weight="bold")
    appTitle = ttk.Label(dashboard, text="Study Buffalo Data Validation Tool", font=titleFont)
    appTitle.grid(column=0, row=0, sticky=(N, W), pady=(0,10))

    subFont = font.Font(size=13, underline=True)
    appTitle = ttk.Label(dashboard, text="Choose Data Source:", font=subFont)
    appTitle.grid(column=0, row=1, sticky=(N, W))

    abcButton = ttk.Button(dashboard, 
                           text="ABC iDBL Data Extraction Tool",
                           command=lambda: abc_validation(root, dashboard))
    abcButton.grid(column=0, row=2, sticky=(N, W), pady=5, padx=(15, 0))

    hcButton = ttk.Button(dashboard, text="HC DPD Data Extraction Tool")
    hcButton.grid(column=0, row=3, sticky=(N, W), pady=5, padx=(15, 0))

import sys
from unipath import Path
import configparser
import python_logging
from tkinter import *
from tkinter import ttk, font

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

# Setting up the program window
root = Tk()

# Set to maximize
root.wm_state('zoomed')

# Creating Menu Bar
create_menu_bar(root)

# Start initial program window
create_dashboard(root)

root.mainloop()