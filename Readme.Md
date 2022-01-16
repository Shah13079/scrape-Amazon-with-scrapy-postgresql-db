**About**:<br/>
This project is made with python scrapy framework with advance concpets of using item adopters and item input out processors, the spider "Amazon_spider" get URLS from input excel file and read URL of products one by one and spider sends the requests , parsing the response & applay some processings.

In pipelines.py the pipelines are written with ORMS  using SQLAlchemy, which saving data into Postgres database, also updating the price of product on another crawl process.

**Some features**:<br/>
1) database integration
2) ORM used
3) scrapy item input and output processors
4) Passing arguments with CMD
5) Proxies Rotation
6) models

**Proxy Rotation**:<br/>
As we know that Amazon blocks IP address by hitting their server too much with bot in certain time, that's why I Integrate Zyte smart proxies, to rotate the proxies for each request and solve this problem, please refer to setting.py and Put your Zyte API to variable  
```
DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 610} 
# enable crawlera 
CRAWLERA_ENABLED = True 
#  APIKEY of zyte smart proxies
CRAWLERA_APIKEY = 'YOUR_API_HERE' 

```

**Tools and packages used in this project:**<br/>
Python<br />
Scrapy framework<br />
Zyte: Smart Proxies<br />
Postgres: a free and open-source relational database management system<br />
ORM :Object–relational mapping<br />
SQLAlchemy: an open-source SQL toolkit and object-relational mapper for Python<br />

**Setup:**<br/>
Donwload python from official website: https://www.python.org/downloads/ <br/>
Scrapy requires Python 3.6+<br />
Make sure pip package-management system is installed

**Prerequisites:** <br />
Open CMD and change working directory into project directory and give command:<br/>
pip install -r requirements.txt <br/>
this will install all required dependencies and packges.

**Run:** <br />
1) Run for default Excel Urls file :<br />```scrapy crawl Amazon_spider -o data.csv```  (-o filename.csv will generate data csv file ) <br/>
2) Pass another excel file by command:<br/>```scrapy crawl Amazon_spider -a file_to_read=YOUR_FILE_NAME_HERE -o OUTPUT_FILE.csv``` <br/>


**Cancel Process:** <br />
CTRL+C to cancel.

Note:
If you don't want to use Database Simply comment out bellow piplines middlewares in settings.py:
```
ITEM_PIPELINES = {
   'Amazon_crawler.pipelines.Amazon_crawlerPipeline': 300,
}
```
-----------------------------------------------------------------------------------------
