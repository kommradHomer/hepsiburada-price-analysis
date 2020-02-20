
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys
import time
import numpy as np

print("ggg")

CHROME_DRIVER_PATH="/home/XXXXXXXXXXXXXXXXXXX/Downloads/chromedriver"

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,chrome_options=option)

urls_path=sys.argv[1]

DEBUG_MODE=False

def logg(s):
    if DEBUG_MODE:
        print(str(s))

with open(urls_path,"r") as urls ,open("output/"+str(time.time())+"analyze.out","a") as outputcsv:
    
    outputcsv.write("median;mean;mean_pct;median_pct;URL;prices\n")
    for url in urls:
        url=url.strip()

        if url.startswith("#"):
            continue

        logg(url)
        
        browser.get(url)
    
        time.sleep(10)

        a_tumu=browser.find_elements_by_xpath('//div[@class="merchantList"]/div/div/a')

        if len(a_tumu)==0:
            continue

        logg(len(a_tumu))

        logg(a_tumu[0].text)

        try:
            a_tumu[0].click()
        except :
            logg("cant click!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            continue

        tds=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//td[@class="productPrice"]')

        logg(len(tds))


        span1=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//span[@class="price product-price"]')

        span2=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//span[@class="not-span"]')

        span3=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//span[@class="price product-price leftFit"]')

        logg(len(span1))
        logg(len(span2))
        logg(len(span3))

        prices=[]

        for s in span1:
            logg(s.text)
            prices.append(int(s.text.split(",")[0].replace(".","")))
            

        for s in span2:
            logg(s.text)
            prices.append(int(s.text.split(",")[0].replace(".","")))

        for s in span3:
            logg(s.text)
            prices.append(int(s.text.split(",")[0].replace(".","")))

        logg(prices)

        print(str(np.median(prices)))
        print(str(np.mean(prices)))
        print(str(np.nanmin(prices)))
        print(str(np.nanmin(prices)*100 / np.mean(prices)))
        print(str(np.nanmin(prices)*100 / np.median(prices)))

        outputcsv.write(str(np.median(prices))+";"+str(np.mean(prices))+";"+str(np.nanmin(prices)*100 / np.mean(prices))+";"+str(np.nanmin(prices)*100 / np.median(prices))+";"+url+";"+str(prices)+"\n")


        

browser.quit()

