from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"


browser = webdriver.Chrome('C:/Users/vkaun/OneDrive/Desktop/Python/Exoplanets/chromedriver.exe')
browser.get(start_url)

time.sleep(10)

scrapped_data = []



def scrape():
               
      
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star = soup.find("table", attrs={"class", "wikitable"})
        
        table_body = bright_star.find('tbody')

        table_rows = table_body.find_all('tr')


        for row in table_rows:
            tables = row.find_all('td')
            print(tables)

            
            temp_list = []

            for columns in tables:
                data = columns.text.strip()
                temp_list.append(data)
            scrapped_data.append(temp_list)


       
 
scrape()



stars_data = []


for i in range(0,len(scrapped_data)):
    
    Star_names = scrapped_data[i][1]
    Distance = scrapped_data[i][3]
    Mass = scrapped_data[i][5]
    Radius = scrapped_data[i][6]
    Lum = scrapped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)



headers = ['Star_name','Distance','Mass','Radius','Luminosity']  


star_df = pd.DataFrame(stars_data, columns=headers)

star_df.to_csv('scraped_data.csv',index=True, index_label="id")
