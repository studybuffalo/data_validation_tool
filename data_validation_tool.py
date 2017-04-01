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
    
    # Font Styles and Label Styles
    fontTitle = font.Font(size=16, weight="bold")
    fontH1 = font.Font(size=13, weight="bold")
    fontH2 = font.Font(size=13, slant="italic")
    fontStats = font.Font(size=13)

    # Create the frame
    dashboard = ttk.Frame(root, padding="3 3 12 12")
    dashboard.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)
    dashboard.columnconfigure(0, weight=1)
    dashboard.columnconfigure(0, weight=1)

    # Create a title
    appTitle = ttk.Label(dashboard, text="Study Buffalo Data Validation Tool", font=fontTitle)
    appTitle.grid(column=0, row=0, sticky=(N, W), pady=(0,10), columnspan=5)

    horSep1 = ttk.Separator(dashboard,orient=HORIZONTAL)
    horSep1.grid(column=0, row=2, sticky=(E, W), columnspan=5, pady=5)

    # Create the ABC iDBL options
    # Title
    abcLabel = ttk.Label(dashboard, text="ABC iDBL Data Extraction Tool", font=fontH1)
    abcLabel.grid(column=0, row=3, sticky=(N, E), pady=5, padx=10)

    # Stats Label
    abcStat = ttk.Label(dashboard, text="Current Stats", font=fontH2)
    abcStat.grid(column=0, row=4, sticky=(N, E), pady=5, padx=10)

    # BSRF Button
    abcButBSRF = ttk.Button(dashboard, text="BSRF Substitutions")
    abcButBSRF.grid(column=1, row=3, sticky=N, pady=5, padx=10)

    abcStatBSRFEntry = 0
    
    if abcStatBSRFEntry > 1:
        abcStatBSRFText = "%s entries" % abcStatBSRFEntry
        abcStatBSRFCol = "red"
    elif abcStatBSRFEntry == 1:
        abcStatBSRFText = "%s entry" % abcStatBSRFEntry
        abcStatBSRFCol = "red"
    else:
        abcStatBSRFText = "0 entries"
        abcStatBSRFCol = "green"

    abcStatBSRF = ttk.Label(dashboard, text=abcStatBSRFText, font=fontStats, 
                            foreground=abcStatBSRFCol)
    abcStatBSRF.grid(column=1, row=4, sticky=N, pady=5, padx=10)

    # Generic Name Button
    abcButGen = ttk.Button(dashboard, text="Generic Name Substitutions")
    abcButGen.grid(column=2, row=3, sticky=N, pady=5, padx=10)

    abcStatGenEntry = 0
    
    if abcStatGenEntry > 1:
        abcStatGenText = "%s entries" % abcStatGenEntry
        abcStatGenCol = "red"
    elif abcStatGenEntry == 1:
        abcStatGenText = "%s entry" % abcStatGenEntry
        abcStatGenCol = "red"
    else:
        abcStatGenText = "0 entries"
        abcStatGenCol = "green"

    abcStatGen = ttk.Label(dashboard, text=abcStatGenText, font=fontStats,
                           foreground=abcStatGenCol)
    abcStatGen.grid(column=2, row=4, sticky=N, pady=5, padx=10)

    # Manufacturer Button
    abcButManuf = ttk.Button(dashboard, text="Manufacturer Substitutions")
    abcButManuf.grid(column=3, row=3, sticky=N, pady=5, padx=10)
    
    abcStatManufEntry = 0
    
    if abcStatManufEntry > 1:
        abcStatManufText = "%s entries" % abcStatManufEntry
        abcStatManufCol = "red"
    elif abcStatManufEntry == 1:
        abcStatManufText = "%s entry" % abcStatManufEntry
        abcStatManufCol = "red"
    else:
        abcStatManufText = "0 entries"
        abcStatManufCol = "green"

    abcStatManuf = ttk.Label(dashboard, text=abcStatManufText, font=fontStats,
                             foreground=abcStatManufCol)
    abcStatManuf.grid(column=3, row=4, sticky=N, pady=5, padx=10)

    # PTC Button
    abcButPTC = ttk.Button(dashboard, text="PTC Substitutions")
    abcButPTC.grid(column=4, row=3, sticky=N, pady=5, padx=10)

    abcStatPTCEntry = 0
    
    if abcStatPTCEntry > 1:
        abcStatPTCText = "%s entries" % abcStatPTCEntry
        abcStatPTCCol = "red"
    elif abcStatPTCEntry == 1:
        abcStatPTCText = "%s entry" % abcStatPTCEntry
        abcStatPTCCol = "red"
    else:
        abcStatPTCText = "0 entries"
        abcStatPTCCol = "green"

    abcStatPTC = ttk.Label(dashboard, text=abcStatPTCText, font=fontStats,
                           foreground=abcStatPTCCol)
    abcStatPTC.grid(column=4, row=4, sticky=N, pady=5, padx=10)
    
    horSep2 = ttk.Separator(dashboard,orient=HORIZONTAL)
    horSep2.grid(column=0, row=5, sticky=(E, W), columnspan=5, pady=5)

    # Create the HC DPD options
    # Title
    hcButton = ttk.Label(dashboard, text="HC DPD Data Extraction Tool", font=fontH1)
    hcButton.grid(column=0, row=6, sticky=(N, E), pady=5, padx=10)

    # Stats label
    hcStat = ttk.Label(dashboard, text="Current Stats", font=fontH2)
    hcStat.grid(column=0, row=7, sticky=(N, E), pady=5, padx=10)

    # In development
    hcTemp = ttk.Button(dashboard, text="IN DEVELOPMENT", state=DISABLED)
    hcTemp.grid(column=1, row=6, sticky=(N, W), pady=5, padx=10)


import sys
from unipath import Path
import configparser
import python_logging
from tkinter import *
from tkinter import ttk, font
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

# Setting up the program window
root = Tk()

# Set to maximize
root.wm_state('zoomed')

# Creating Menu Bar
create_menu_bar(root)

# Start initial program window
create_dashboard(root)

root.mainloop()