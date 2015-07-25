#!/usr/bin/env python3

import DISC

# Prototype for writing discussion group spreadsheets.
# Make a new copy of this file for each discussion board

# Enter values for XXX and NAME below
url = 'https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-XXX'
htmlfile = 'NAME.html'
xlsfile = 'NAME.xlsx'

# Call get_discussion
# The htmlfile will be stored in the dccfilepath directory and the
# xlsfile will be stored in the current directory

DISC.get_discussion(url, htmlfile, xlsfile)