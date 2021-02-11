
#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    Address = ' '.join(sys.argv[1:])
   
else:
    Address = pyperclip.paste()
    if len(Address) == 0:
        raise Exception ('Please type in an address or postal code after \'mapit\'')
            
            

webbrowser.open('https://www.google.com/maps/search/' + Address)
    

    


    




