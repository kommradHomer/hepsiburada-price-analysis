
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


page=0

with open("output/"+str(time.time())+"_urls.out","a") as urls:
    while page < 21:
        page=page + 1
        browser.get(sys.argv[1]+"?sayfa="+str(page))
    
        time.sleep(10)

        all_product_as=browser.find_elements_by_xpath('//div[@class="box product no-hover" or  @class="box product"]/a')

        print(len(all_product_as))

        for a in all_product_as:
            print(a.get_attribute("href"))
            urls.write(a.get_attribute("href")+"\n")




browser.quit()
sys.exit(0)

