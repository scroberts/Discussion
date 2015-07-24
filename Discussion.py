#!/usr/bin/env python3

import DISC

# URLS 
# First go to DCC and save discussion as .html local file
# Locations
# FDRP2: https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-302?init=true
# M1CS: https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-309?init=true
# Test: https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-319

# DISC.get_discussion('MOBIE.html', 'mobie.xlsx')
# DISC.get_discussion('STR_FDRP1.html', 'fdrp1.xlsx')

DISC.get_discussion('CR173_M1CS.html', 'm1cs.xlsx')
DISC.get_discussion('STR_FDRP2.html', 'fdrp2.xlsx')
DISC.get_discussion('Scott_test.html', 'scott_test.xlsx')
