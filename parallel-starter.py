import logging
from datetime import datetime
import sys
import time
from threading import Thread
import os

CONCURRENCY_LEVEL=2

logging.basicConfig(level=logging.INFO,format='%(asctime)-15s-%(levelname)s:%(pathname)s:%(lineno)s %(message)s')

logger=logging.getLogger()

logger.info("start")

urls_path=sys.argv[1]

dateTag=datetime.now().strftime("%Y%m%d_%H%M%S")

def runSingleAnalyzer(number,dateTag):
    os.system("parallel-analyzer.py "+sys.argv[0]+" "+sys.argv[1])


logger.info("OUTPUT_FILE:"+dateTag)

with open(urls_path,"r") as urls:
   
    allUrls=urls.readlines()
    
    logger.info(len(allUrls))

    logger.info("splitting urls for concurrency")

    for i in range(0,CONCURRENCY_LEVEL):
        temp=[]
        j=i
        while j < len(allUrls):
            temp.append(allUrls[j].strip())
            j=j+CONCURRENCY_LEVEL

        f=open("output/parallel_inputs/"+dateTag+"_p"+str(i),"w")

        for t in temp:
            f.write(t+"\n")

        f.close()

    threadss=[]

    for i in range(CONCURRENCY_LEVEL):
        t1=Thread(target=runSingleAnalyzer, args=(dateTag,i))
        t1.start()
        t1.join()
        
    
        



        


