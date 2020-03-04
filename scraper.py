import requests
import urllib.request
import time
import bs4
import datetime

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
soup.findAll('span')
infected = soup.findAll('span')
dead = soup.findAll('span')
recovered = soup.findAll('span')

print('Currently, the 2019 novel coronavirus on ' + datetime.datetime.now + ' has infected ' + infected + ' people and killed ' + dead + '. ' + recovered + ' have recovered.')
