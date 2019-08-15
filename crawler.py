import requests as req 
import bs4  

url = 'https://forum.gamer.com.tw/'
res = req.get('https://forum.gamer.com.tw/B.php?bsn=23805&subbsn=0')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.text)
titles = soup.find_all('a', {'class':'b-list__main__title'})

names = []
webs = []
for title in titles:
	if title.string != '首篇已刪':
		names.append(title.string)
		webs.append(title.get('href'))

urls = []
for web in webs:
	urls.append(url + web)

baha = []
bahas = dict(zip(names, urls))
for key, value in bahas.items():
	baha.append(key + ': ' + value)

with open('baha.txt', 'w') as f:
	for line in baha:
		f.write(line + '\n')
	print('我寫好了!')