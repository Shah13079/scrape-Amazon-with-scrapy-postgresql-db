from logging import exception
from openpyxl import load_workbook
import re


User_agents={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

#Reading excel file column A and return List of Links
def Reading_excelFile(filename):
    column_urls_list=list()
    try:
        Urls_Sheets = load_workbook(f'.//{filename}.xlsx')
    except FileNotFoundError:
        raise 
    
    else:

        sheet = Urls_Sheets.active

        #Finding length of column a to iterate
        ws = len(sheet['A'])
        for i in range(1,ws):
            Product_url=sheet[f'A{i+1}'].value
            if Product_url is not None and "http" in Product_url:
                column_urls_list.append(Product_url
                )
                
        return column_urls_list


#Getting ASIN from Product Url using re
def get_ASIN(href):
    asin = re.search(r'/[dg]p/([^/?]+)', href, flags=re.IGNORECASE)
    if asin:
        return asin.group(1)
    
    

