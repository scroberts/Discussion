#!/usr/bin/env python3

# My modules
import DCC
import DISC
import config as cf

# URLS 
# First go to DCC and save discussion as .html local file
# Locations
url = 'https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-309?init=true'
htmlfile = 'CR173_M1CS.html'
xlsfile = 'm1cs.xlsx'

# Call get_discussion
# The htmlfile will be stored in the dccfilepath directory and the
# xlsfile will be stored in the current directory

DISC.get_discussion(url, htmlfile, xlsfile)

