# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from asyncio.log import logger
from xml.etree.ElementInclude import default_loader
import scrapy
from itemloaders.processors import MapCompose, Join,Compose,TakeFirst
from scrapy import item
from scrapy.loader import ItemLoader
from collections import ChainMap
from itemloaders.common import wrap_loader_context
import numpy,re


def Remove_Extra_string(value):
    if "out of" in value:
        return value.replace("out of 5 stars","")
    return


def is_amazon_choice(values):
        if len(values) ==0 :
            return numpy.nan
        else:
            return True

def get_curr(price):
    
    pattern =  r'(\D*)[\d\,\.]+(\D*)'
    g = re.match(pattern, price.strip()).groups()
    return (g[0] or g[1]).strip()

def remove_curr(price):
    pattern =  r'(\D*)[\d\,\.]+(\D*)'
    g = re.match(pattern, price.strip()).groups()
    Currency=(g[0] or g[1]).strip()
    return price.replace(Currency,'').strip()



class Amazon_crawlerItem(scrapy.Item):

    default_output_processor = TakeFirst()


    Product_Url=scrapy.Field(
        output_processor=TakeFirst()
                            )

    ASIN=scrapy.Field(
        output_processor=TakeFirst()
                    )

    title=scrapy.Field(
        output_processor=TakeFirst()
                        )

    Price=scrapy.Field(
        input_processor=MapCompose(remove_curr),
        output_processor=TakeFirst()
                     )

    Currancy=scrapy.Field(
        input_processor=MapCompose(get_curr),
        output_processor=TakeFirst()
                     )

    Brand=scrapy.Field(
        output_processor=TakeFirst()
                     )


    Ratings=scrapy.Field(
        input_processor=MapCompose(Remove_Extra_string),
        output_processor=TakeFirst()
                       )

    Amazon_choice=scrapy.Field(
        
        input_processor=Compose(is_amazon_choice),
        output_processor =TakeFirst(),
        
                      )



   