
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys
import time

print("ggg")


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path="/home/yigit/Downloads/chromedriver",chrome_options=option)


isQuery= True if "?" in sys.argv[1] else False

page=0

urlsArr=[]

lastPageHit=False

with open("output/"+str(time.time())+"_urls.out","a") as urls:
    while True:
        if lastPageHit:
            break

        page=page + 1

        pageStr="&sayfa="+str(page) if isQuery else "?sayfa="+str(page)


        browser.get(sys.argv[1]+pageStr)
    
        time.sleep(10)

        all_product_as=browser.find_elements_by_xpath('//div[@class="box product no-hover" or  @class="box product"]/a')

        print(len(all_product_as))

        for a in all_product_as:
            if a.get_attribute("href") in urlsArr:
                lastPageHit=True
                break
            print(a.get_attribute("href"))
            urls.write(a.get_attribute("href")+"\n")
            urlsArr.append(a.get_attribute("href"))



browser.quit()
sys.exit(0)

