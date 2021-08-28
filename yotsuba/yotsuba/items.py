# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from urllib3 import poolmanager


class YotsubaItem(scrapy.Item):
    # define the fields for your item here like:
    chapter = scrapy.Field()
    page    = scrapy.Field()
    src     = scrapy.Field()

class ImagescraperItem(scrapy.Item):
    images = scrapy.Field()
    image_names = scrapy.Field()
    image_urls = scrapy.Field()