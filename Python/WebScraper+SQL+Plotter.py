import time

import pandas as pd

from selenium import webdriver

from bs4 import BeautifulSoup

from sqlalchemy import create_engine  

import matplotlib.pyplot as plt  

 
DRIVER_PATH = r"/Users/mouradsal/Downloads/DataSets Python/chromedriver"

URL = "https://www.kaggle.com/crawford/80-cereals"


def showQueryResult(sql):  

    engine     = create_engine('sqlite://', echo=False)  

    connection = engine.connect()  

    df.to_sql(name='cereal', con=connection, if_exists='replace', index=False)  

    # This code performs the query.  

    queryResult = pd.read_sql(sql, connection)  


    return queryResult  



browser = webdriver.Chrome(DRIVER_PATH)

browser.get(URL)

time.sleep(4)


def extractText(data): 

    text    = data.get_attribute('innerHTML') 

    soup    = BeautifulSoup(text, features="lxml") 

    content = soup.get_text() 

    return content 

headers = browser.find_elements_by_css_selector(".bjduuH")
data = browser.find_elements_by_css_selector(".hPyIKH div")

headerList   = [] 

dataList = [] 

for i in range(0, len(headerList)): 

    # extract title and add to list. 

    header = extractText(headers[i]) 

    headerList.append(header) 

 

    # extract description and add to list. 

    mainData = extractText(data[i]) 

    dataList.append(mainData) 

 

# Show the content. 

for i in range(0, len(dataList)): 

    print("\n********************") 

    print("Headers:  " + headerList[i]) 

    print("Data: " + dataList[i])
   
    
dataDictionary = {}

df = pd.DataFrame(dataDictionary)

df.to_csv(r"/Users/mouradsal/Downloads/DataSets Python/Cereal.csv", sep = ",")
print(df)




SQL = ("SELECT name, # calories, AVG(# calories) AS 'Average Calorie' FROM cereal \
       GROUP BY name")

results = showQueryResult(SQL)


plt.subplots(nrows = 2, ncols =3, figsize=(14,7))

plt.subplot(1,1,1)

plt.bar(results['Name'], results['# calories'], color="green")

plt.title("Cereal Brand Nutritional Info")

plt.show()

    

     