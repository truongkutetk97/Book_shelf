import requests
import sys
from datetime import datetime  
from datetime import timedelta 
import re
import numpy
import time
import csv
import pandas
from pandas import DataFrame
from bs4 import BeautifulSoup

argv = "python"
print("Searhing for: {}  ".format(argv))

sess = requests.Session()
sess_2 = requests.Session()

count_book = 0
list_link_book = []
f = open("data.txt", "w")
total_isbn_valid = 0
total_isbn_invalid = 0

# with open("data.csv", mode = 'w') as file:
#     writer = csv.writer( file, delimiter=';', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
#     for page_index in range(1,11): 
#         payload = {'page': page_index}
#         response = sess.get('https://1lib.limited/s/{}'.format(argv) ,params=payload)
#         if response.status_code != 200:
#             continue
#         links = re.findall('<a href="(.*?)">(.*?)</a>', str(response.content))
#         for books in links :
#             str_book = str(books)
#             book_pos_start =  str_book.find("/book/")
#             if  book_pos_start >0 :
#                 if str_book.find("https://") > 0:
#                     continue
#                 if  str_book.find("book-no-cover") > 0 :
#                     continue
#                 book_pos_end = str_book.find(" ", book_pos_start)
#                 list_link_book.append("https://1lib.limited" + str_book[book_pos_start:book_pos_end-1] +" ")
#                 f.write("Book [{}] = {} \n".format(count_book, str_book  ))
#                 divided_by_quote_mask = str_book.split("'")
#                 #request isbn:
#                 response_2 = sess_2.get("https://1lib.limited" + str_book[book_pos_start:book_pos_end-1])
#                 soup = BeautifulSoup(response_2.content, 'html.parser')
#                 isbn_box = soup.find("div", attrs={"class":"bookProperty property_isbn 13"})
#                 if isbn_box != None:
#                     isbn = isbn_box.text
#                     isbn = isbn[isbn.find(":")+2:]  
#                     total_isbn_valid +=1
#                 else : 
#                     total_isbn_invalid +=1
#                     isbn = "ISBN_NULL_"+str(total_isbn_invalid)
#                 writer.writerow([count_book,isbn , list_link_book[count_book] ,divided_by_quote_mask[3] ])

#                 count_book += 1
#         f.write("  End page \n")
#         time.sleep(1)

with open("data.csv", mode = 'w') as file:
    writer = csv.writer( file, delimiter=';', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    for page_index in range(1,11): 
        payload = {'page': page_index}
        response = sess.get('https://1lib.limited/s/{}'.format(argv) ,params=payload)
        if response.status_code != 200:
            continue
        links = re.findall('<a href="(.*?)">(.*?)</a>', str(response.content))
        for books in links :
            str_book = str(books)
            book_pos_start =  str_book.find("/book/")
            if  book_pos_start >0 :
                if str_book.find("https://") > 0:
                    continue
                if  str_book.find("book-no-cover") > 0 :
                    continue
                book_pos_end = str_book.find(" ", book_pos_start)
                list_link_book.append("https://1lib.limited" + str_book[book_pos_start:book_pos_end-1] +" ")
                f.write("Book [{}] = {} \n".format(count_book, str_book  ))
                divided_by_quote_mask = str_book.split("'")
                #request isbn:
                response_2 = sess_2.get("https://1lib.limited" + str_book[book_pos_start:book_pos_end-1])
                soup = BeautifulSoup(response_2.content, 'html.parser')
                isbn_box = soup.find("div", attrs={"class":"bookProperty property_isbn 13"})
                if isbn_box != None:
                    isbn = isbn_box.text
                    isbn = isbn[isbn.find(":")+2:]  
                    total_isbn_valid +=1
                else : 
                    total_isbn_invalid +=1
                    isbn = "ISBN_NULL_"+str(total_isbn_invalid)
                writer.writerow([count_book,isbn , list_link_book[count_book] ,divided_by_quote_mask[3] ])

                count_book += 1
        f.write("  End page \n")
        time.sleep(1)




f.close()
print(response.url)
print(" Total book in page: {} ".format(count_book))

# print(" Total book in page: {} ".format(count_book_response))

# print(response.text )
