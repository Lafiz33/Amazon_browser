# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:05:29 2019

@author: Lafiz33
"""
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import time
print("*"*60)
print("Auto_amazon_Browser_v1.0.0_By__Lafiz33 \nthis is a test program.. ")
print("*"*60)

url= "https://www.amazon.com/"

search_item_list=["dog food", "cat food", "shoes", "belt", "chips", "drone", "t-shirt", "tv", "fridge", "camera", "puzzle", "chocolate", "sensors", "mug","laptop"]
max_iteration= (len(search_item_list))*7

def make_url_amazon(url, page_num):
    page="page="
    count=url.count("&")
    str2= url.split("&")
#    sign="&"
    full_url=str2[0]+"&"+page+str(i)+"&"
    for j in range(1,count+1):
        if(j!=count):
            full_url=full_url+str2[j]+"&"
        else:
            full_url=full_url+str2[j]
#    print(full_url)
    
    return full_url
    
#    
#for i in range (1,4):
#    new_url=make_url_amazon(str1, i)

while(True):
    try:    
        page_counter=1
        page_num=int(input("how many pages you want? Max Limit: "+str(max_iteration)+" \n\r"))
        
        print("Opening Web Browser...")
        dir_now=os.path.dirname(os.path.abspath(__file__))
        browser=webdriver.Chrome(executable_path=dir_now+'\\chromedriver.exe')
            
        print("Creating File...")
        filename = "results.txt"
        f = open(filename, "w")
            
            
        print("Writing Headers...")
        headers= "Starting Loading Time Count For Amazon page :"
        f.write(headers+ "\n")
            
        
        for items in search_item_list:
            flag = True
            timer1 = []
#            print(str(items))
            searched_url=""
            
            for i in range(1,8) :
                start_time = time()
                browser.get(url)
                end_time = time()
                
                temp_time=round(end_time-start_time,5)
                timer1.append(float(temp_time))
                
                str1="page number :"+str(page_counter)+" time took to load : " +str(round(end_time-start_time,5)) +"s"
                print(str1)            
                            
                print("searching for "+str(items))
                if (flag):
                    elem = browser.find_element_by_id("twotabsearchtextbox")
                    elem.clear()
                    elem.send_keys(str(items))
                    elem.send_keys(Keys.RETURN)
                    searched_url=str(browser.current_url)
                    flag = False
                    
#                print("Page found.. \nmaking soup")
#                soup=BeautifulSoup(browser.page_source, "html.parser")
            
                print("taking notes")
                searched_url
                f.write(str1+"\n")
                if(page_counter>=page_num):
                    break
                else:
                    page_counter=page_counter+1
                    
                    print("going to next page...")
                    nextPage = make_url_amazon(searched_url,i)
                    url=nextPage
                    print("found next page")
                    
            if(page_counter>=page_num):
                 break                
        if(page_counter>=page_num):
            
            time_sum = sum(timer1)
            avg = round(time_sum/page_counter, 5)
            time_max = max(timer1)
            time_min = min(timer1)
            
            print("writing results..")
            f.write("total number of page :"+str(page_counter)+"\n"+"minimum loading time: "+str(time_min)+" maximum loading time: "+str(time_max)+" average time: "+str(avg)+"\n")
        
            break
            
        
    except:
        print("Something went wrong.. \nSorry.. \nTry again :(")
    finally:
        print("Closing file...")
        f.close()
        print("have fun.. :)")
        if(input("exit browser? y/n \n")=="y"):
            print("exiting..\nthank you..")
            browser.close();
            break
        

    
        




