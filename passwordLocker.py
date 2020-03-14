#! /usr/bin/env python3

import sys
import pyperclip

passwords={'ghub':'flash','add':'Nashville','f':'Kakashi','last':'Hatake'}
if len(sys.argv)<2:
    print('We will copy the '+sys.argv[1]+' password to clipboard')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)



