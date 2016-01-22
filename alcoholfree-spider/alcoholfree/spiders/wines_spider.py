import scrapy

from alcoholfree.items import WineItem

class WinesSpider(scrapy.Spider):
    name = "wines"
    start_urls = [
        "http://www.deliciousdrinksshop.co.uk/nonalcoholicwines?mode=grid",
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="products-container"]//li[contains(@class, "item")]'):
            item = WineItem()
            item['title'] = sel.xpath('h2[@class="product-name"]/a/text()').extract_first()
            item['price'] = sel.xpath('div/div[@class="price-box"]/span[@class="regular-price"]/span[@class="price"]/text()').extract_first()
            item['thumbnail_url'] = sel.xpath('a[@class="product-image"]/img/@src').extract_first()

            detail_path = sel.xpath('h2[@class="product-name"]/a/@href').extract_first()
            request = scrapy.Request(response.urljoin(detail_path), callback=self.parse_detail)
            request.meta['item'] = item
            yield request

        next_page = response.xpath('//div[@class="pages"]//a[@class="next"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['image_url'] = response.xpath('//*[@id="image"]/@src').extract_first()
        item['brief_description'] = response.xpath('//div[@class="short-description"]/div[@class="std"]/text()').extract_first()
        item['long_description'] = response.xpath('//div[contains(@class, "box-description")]/div[@class="std"]/text()').extract_first()

        for sel in response.xpath('//div[contains(@class, "box-additional")]/table/tbody/tr'):
            DETAIL_MAP = {
                'Manufacturer': 'manufacturer',
                'Country of origin': 'country_of_origin',
                'Volume (Liter)': 'volume_in_liter',
                'Alcohol By Volume': 'alcohol_by_volume',
                'Calories (kCal/ 100ml)': 'calories_in_kcal_per_100ml',
                'Grapes': 'grape_type',
            }
            label = sel.xpath('th[@class="label"]/text()').extract_first()
            if label in DETAIL_MAP.keys():
                item[DETAIL_MAP[label]] = sel.xpath('td[contains(@class, "data")]/text()').extract_first()

        yield item
