# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from datetime import date
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
from asyncio.log import logger
from math import prod
from sqlalchemy.orm import sessionmaker
from .spiders.models import db_connect, create_table,Amazon_data_model



class Amazon_crawlerPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()


    def process_item(self, item, spider):
        """Save data in the database.
        This method is called for every item pipeline component.
        """
        item_exists =self.session.query(Amazon_data_model).filter_by(ASIN=item['ASIN']).first()
        
        if item_exists and item.get("Price") is not None:
            item_exists.Price=item.get('Price')         #Update the price here
            item_exists.Currancy=item.get('Currancy')   #Update the Currency 
         
        elif item_exists is None:
            new_item=Amazon_data_model(**item) #Unpacking the the data 
            self.session.add(new_item)

        return item

        
    def close_spider(self, spider):
        # We commit and save all items to DB when spider finished scraping.
        try:
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()

      







