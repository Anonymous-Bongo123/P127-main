from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4 
from bs4 import BeautifulSoup
import pandas as pd
import requests


START_URL = "https://en.wikipedia.org/w/index.php?title=List_of_brightest_stars_and_other_record_stars&oldid=1147387876"
browser = webdriver.Chrome("C:/Users/Owner/Downloads/P127_main/chromedriver.exe")
browser.get(START_URL)

# scraped_data = []

# def scrape():
#     soup=BeautifulSoup(browser.page_source, "html.parser")
#     bright_star_table = soup.find("table", attrs={"class", "wikitable"})
#     table_body=bright_star_table.find('tbody')
#     table_rows=table_body.find_all('tr')
#     for row in table_rows:
#         table_cols=row.find_all('td')
#         #print(table_cols)
#         temp_list=[]
#         for col_data in table_cols:
#             #print(col_data.text)
#             data = col_data.text.strip()
#             #print(data)
#             temp_list.append(data)
#         scraped_data.append(temp_list)
#         stars_data=[]
#         for i in range(0,len(scraped_data)):
#             Star_names = scraped_data[i][1]
#             Distance = scraped_data[i][3]
#             Mass = scraped_data[i][5]
#             Radius = scraped_data[i][6]
#             Lum = scraped_data[i][7]
#             required_data = [Star_names, Distance, Mass, Radius, Lum]
#             stars_data.append(required_data)
#             headers = ['Star_names', 'Distance', 'Mass', 'Radius', 'Lum']
#             star_df_1 = pd.DataFrame(stars_data, columns=headers)
#             star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")




# page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
