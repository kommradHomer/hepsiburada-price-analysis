import logging
from datetime import datetime
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys
import time

logging.basicConfig(level=logging.INFO,format='%(asctime)-15s-%(levelname)s:%(pathname)s:%(lineno)s %(message)s')

logger=logging.getLogger()

logger.info("start")


CHROME_DRIVER_PATH="/home/yigit/Downloads/chromedriver"
FIREFOX_DRIVER_PATH="/home/yigit/Downloads/geckodriver"

##option = webdriver.ChromeOptions()
##option.add_argument(" — incognito")


#browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,chrome_options=option)
browser = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)


isQuery= True if "?" in sys.argv[1] else False

page=0

urlsArr=[]

lastPageHit=False

dateTag=datetime.now().strftime("%Y%m%d_%H%M%S")


with open("output/urls_"+dateTag+".out","a") as urls:
    while True:
        if lastPageHit:
            break

        page=page + 1

        pageStr="&sayfa="+str(page) if isQuery else "?sayfa="+str(page)


        browser.get(sys.argv[1]+pageStr)
    
        time.sleep(10)
        print("done with sleeping")

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

