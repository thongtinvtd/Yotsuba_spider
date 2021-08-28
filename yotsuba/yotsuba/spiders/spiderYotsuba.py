import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import time

class SpideryotsubaSpider(scrapy.Spider):
    name = 'spiderYotsuba'
    allowed_domains = ['nettruyenvip.com/truyen-tranh/yotsubato-6628']
    # start_urls = ['http://www.nettruyenvip.com/truyen-tranh/yotsubato-6628/']
    def start_requests(self):
            urls = ['http://www.nettruyenvip.com/truyen-tranh/yotsubato-6628/']
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        url = 'http://www.nettruyenvip.com/truyen-tranh/yotsubato-6628/'
        self.driver = webdriver.Firefox()
        self.driver.get(url)
          # Implicit wait
        self.driver.implicitly_wait(10)
        # Explicit wait
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "chapter")))
        time.sleep(2)

        # Hand-off between Selenium and Scrapy happens here
        sel = Selector(text = self.driver.page_source)

        # Extract link
        links = sel.xpath("//div[@class='list-chapter']/nav/ul/li/div[1]/a/@href").getall()
        print('link gotten:', links)
        for link in links:
            yield {"link":link,}
        # for link in links:
        #     yield scrapy.Request(url=link, callback=self.saveImg)
        self.driver.quit()

    def jpg2pdf():
        pass