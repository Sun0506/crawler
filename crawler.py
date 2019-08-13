import requests as req 
import bs4  

res = req.get('https://www.eyny.com/video')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.text)
titles = soup.find_all('a', {'target':'_blank'})
for title in titles:
	if title != None:
		print(title.string)