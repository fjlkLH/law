from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import  Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
 
driver = webdriver.Firefox()

#url_list=[]
urllist2=[] #存储所有地方性法规地址的列表
titel_list=[]#存储所有地方性法规题目的列表
#zidian_list=[]#存储所有地方性法规信息的字典的列表
for count in range(1,240):      #将所有地方性法规信息的字典存储在zidian_list[]中
    ur = f"https://flk.npc.gov.cn/api/?type=&zdjg=4028814858b9b8e50158bee5863c0091%264028814858b9b8e50158bee9a3aa0095&zdjg=4028814858b9b8e50158beeaa1b70099%264028814858b9b8e50158beeb4757009d&zdjg=4028814858b9b8e50158beefec0d00b1%264028814858b9b8e50158bef0947c00b5&zdjg=4028814858b9b8e50158bef3797c00c1%264028814858b9b8e50158bef4210100c5&zdjg=4028814858b9b8e50158bef53e9e00c9%264028814858b9b8e50158bef5d32f00cd&zdjg=4028814858b9b8e50158bef6eec900d1%264028814858b9b8e50158bef7e82500d5&zdjg=4028814858b9b8e50158bef9249700d9%264028814858b9b8e50158bef9d8b900dd&searchType=title%3Bvague%3B1&sortTr=f_bbrq_s%3Bdesc&gbrqStart=&gbrqEnd=&sxrqStart=&sxrqEnd=&page={count}&size=10&_=1712890827560"
    #url_list.append(ur)
    resp = driver.get(ur)
    ex=driver.find_element(By.ID,"content").text
    
    data = json.loads(ex)#将text转为字典
    value1 = data.get("result")
    value2 = value1.get("data")
    for i in range(10):
        urllist2.append(value2[i].get("url")[2:])
        titel_list.append(value2[i].get("title"))
    
newRUL_list=[]
for url in urllist2:
    newRUL_list.append('https://flk.npc.gov.cn/' + url)

for i in range(len(newRUL_list)):
    driver.get(newRUL_list[i])
    download_button = driver.find_element(By.ID,"downLoadFile")
    download_button.click()
    time.sleep(random.randint(3,4))




    




#for url in url_list:
