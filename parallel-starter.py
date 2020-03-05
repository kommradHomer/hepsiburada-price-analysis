import logging
from datetime import datetime
import sys
import time
from threading import Thread
import os
import parallel_analyzer

CONCURRENCY_LEVEL=4



logging.basicConfig(level=logging.INFO,format='%(asctime)-15s-%(levelname)s:%(pathname)s:%(lineno)s %(message)s')

logger=logging.getLogger()

logger.info("start")

urls_path=sys.argv[1]

dateTag=datetime.now().strftime("%Y%m%d_%H%M%S")


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
        t1=Thread(target=parallel_analyzer.run, args=(dateTag,i))
        t1.start()
        threadss.append(t1)

    for t in threadss:
        t.join()


    logger.info("DONE WITH WAITING ALL THREADS")

    logger.info("combining outputs")

    with open("output/analysis-"+dateTag+".csv", 'w') as outfile:
        for i in range(CONCURRENCY_LEVEL):
            with open("output/"+dateTag+"_p"+str(i),"r") as infile:
                for line in infile:
                    outfile.write(line)

    logger.info("DONE COMBINING FILES")



        
    
        



        


