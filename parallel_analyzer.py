import logging
from datetime import datetime
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import sys
import time
import numpy as np

def run(dateTag,number):

    logging.basicConfig(level=logging.INFO,format='%(asctime)-15s-%(levelname)s:%(pathname)s:%(lineno)s %(message)s')

    logger=logging.getLogger()

    logger.info("start")

    CHROME_DRIVER_PATH="/home/XXXXXXXXXXX/Downloads/chromedriver"

    option = webdriver.ChromeOptions()
    option.add_argument(" — incognito")

    browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,chrome_options=option)

    urls_path="output/parallel_inputs/"+dateTag+"_p"+str(number)

    outputFileName=dateTag+"_p"+str(number)


    logger.info("OUTPUT_FILE:"+outputFileName)


    with open(urls_path,"r") as urls ,open("output/"+outputFileName,"a") as outputcsv:
    
        outputcsv.write("median;mean;mean_pct;median_pct;URL;prices\n")
        for url in urls:
            url=url.strip()

            if url.startswith("#"):
                continue

            logger.info(url)
        
            browser.get(url)
    
            time.sleep(10)

            a_tumu=browser.find_elements_by_xpath('//div[@class="merchantList"]/div/div/a')

            if len(a_tumu)==0:
                continue

            logger.debug(len(a_tumu))

            logger.debug(a_tumu[0].text)

            try:
                a_tumu[0].click()
            except :
                logger.warn("cant click!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                continue

            tds=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//td[@class="productPrice"]')

            logger.debug(len(tds))


            span1=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//span[@class="price product-price"]')

            span2=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//span[@class="not-span"]')

            span3=browser.find_elements_by_xpath('//div[@id="tabMerchant"]//table[@id="merchant-list"]/tbody//span[@class="price product-price leftFit"]')

            logger.debug(len(span1))
            logger.debug(len(span2))
            logger.debug(len(span3))

            prices=[]

            for s in span1:
                logger.debug(s.text)
                prices.append(int(s.text.split(",")[0].replace(".","")))
            

            for s in span2:
                logger.debug(s.text)
                prices.append(int(s.text.split(",")[0].replace(".","")))

            for s in span3:
                logger.debug(s.text)
                prices.append(int(s.text.split(",")[0].replace(".","")))

            logger.info(prices)

            logger.debug(str(np.median(prices)))
            logger.debug(str(np.mean(prices)))
            logger.debug(str(np.nanmin(prices)))
            logger.debug(str(np.nanmin(prices)*100 / np.mean(prices)))
            logger.debug(str(np.nanmin(prices)*100 / np.median(prices)))

            row=str(np.median(prices))+";"+str(np.mean(prices))+";"+str(np.nanmin(prices)*100 / np.mean(prices))+";"+str(np.nanmin(prices)*100 / np.median(prices))+";"+url+";"+str(prices)+"\n"

            logger.info(row)

            outputcsv.write(row)

        

    browser.quit()

