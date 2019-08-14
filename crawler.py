import requests as req 
import bs4  

res = req.get('https://forum.gamer.com.tw/B.php?bsn=23805&subbsn=0')
# print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.text)
titles = soup.find_all('a', {'class':'b-list__main__title'})

names = []
for title in titles:
		if title.string != '首篇已刪':
			names.append(title.string)


with open('eyny.txt', 'w') as f:
	for name in names:
		f.write(name + '\n')
	print('我寫好了!')
