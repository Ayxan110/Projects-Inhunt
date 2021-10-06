from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import io
import base64
from urllib.request import urlopen
from flask.globals import request
import requests
from io import BytesIO
import urllib
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


googleURL = "https://www.google.com/search?tbm=isch&as_q="
DRIVER_PATH = 'chromedriver.exe'

HOTEL_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Brochure","Web page","Social Media","Card door key","Paper key card holder","Door hangers","Employee uniform","Manager business suit","Housekeeping staff","Employee badge"]
RESTAURANT_BRAND_ITEMS = ["Outdoor Sign Board","Menu","Reservation sign","Business card","Letterhead","Folder","Envelope","Web page","Social Media","Employee uniform","Manager business suit","Waiter Shirt","Kitchen staff","Cleaning staff","Employee badge","Take away bag"]
HOSPITAL_CLINIC_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Website","Outdoor Advertising","Internal Poster","Internal Signage","Pen pencil","Memo","Notepad","Lab Test result","Medical record","Medical Prescription pad","Brochure about hospital","Calendar","Folder","Test result","Envelope","Social Media","E-mail signature","Emergency vehicle","Corporate car","Staff badge","Employee uniform","Business outfit","Doctor uniform","Nursing outfit","Janitor staff"]
CONSTRUCTION_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","Internal Safety Poster","Internal Signage","Internal Safety Brochure", "Project Catalog","Annual Report","Sustainability Report", "Website", "Social-media","E-mail signature","Presentation templates","Branded Truck","corporate car","construction site fence","Staff badge","Employee uniform","Office manager uniform","construction area worked uniform"]
METALLURGICAL_BRAND_ITEMS  = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","Internal Safety Poster","Internal Signage","Internal Safety Brochure", "Project Catalog","Product catalog","Annual Report","Sustainability Report", "Website", "Social-media","E-mail signature","Presentation templates","staff badge","employee uniform"]
SOCIAL_MEDIA_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","notepad","memo","pen+pencil","internal signage","internal poster","mousepad","website","avatar","icons","font","illustration","notification message template","e-mail signature","presentation template","corporate car","staff badge","phone-number","auto-reply","employee uniform"]
BANK_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about+bank","outdoor advertising","website","social media","e-mail signature","corporate car","staff badge","phone number","auto-reply","employee uniform"]
MORTGAGE_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","calendar","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about","outdoor advertising","website","social media","e-mail signature","corporate car","staff badge","phone number","auto-reply","employee uniform"]
FINANCE_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about+bank","outdoor advertising","website","social media","e-mail signature","corporate car","staff badge","phone number","auto-reply","employee uniform"]
TELECOMMUNICATION_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about+services","outdoor advertising","website","social media","e-mail signature","corporate car","staff badge","phone number","auto-reply","employee uniform"]
MEDIA_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","calendar","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about+bank","outdoor advertising","website","social media","e-mail signature","staff badge","phone number"]
UTILITIES_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about+utilities","outdoor advertising","website","social media","e-mail signature","corporate car","staff badge","phone number","auto-reply","employee uniform"]
RETAIL_ESTATE_BRAND_ITEMS = ["Outdoor Sign Board","Business card","Letterhead","Envelope","Folder","Agenda","notepad","memo","pen+pencil","internal signage","internal poster","brochure+about+retail+estate","outdoor advertising","website","social media","e-mail signature","corporate car","staff badge","phone number","auto-reply","employee uniform"]







def googleFetch( brandName, item):

    brandName = brandName.replace(" ", "+")
    print(brandName)
    item = deleteSpaces(item)

    url = googleURL + brandName + "+" + item 
    print(url)

    #img class="rg_i Q4LuWd" n3VNCb

    # start selenium scraping
    options = Options()
    #options.headless = True
    #options.add_argument("--window-size=1500,600")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 1 
    })
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    #get images
    imageElements = driver.find_elements_by_xpath("//img[contains(@class,'rg_i Q4LuWd')]")
    
    images = []

    try:
        imageElements[1].click()
        time.sleep(2)
        
        image0 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image0:
            print(" img0 alt", im.get_attribute("alt"))
            print(" img0 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass
    
    print('\n')

    try:
        imageElements[1].click()
        time.sleep(2)
        image1 = driver.find_elements_by_xpath("//img[contains(@jsaction,'load:XAeZkd;')]")
        
        for im in image1:
            print(" img1 alt", im.get_attribute("alt"))
            print(" img1 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass
    
    print('\n')

    try:
        imageElements[2].click()
        time.sleep(2)
        image2 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image2:
            print(" img2 alt", im.get_attribute("alt"))
            print(" img2 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass

    print('\n')

    try:
        imageElements[3].click()
        time.sleep(2)
        image3 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image3:
            print(" img3 alt", im.get_attribute("alt"))
            print(" img3 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass

    print('\n')

    try:
        imageElements[4].click()
        time.sleep(2)
        image4 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image4:
            print("img4 alt", im.get_attribute("alt"))
            print(" img4 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass

    try:
        imageElements[5].click()
        time.sleep(2)
        image5 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image5:
            print("img5 alt", im.get_attribute("alt"))
            print(" img5 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass
        
    try:
        imageElements[6].click()
        time.sleep(2)
        image6 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image6:
            print("img6 alt", im.get_attribute("alt"))
            print(" img6 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass

    try:
        imageElements[7].click()
        time.sleep(2)
        image7 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image7:
            print("img7 alt", im.get_attribute("alt"))
            print(" img7 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass

    try:
        imageElements[8].click()
        time.sleep(2)
        image8 = driver.find_elements_by_xpath("//img[contains(@class,'n3VNCb')]")
        
        for im in image8:
            print("img8 alt", im.get_attribute("alt"))
            print(" img8 src", im.get_attribute("src"))
            if "data:" not in im.get_attribute("src"):
                images.append(im.get_attribute("src"))
    except:
        pass
    

    print("\n\n\n\n")

    print("\n****images****\n")

    finalImages = []

    for i in range(5):
        try:
            print(images[i])
            finalImages.append(images[i])
        except:
            finalImages.append("")
            pass
        
    driver.quit()
    return finalImages

def returnItems(industry):

    if(industry == "hotel"):
        return HOTEL_BRAND_ITEMS

    if(industry == "restaurant"):
        return RESTAURANT_BRAND_ITEMS

    if(industry == "hospital"):
        return HOSPITAL_CLINIC_BRAND_ITEMS
        
    if(industry == "construction"):
        return CONSTRUCTION_BRAND_ITEMS

    if(industry == "metallurgical"):
        return METALLURGICAL_BRAND_ITEMS

    if(industry == "social_media"):
        return SOCIAL_MEDIA_BRAND_ITEMS
        
    if(industry == "bank"):
        return BANK_BRAND_ITEMS
    
    if(industry == "mortgage"):
        return MORTGAGE_BRAND_ITEMS
    
    if(industry == "finance"):
        return FINANCE_BRAND_ITEMS
    
    if(industry == "telecommunication"):
        return TELECOMMUNICATION_BRAND_ITEMS
    
    if(industry == "media"):
        return MEDIA_BRAND_ITEMS

    if(industry == "utility"):
        return UTILITIES_BRAND_ITEMS
    
    if(industry == "retail estate"):
        return RETAIL_ESTATE_BRAND_ITEMS


def bingFetch(BRAND_NAME, ITEM):

    BRAND_NAME = deleteSpaces(BRAND_NAME)
    ITEM = deleteSpaces(ITEM)
    
    image_list = []

    resultUrls = []
    URL = "https://www.bing.com/images/search?q=" + BRAND_NAME + "+"+ITEM

    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

    html = session.get(URL).content
    soup = BeautifulSoup(html, 'html.parser')

    allImgTags = soup.findAll('img')
  
    for img in allImgTags:
        try:
            print(img["src"])
            if "pid=1.7" in img["src"] and not "moderate" in img["src"]:
                image_list.append(img["src"])
        except:
            pass

    return image_list


def deleteSpaces(text):
    return text.replace(" ", "+")

def googleFetch2(brandName, item):

    print(brandName)

    url = googleURL + brandName + "+" + item 
    print(url)

    options = Options()
    options.headless = True
    #options.add_argument("--window-size=1500,600")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(url)

    #get images
    imageElements = driver.find_elements_by_xpath("//img[contains(@class,'rg_i Q4LuWd')]")

    imageElements[0].click()
    time.sleep(5)
    div = driver.find_elements_by_xpath("//img[contains(@jsname,'HiaYvf')]")
    #print(div.get_attribute("outerHTML"))
    print(len(div))

    for d in div:
        print(d.get_attribute("outerHTML"))
    
    print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/")
    imageElements[1].click()
    time.sleep(5)
    div = driver.find_elements_by_xpath("//img[contains(@jsname,'HiaYvf')]")
    #print(div.get_attribute("outerHTML"))
    print(len(div))

    print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/")
    imageElements[2].click()
    time.sleep(5)
    div = driver.find_elements_by_xpath("//img[contains(@jsname,'HiaYvf')]")
    #print(div.get_attribute("outerHTML"))
    print(len(div))

    for d in div:
        print(d.get_attribute("outerHTML"))
    #imageElements[1].click()
    #time.sleep(5)
    #div = driver.find_element_by_xpath(".//div[contains(@class,'v4dQwb')]")
    #print(div.get_attribute("outerHTML"))
    driver.quit()

def startDriver():
    options = Options()
    options.headless = True
    #options.add_argument("--window-size=1500,600")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    return driver

def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls
    
def main():

    BRAND_NAME = "AT and T"
    ITEM = "business card"

    #print(bingFetch(deleteSpaces(BRAND_NAME), deleteSpaces(ITEM)))
    
    googleFetch(deleteSpaces(BRAND_NAME), deleteSpaces(ITEM))

    #print(fetch_image_urls("facebook uniform", 5 , startDriver()))

if __name__ == "__main__":
    main()