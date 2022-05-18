import scrapy


class MytheresaItem(scrapy.Item):
    name1 = scrapy.Field()
    name2 = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    breadcrumbs = scrapy.Field()
    image_url = scrapy.Field()
    brand = scrapy.Field()
    product_name = scrapy.Field()
    listing_price = scrapy.Field()
    offer_price = scrapy.Field()
    discount = scrapy.Field()
    product_id = scrapy.Field()
    sizes = scrapy.Field()
    description = scrapy.Field()
    other_images = scrapy.Field()
