import scrapy
from .utilities import *
from scrapy.loader import ItemLoader
from ..items import Amazon_crawlerItem


class AmazonSpider(scrapy.Spider):
    name = 'Amazon_spider'

    #Taking Arguments from outside of spider | User don't need to edit code 
    def __init__(self, file_to_read='Products_ursl' , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = file_to_read

    
    def start_requests(self):
        Urls=Reading_excelFile(self.filename)
        for each_url in Urls:
           yield scrapy.Request(url=each_url,
            callback=self.parse,
            headers={"User-Agent":User_agents})


    def parse(self, response):
        loader=ItemLoader(item=Amazon_crawlerItem(),response=response,)

        loader.add_value('Product_Url',response.url)
        loader.add_value("ASIN",get_ASIN(response.url))
        loader.add_xpath("title","normalize-space(//h1[@id='title']/span/text())")
        loader.add_xpath("Price",'//span[@class="a-size-medium a-color-price" and @id="price_inside_buybox"]/text()')
        loader.add_xpath("Currancy",'//span[@class="a-size-medium a-color-price" and @id="price_inside_buybox"]/text()')
        loader.add_xpath("Ratings",'(//span[contains(text(),"out of 5 stars")])[1]/text()')
        loader.add_xpath("Brand","(//td/span[contains(text(),'Brand')]/following::td)[1]/span/text()")
        loader.add_xpath("Amazon_choice","//span[contains(text(),'Choice')]/text()")
        
        yield loader.load_item()




