import requests as req 
import bs4  

baha = []
# 抓取網頁 1 ~ 3 頁
for i in range(1,4):
	url = 'https://forum.gamer.com.tw/'
	res = req.get('https://forum.gamer.com.tw/B.php?page={}&bsn=23805'.format(i))
	# print(res.text)
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	# print(soup.text)
	titles = soup.find_all('a', {'class':'b-list__main__title'})

# 將標題和網址寫入字串
	names = []
	webs = []
	for title in titles:
		if title.string != '首篇已刪':
			names.append(title.string)
			webs.append(url + title.get('href'))

# 把兩個字串合併成字典
	bahas = dict(zip(names, webs))
	for key, value in bahas.items():
		baha.append(key + ': ' + value)

# 寫入 baha 文字檔
with open('baha.txt', 'w') as f:
	for line in baha:
		f.write(line + '\n')
print('我寫好了!')