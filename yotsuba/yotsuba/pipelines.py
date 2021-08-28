# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class YotsubaPipeline:
#     def process_item(self, item, spider):
#         return item
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image in item.get('image_urls', []):
            yield scrapy.Request(image["url"], meta={'image_names': image["name"]})

    def file_path(self, request, response=None, info=None):
        return '%s.jpg' % request.meta['image_names']