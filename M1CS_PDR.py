#!/usr/bin/env python3

# My modules
import DCC
import DISC
import Config as CF

# URLS 
# First go to DCC and save discussion as .html local file
# Locations
url = 'https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-331?init=true'
htmlfile = 'M1CS_PDR.html'
xlsfile = 'M1CS_PDR_ReviewComments.xlsx'

# Call get_discussion
# The htmlfile will be stored in the dccfilepath directory and the
# xlsfile will be stored in the current directory

DISC.get_discussion_rowcol(url, htmlfile, xlsfile, 4, 1)

