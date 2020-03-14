#! /usr/bin/env python3

import sys
import pyperclip

passwords={'ghub':'Cherrycool@1995','add':'14815 Avery Ranch','f':'Hari Charan','last':'gurramkonda','cmail':'hari_charan.gurramkonda@students.tamuk.edu','sevis':'Cherrycool@2020','1789':'Mementomori','mail':'charan.harry5@gmail.com'}

if len(sys.argv)<2:
    print('We will copy the '+sys.argv[1]+' password to clipboard')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)



