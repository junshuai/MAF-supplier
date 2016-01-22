# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WineItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    thumbnail_url = scrapy.Field()
    brief_description = scrapy.Field()

    image_url = scrapy.Field()
    long_description = scrapy.Field()
    manufacturer = scrapy.Field()
    country_of_origin = scrapy.Field()
    volume_in_liter = scrapy.Field()
    alcohol_by_volume = scrapy.Field()
    calories_in_kcal_per_100ml = scrapy.Field()
    grape_type = scrapy.Field()
