# import module
import requests
from bs4 import BeautifulSoup
  
# user define function
# Scrape the data
def getdata(url):
    r = requests.get(url)
    return r.text
  
  
# input by geek
from_Station_code = "GAYA"
from_Station_name = "GAYA"
  
To_station_code = "PNBE"
To_station_name = "PATNA"
# url
url = "https://www.railyatri.in/booking/trains-between-stations?from_code="+from_Station_code+"&from_name="+from_Station_name+"+JN+&journey_date=+Wed&src=tbs&to_code=" + \
    To_station_code+"&to_name="+To_station_name + \
    "+JN+&user_id=-1603228437&user_token=355740&utm_source=dwebsearch_tbs_search_trains"
  
# pass the url
# into getdata function
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')
  
# find the Html tag
# with find()
# and convert into string
data_str = ""
for item in soup.find_all("div", class_="col-xs-12 TrainSearchSection"):
    data_str = data_str + item.get_text()
result = data_str.split("\n")
  
print("Train between "+from_Station_name+" and "+To_station_name)
print("")
  
# Display the result
for item in result:
    if item != "":
        print(item)
