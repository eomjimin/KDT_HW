import time
from selenium import webdriver
from urllib.request import Request, urlopen
from selenium.webdriver.common.by import By ## 검색의 상수화
import os
def bana():
    driver = webdriver.Chrome()
    url = 'https://www.banapresso.com/store'
    driver.get(url)
    time.sleep(3)

    nameList = []
    addList = []
    iNameList = []

    imgList = []

    area_xpath = '/html/body/div/div/div/div/article/article/div/div[1]/div[2]'

    area = driver.find_element(By.XPATH, area_xpath)
    for i in range(3):
        if(i < 2):
            for j in range (1,6):
                button = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/article/article/div/div[1]/div[3]/ul/li[{j}]/a").click()
                div = driver.find_elements(By.CLASS_NAME, "store_name_map")
                for d in div:
                    nameList.append(d.text.strip().split('\n')[1])
                    addList.append(d.text.strip().split('\n')[2])
                img = area.find_elements(By.CLASS_NAME, "store_photo")
                for k in img:
                    url = k.find_element(By.TAG_NAME, "img").get_attribute("src")
                    imgList.append(url)
            nextbtn = driver.find_element(By.XPATH, "/html/body/div/div/div/div/article/article/div/div[1]/div[3]/span[2]/a").click()
            time.sleep(1.5)

        else:
            for j in range(1,4):
                button = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/article/article/div/div[1]/div[3]/ul/li[{j}]/a").click()
                div = driver.find_elements(By.CLASS_NAME, "store_name_map")
                for d in div:
                    nameList.append(d.text.strip().split('\n')[1])
                    addList.append(d.text.strip().split('\n')[2])
                img = area.find_elements(By.CLASS_NAME, "store_photo")
                for k in img:
                    url = k.find_element(By.TAG_NAME, "img").get_attribute("src")
                    imgList.append(url)

    if not os.path.exists("banaIMG"):
        os.mkdir("banaIMG")

    for i in range(len(imgList)):
        imgURL = imgList[i]
        ext = imgURL.split('.')[-1]
        imgByte = Request(imgURL, headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'})
        f = open(f'banaIMG/bana{i}.{ext}', 'wb')
        iNameList.append(f'banaIMG/bana{i}.{ext}')
        f.write(urlopen(imgByte).read())
        f.close()

    return nameList, addList, iNameList