import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time
from ..items import ImagescraperItem
from os import rename

class Spideryotsuba1Spider(scrapy.Spider):
    name = 'spiderYotsuba1'
    # allowed_domains = ['www.nettruyenvip.com/truyen-tranh/yotsubato/chap-1/125296']
    def start_requests(self):
        # urls = ['https://shakai.ru/manga-read/752/32/1']
        urls = ['http://www.nettruyenvip.com/truyen-tranh/yotsubato/chap-1/125296']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.driver = webdriver.Firefox()
        url = 'http://www.nettruyenvip.com/truyen-tranh/yotsubato/chap-1/125296'
        # url = 'https://shakai.ru/manga-read/752/32/1'
        self.driver.get(url)
          # Implicit wait
        self.driver.implicitly_wait(10)
        # Explicit wait
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "page-chapter")))
        
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "application__image-wrapper")))
        time.sleep(2)
        # try:
        #     formatButton = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div[1]')
        #     formatButton.click()
        # except Exception as e:
        #     print('error:',e)

        # Hand-off between Selenium and Scrapy happens here
        sel = Selector(text = self.driver.page_source)

        # Extract link
        img_URL = sel.xpath('//div[@class="page-chapter"]/img/@src').getall()
        # img_URL = sel.xpath('/html/body/div[1]/div[6]/div[2]/div/div/div/div/div/div[3]/div/div/div/img/@src').getall()
        print('url:',img_URL)
        
        img_URLs = []
        for url in img_URL:
            url = 'https:' + url
            img_URLs.append(url)
        print('link Images:',img_URLs)
        image = ImagescraperItem()

        img_Name = []
        img_URLs = []
        for i in range(len(img_URL)):
            img_Name.append(i)
        for (url,name) in zip(img_URL,img_Name):
            url = 'https:' + url
            img_URLs.append({'url':url,'name':name})

        image["image_urls"] = img_URLs
        yield  image
        # print('image1:',image['images'])
        self.driver.quit()