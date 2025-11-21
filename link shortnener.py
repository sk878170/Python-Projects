""""What the program does? 

1. Shortening Links
- You have to give your big link in the terminal
- Program will use tinyurl server for shortening the link without using any browser
- Shortened link will pass by print() function

2. Extracting Original Links
- You have to give a shortened link in the terminal
- Program will extract the original URL from the shortened link
- Original link will pass by print() function"""

import pyshorteners
from urllib.request import urlopen

def link_Shortener(link):
    shortener=pyshorteners.Shortener()
    shortened_link=shortener.tinyurl.short(link)  # This process will shorten the link

    print('\t[+] Real Link: ' + link)
    print('\t[+] Shortened Link: ' + shortened_link)

def link_opener(link):
    shortened_url=urlopen(link)
    Real_link=shortened_url.geturl()

    print('\t[+] Shortened Link: ' + link)
    print('\t[+] Real Link: ' + Real_link)

    
while True:
    if __name__=='__main__':
        num=input("Enter your choice\n1.Link Shortening\n2.Extract\n")
        link=input("Enter the link:")

        if(num=='1'):
            link_Shortener(link)
        else:
            link_opener(link)
