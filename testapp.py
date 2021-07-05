from selenium import webdriver
import time

import random

driver =webdriver.Firefox()

url="https://www.dr.com.tr/kategori/Kitap/Bilim/grupno=00052#/page="

pagecount =1
books=[]

while pagecount<=7:
    randomPage =random.randint(1,41)
    newUrl=url + str(randomPage)
    driver.get(newUrl)

    elements =driver.find_elements_by_css_selector("h3.ellipsis")

    for element in elements:
        books.append(element.text)
    time.sleep(5)    
    pagecount +=1

with open("books.txt","w",encoding="utf-8") as file:
    for i in books:
        file.write("**************\n")
        file.write("Book Name: " + i + "\n")
    


