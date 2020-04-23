#! /usr/bin/env python3
#((\d{3})|(\(\d{3}\)))?(\s|-)\d{3}-\d{4}(((ext(\.)?\s)|x)(\d+))?


import re, pyperclip

phonePattern =re.compile('''
#457-567-3884, 555-0000,(415) 555-0000, 555-0000 ext 12345,555-0000 ext. 12345,555-0000 x12345

(
((\d{3})|(\(\d{3}\)))?           #area code(optional)
(\s|-)                           #first separator
\d{3}                            #first 3 digits
-                                #separator
\d{4}                            #last 4 digits
(((ext(\.)?\s)|x)                #extension word part(optional)
(\d+))?
)                         #extension number part(optional)                      

''', re.VERBOSE)

mailPattern =re.compile('''
#some.+_thing@xyz.com

[\w.+]+@[\w]+.[\w]{3}


''',re.VERBOSE)

text = pyperclip.paste()

Numbers = phonePattern.findall(text)
#print(Numbers)
Addresses = mailPattern.findall(text)
#print(Addresses)



newList=[]
for i in Numbers:
    newList.append(i[0])
    

result='\n'.join(newList)+'\n'+'\n'+'\n'.join(Addresses)
print(result)
pyperclip.copy(result)

#eachLine = '\n'.join(newList)+'n'.join
