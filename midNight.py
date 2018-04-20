import requests
import os
import logging

log = logging.getLogger('theLogger')
log.debug('Start of program')#logging the start of the program

response = requests.get('http://www.gutenberg.org/files/11/11-0.txt')

bookFile = response.text

print(len(bookFile))

#Writting the  book to a file
bookSave = open("TheBook.txt","w+",encoding="utf-8")
bookSave.write(bookFile)
bookSave.close()

log = logging.getLogger('theLogger')


n = 1000
assert (n == 1000),""#an assertion to make sure n is always 1000
parts = [bookFile[i:i+ int(n)] for i in range(0, len(bookFile), int(n))]


print('This has '+ str(len(parts)) +' pages.')

pages = 0
while pages < len(parts):
 try:#Prevents the inputs of things other than p,n or numbers
    os.system('cls')
    print('======================================================================')
    print(parts[pages] + '\n\n')#prints a chunk of text
    answer = input('Page ' + str(pages + 1) + '\n\n Enter [P]revious [N]ext or Page#\n')
    if (answer.lower() == 'p'):#moves back one page
        pages += -1
        log.debug("p was typed")#logging randon stuff
    elif (answer.lower() == 'n'):#moves forward one page
        pages += 1
        log.debug("n was typed")#logging randon stuff
    else:#lets user put a page number
        pages = int(answer) - 1
        log.debug('a number '+ answer +' was typed')#logging randon stuff
 except ValueError:
    print('VALID INPUTS ARE P,N OR A NUMBER')

log.debug('End of program')

 

    