# This is a mini project using Beautiful Soup to list the name of movies 
# released in a particular year in order of popularity
from bs4 import BeautifulSoup
import requests



year = input()

# setting url with string concatenation and sending request
url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"
r = requests.get(url).content

data = BeautifulSoup(r,'lxml')
print(data.find('title').text)


movieList = data.findAll('div', attrs={'class': 'lister-item mode-advanced'})
i = 1
# finding the movie title from a large dictionary using HTML tags
for div_item in movieList:
    div = div_item.find('div',attrs={'class':'lister-item-content'})
    header = div.findChildren('h3',attrs={'class':'lister-item-header'})
    print(str(i) + '.'),
    print('Movie: ' + str((header[0].findChildren('a'))[0].contents[0]))
    i += 1