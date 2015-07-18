#!/usr/bin/env python3

import DISC

# URLS 
# First go to DCC and save discussion as .html local file
# Locations
# FDRP2: https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-302?init=true
# M1CS: https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-309?init=true

# mobie = 'MOBIE.html'
# fdrp1 = 'STR_FDRP1.html'
fdrp2 = 'STR_FDRP2.html'
m1cs = 'CR173_M1CS.html'

# DISC.get_discussion(mobie, 'mobie.xlsx')
# DISC.get_discussion(fdrp1, 'fdrp1.xlsx')
DISC.get_discussion(fdrp2, 'fdrp2.xlsx')
DISC.get_discussion(m1cs, 'm1cs.xlsx')