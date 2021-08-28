# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='./venv/bin/chromedriver')
# driver.get ("https://vntesters.com/")
# print (driver.title)
# driver.quit()
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from scrapy import Selector
# import urllib.request
import imageio

class HelloSelenium:
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)

    def get_site_info(self):
        print('URL:', self.driver.current_url)
        print('Title:', self.driver.title)
        sleep(5)
        self.driver.save_screenshot('screen_shot.png')

    def saveWeb(self):
        with open('./output.html','w') as f:
            f.write(self.driver.page_source)

    def saveImg(self):
        img = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[2]/div/div/div/div/div/div[3]/div/div/div/img[1]')
        src = img.get_attribute('src')
        print(src)
        bufferImg = imageio.imread(imageio.core.urlopen(src).read(),'jpg')
        bufferImg.shape
        imageio.imwrite('ouput.jpg',bufferImg[:,:,0])


if __name__ == '__main__':
    hello = HelloSelenium('https://shakai.ru/manga-read/752/32/1')
    hello.get_site_info()
    hello.saveImg()
    # Close driver
    hello.driver.close()
