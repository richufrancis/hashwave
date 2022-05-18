import scrapy
from ..items import MytheresaItem


class MytheresaSpider(scrapy.Spider):
    name = 'mytheresa'
    allowed_domains = ['https://www.mytheresa.com/']
    start_urls = ['https://www.mytheresa.com/int_en/men/shoes.html?p=1', ]

    page_number = 1

    def parse(self, response):
        items = MytheresaItem()
        name1 = response.xpath('//span[@class="ph1"]/text()').extract()
        name2 = response.xpath('//a[@class="pa1-rm"]/text()').extract()

        price = response.xpath('//span[@class="price"]/text()').extract()


        items['name1'] = name1
        items['name2'] = name2
        items['price'] = price

        yield {"name1": name1, "name2": name2, "price": price}

        href = response.xpath(('// div[1] / div / div[2] / div[2] / div[2] / div[2] / div[2] / div / div[6] / ul / li[1] / a[1] / @ href')).extract()
        items['href'] = href
        yield items
        for i in href:
            next_url = i
            yield response.follow(next_url, callback=self.parse_details)

    def parse_details(self, response):
        name1 = response.xpath('//span[@class="ph1"]/text()').extract()
        breadcrumbs = response.xpath()
        image_url = response.xpath('// [ @ id = "product-collection-image-2201760"]/scr()').extract()
        brand = response.xpath('//[@id="filter-designer"]/li[3]/a/span[2]/text()').extract()
        product_name = response.xpath('// [ @ id = "product-collection-image-2201760"]/scr()').extract()')
        listing_price = response.xpath('// [ @ id = "product-collection-image-2201760"]/scr()').extract()')
        offer_price = response.xpath(''//[@id="filter-accordion"]/h3[2]/span[1]/'')
        discount = response.xpath(''//[@id="filter-accordion"]/h3[2]/span[1]/'')
        product_id = response.xpath('// [ @ id = "product-collection-image-2201760"]/scr()').extract()')
        sizes = response.xpath('//*[@id="filter-accordion"]/h3[2]/span[1]/')
        description = response.xpath(''//[@id="filter-accordion"]/h3[2]/span[1]/'')
        other_images = response.xpath(''//[@id="filter-accordion"]/h3[2]/span[1]/'')

        next_page = 'https://www.mytheresa.com/int_en/men/shoes.html?p=' + str(MytheresaSpider.page_number)

        if MytheresaSpider.page_number <= 10:
            MytheresaSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

# print(response.xmlpath)
# print(response.xpath('//li[@class="item"]').get())
# print(response.xpath('//ul[@class="col-main"]').get())
# print(response.xpath('//ul[@class="mt-slider"]').get())
# print(response.xpath('//div[@class="main"]').get())
# print(response.xpath('//div[@class="block-title"]').get())
# print(response.xpath('//div[@class="//div[@class="breadcrumbs-text"]/ul"]').get())

# for mytheresa in response.xpath("//div[@class='breadcrumbs']"):
#     yield {
#         'breadcrumbs': mytheresa.xpath(".//div[@class='breadcrumbs']/ul").extract_first()
#     }
