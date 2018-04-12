### Steven Morgan
### Scraping Press Releases from State Republican Party Websites

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2, re, requests, bs4, os

### Maine

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.mainegop.com/news/previous/3)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 20): #20 
	x = "http://www.mainegop.com/news/previous/" + str(i) #+ "/"
	try:
		resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('www.mainegop.com/news/', str(link)) and not re.search('#comments', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('maineGOP_press_releases')
for link in links:
	if not re.search('http:', str(link)):
		res = requests.get(str('http:' + str(link)))
	else:
		res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('p', class_ = 'blog-date')
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.select('h2')
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	
	maine = open('MEgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#maine = open('MEgop_' + link[29:-1] + '.txt', 'w')
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				#maine.write(re.split('<', re.split('>', str(title))[1])[0])
				#maine.write('\n')
				maine.write(re.split('</', re.split('text">', str(pub))[1])[0].strip())
				maine.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			maine.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			maine.write(pElems[i].getText().encode("utf-8"))
			maine.write("\n")

			
### Alabama

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://algop.org/category/press-releases/page/2/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 32): #32
	x = "https://algop.org/category/press-releases/page/" + str(i) + "/"
	try:
		resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', class_ = 'button'):  #soup.find_all('a', href=True)
		if re.search('https://algop.org/', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('alabamaGOP_press_releases')
os.chdir('C:/Users/Steve/Desktop/State_Party_PR/scripts/alaskaGOP_press_releases')
for link in links:
	res = ''
	while res == '':
		try:
			res = requests.get(link)
		except:
			break
	#res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('time', attrs={'class': 'entry-date published updated'})  
	title = noStarchSoup.select('h1')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	print str(pub)
	#print str(title)
	#alabama = open(re.sub('/','_',('ALgop_' + link[18:-1] + '.txt')), 'w')
	alabama = open('ALgop_' + str(counter) + '.txt', 'w')
	counter += 1	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				print str(pub)
				print str(title)
				alabama.write(re.split('<', re.split('>', str(title))[1])[0])
				alabama.write('\n')
				alabama.write(re.split('T', re.split('datetime="', str(pub))[1])[0])
				alabama.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			alabama.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			alabama.write(pElems[i].getText().encode("utf-8"))
			alabama.write("\n")

			
### Alaska

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.alaskagop.net/news/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 107): 
	x = "http://www.alaskagop.net/news/page/" + str(i) + "/"
	try:
		resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', class_ = 'moreLink'): #soup.find_all('a', href=True, attrs={'class': 'moreLink'})
		if re.search('http://www.alaskagop.net', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('alaskaGOP_press_releases')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/scripts/alaskaGOP_press_releases')
for link in links:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	#pub = noStarchSoup.find('i', attrs={'class': 'fa fa-clock-o'})  
	pub = noStarchSoup.select('span')
	title = noStarchSoup.select('h5')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print str(title)
	#alaska = open(re.sub('/','_',('AKgop_' + link[25:-1] + '.txt')), 'w')
	alaska = open('AKgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				print str(pub)
				print str(title)
				alaska.write(re.split('<', re.split('>', str(title))[1])[0])
				alaska.write('\n')
				alaska.write(re.split('</', re.split('</i> ', str(pub))[1])[0])
				alaska.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			alaska.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			alaska.write(pElems[i].getText().encode("utf-8"))
			alaska.write("\n")

			
### Iowa

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://www.iowagop.org/category/news/releases/page/2/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 24): #24 
	x = "https://www.iowagop.org/category/news/releases/page/" + str(i) + "/"
	#resp = urllib2.urlopen(x)
	try:
		req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
		resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('www.iowagop.org/20', str(link)) and not re.search('#comments', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('IA_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('ul', class_ = 'meta')
	print pub
	#print re.split('</li> ', re.split('</a></li>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.select('h1')
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print title
	#print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	
	iowa = open('IAgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				iowa.write(re.split('</', re.split('">', str(title))[1])[0])
				iowa.write('\n')
				try:
					iowa.write(re.split('<li>', re.split('</li> ', re.split('</a></li>', str(pub))[1])[0].strip())[1])
					iowa.write('\n')
				except:
					pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			iowa.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			iowa.write(pElems[i].getText().encode("utf-8"))
			iowa.write("\n")

			
### Mississippi

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://msgop.org/news/page/2/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 37): #37
	x = "http://msgop.org/news/page/" + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	#try:
	#	req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
	#	resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	#except:
	#	pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('http://msgop.org/', str(link)) and len(str(link['href'])) > 25 and not re.search('tag', str(link)) and not re.search('category', str(link)) and not re.search('msgop.org/news', str(link)) and not re.search('msgop.org/officials|about-us|all-events|sgop.org/volunteer|get-involved', str(link)): #and not re.search('#respond', str(link)) and len(str(link['href'])) > 40:
			print link['href']
			links = links + [link['href']]
		#if not re.search('http', str(link)) and len(str(link['href'])) > 17 and not re.search('twitter', str(link)):
			#print link['href']
			#links = links + ['https://southcarolina.gop/orp-press-releases' + str(i) + str(link['href'])]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('MS_gop')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/MS_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#print pElems
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('div', class_ = 'postDate')
	#pub = noStarchSoup.find('span', class_ = 'aQJ') # date
	print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h2')#, class_ = 'heading')

	mississippi = open('MSgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				mississippi.write(re.split("<", re.split('>', str(title))[1])[0])
				mississippi.write('\n')
				mississippi.write(re.split('</', re.split('>', str(pub))[1])[0].strip())
				mississippi.write('\n')
				mississippi.write('\n')
				#try:
				#	mississippi.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				#	mississippi.write('\n')
				#except:
				#	pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			mississippi.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			mississippi.write(pElems[i].getText().encode("utf-8"))
			mississippi.write("\n")
			

### South Dakota

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://southdakotagop.com/stay-informed/press-releases/P0)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 13): #13
	x = "http://southdakotagop.com/stay-informed/press-releases/P0" + str((i - 1) * 6) #+ "/"
	resp = urllib2.urlopen(x)
	#try:
	#	req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
	#	resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	#except:
	#	pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('http://southdakotagop.com/stay-informed/press-releases/', str(link)) and len(str(link['href'])) > 65: #and not re.search('#respond', str(link)) and len(str(link['href'])) > 40:
			print link['href']
			links = links + [link['href']]
		#if not re.search('http', str(link)) and len(str(link['href'])) > 17 and not re.search('twitter', str(link)):
			#print link['href']
			#links = links + ['https://southcarolina.gop/orp-press-releases' + str(i) + str(link['href'])]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('SD_gop')
os.chdir('C:/Users/Steve/Desktop/State_Party_PR/SD_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#print pElems
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('h3', class_ = 'item-date')
	#pub = noStarchSoup.find('span', class_ = 'aQJ') # date
	print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h2')#, class_ = 'heading')
	
	southdakota = open('SDgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				southdakota.write(re.split("<", re.split('>', str(title))[1])[0])
				southdakota.write('\n')
				southdakota.write(re.split('</', re.split('>', str(pub))[1])[0].strip())
				southdakota.write('\n')
				southdakota.write('\n')
				#try:
				#	southdakota.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				#	southdakota.write('\n')
				#except:
				#	pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			southdakota.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			southdakota.write(pElems[i].getText().encode("utf-8"))
			southdakota.write("\n")

			
### South Carolina

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://www.sc.gop/blog/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 40): #94
	x = "https://www.sc.gop/blog/page/" + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://www.sc.gop/20', str(link)): #and not re.search('#respond', str(link)) and len(str(link['href'])) > 40:
			print link['href']
			links = links + [link['href']]
		#if not re.search('http', str(link)) and len(str(link['href'])) > 17 and not re.search('twitter', str(link)):
			#print link['href']
			#links = links + ['https://southcarolina.gop/orp-press-releases' + str(i) + str(link['href'])]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('SC_gop')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/SC_gop')
for link in links:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#print pElems
	pub = noStarchSoup.find('li', class_ = 'meta-date')
	title = noStarchSoup.find('h1')#, class_ = 'heading')

	
	southcarolina = open('SCgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				southcarolina.write(re.split("<", re.split('>', str(title))[1])[0])
				southcarolina.write('\n')
				southcarolina.write(re.split('</', re.split('</i>', str(pub))[1])[0].strip())
				southcarolina.write('\n')
				southcarolina.write('\n')
				#try:
				#	southcarolina.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				#	southcarolina.write('\n')
				#except:
				#	pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			southcarolina.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('SOUTH CAROLINA REPUBLICAN PARTY FOR IMMEDIATE RELEASE', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			southcarolina.write(pElems[i].getText().encode("utf-8"))
			southcarolina.write("\n")

			
### Oregon

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://oregon.gop/orp-press-releases)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 2): #2
	x = "https://oregon.gop/orp-press-releases" # + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	#try:
	#	req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
	#	resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	#except:
	#	pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		#if re.search('http://nh.gop', str(link)) and not re.search('#respond', str(link)) and len(str(link['href'])) > 40:
		#	print link['href']
		#	links = links + [link['href']]
		if not re.search('http', str(link)) and len(str(link['href'])) > 17 and not re.search('twitter', str(link)):
			#print link['href']
			links = links + ['https://oregon.gop/orp-press-releases' + str(i) + str(link['href'])]

links = links[17:]
links = list(set(links))
#print links
print len(links)

counter = 1

#os.makedirs('OR_gop')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/OR_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	print pElems
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	pub = noStarchSoup.select('time')
	#pub = noStarchSoup.find('span', class_ = 'aQJ') # date
	#print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h1')#, class_ = 'heading')
	
	oregon = open('ORgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				oregon.write(re.split("<", re.split('>', str(title))[1])[0])
				oregon.write('\n')
				oregon.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				oregon.write('\n')
				#try:
				#	oregon.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				#	oregon.write('\n')
				#except:
				#	pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		#if re.search('###', str(pElems[i])):
		#	oregon.write("###")
		#	break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			oregon.write(pElems[i].getText().encode("utf-8"))
			oregon.write("\n")

			
### North Carolina

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://www.nc.gop/news?page=3)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 6): #6
	x = "https://www.nc.gop/news?page=" + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		#if re.search('http://nh.gop', str(link)) and not re.search('#respond', str(link)) and len(str(link['href'])) > 40:
		#	print link['href']
		#	links = links + [link['href']]
		if not re.search('http', str(link)) and len(str(link['href'])) > 17 and not re.search('twitter', str(link)):
			print link['href']
			links = links + ['https://www.nc.gop/news?page=' + str(i) + str(link['href'])]
		
links = list(set(links))
print len(links)

counter = 1

#os.makedirs('NC_gop')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/NC_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	pub = noStarchSoup.select('time')
	#pub = noStarchSoup.find('span', class_ = 'aQJ') # date
	print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h1')#, class_ = 'heading')
	print title
	#title = noStarchSoup.select('h2')
	#print re.split("</", re.split('">', str(title))[1])[0]
	#print title
	#print re.split('\n', re.split('>\n', str(title))[1])[0]
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print title
	#print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	#print re.split('</time>', re.split('</span>', str(pub))[1])[0]
	
	northcarolina = open('NCgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				northcarolina.write(re.split("<", re.split('>', str(title))[1])[0])
				northcarolina.write('\n')
				northcarolina.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				northcarolina.write('\n')
				#try:
				#	northcarolina.write(re.split('</time>', re.split('</span>', str(pub))[1])[0].strip())
				#	northcarolina.write('\n')
				#except:
				#	pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			northcarolina.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			northcarolina.write(pElems[i].getText().encode("utf-8"))
			northcarolina.write("\n")
			
			
### New Hampshire

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.nh.gop/news/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 24): #24
	x = "http://nh.gop/news-and-events/page/" + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	#try:
	#	req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
	#	resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	#except:
	#	pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('http://nh.gop', str(link)) and not re.search('#respond', str(link)) and len(str(link['href'])) > 40:
			print link['href']
			links = links + [link['href']]
		#if not re.search('http', str(link)) and len(str(link['href'])) > 10 and not re.search('twitter', str(link)):
		#	print link['href']
		#	links = links + ['http://www.massgop.com/' + str(link['href'])]
		
links = list(set(links))
print len(links)

counter = 1

#os.makedirs('NH_gop')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/NH_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('span', class_ = 'aQJ') # date
	print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h1', class_ = 'heading')
	#title = noStarchSoup.select('h2')
	#print re.split("</", re.split('">', str(title))[1])[0]
	print title

	
	newhampshire = open('NHgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				newhampshire.write(re.split("</", re.split('">', str(title))[1])[0])
				newhampshire.write('\n')
				newhampshire.write('\n')
				try:
					newhampshire.write(re.split('\n', re.split('</i>', str(pub))[1])[0].strip())
					newhampshire.write('\n')
				except:
					pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			newhampshire.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			newhampshire.write(pElems[i].getText().encode("utf-8"))
			newhampshire.write("\n")
			

### Nebraska

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.ne.gop/news/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 2): 
	x = "http://www.ne.gop/news/"# + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('http://www.ne.gop/201', str(link)): #, str(link)) and not re.search('#respond', str(link)) and len(str(link['href'])) > 48:
			print link['href']
			links = links + [link['href']]

		
links = list(set(links))
print len(links)

counter = 1

#os.makedirs('NE_gop')
os.chdir('C:/Users/Steve/Desktop/State_Party_PR/NE_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('h1', class_ = 'entry-title') # date
	#print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h1', class_ = 'entry-title')
	#title = noStarchSoup.select('h2')
	#print re.split("</", re.split('">', str(title))[1])[0]
	print title
	#print re.split('\n', re.split('>\n', str(title))[1])[0]
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print title
	#print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	
	nebraska = open('NEgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				nebraska.write(re.split("</", re.split('">', str(title))[1])[0])
				nebraska.write('\n')
				nebraska.write('\n')
				try:
					nebraska.write(re.split('\n', re.split('</i>', str(pub))[1])[0].strip())
					nebraska.write('\n')
				except:
					pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('Get all the latest news and updates from the Nebraska Republican Party', str(pElems[i])):
			nebraska.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('Get all the latest news and updates from the Nebraska Republican Party', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			nebraska.write(pElems[i].getText().encode("utf-8"))
			nebraska.write("\n")
			
			
### Montana

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://mtgop.org/category/news/page/2/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 12): #12
	x = "http://mtgop.org/category/news/page/" + str(i) #+ "/"
	resp = urllib2.urlopen(x)
	#try:
	#	req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
	#	resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	#except:
	#	pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('mtgop.org', str(link)) and not re.search('#respond', str(link)) and len(str(link['href'])) > 48:
			print link['href']
			links = links + [link['href']]
		#if not re.search('http', str(link)) and len(str(link['href'])) > 10 and not re.search('twitter', str(link)):
		#	print link['href']
		#	links = links + ['http://www.massgop.com/' + str(link['href'])]
		
links = list(set(links))
print len(links)

counter = 1

#os.makedirs('MT_gop')
os.chdir('C:/Users/Steve/Desktop/State_Party_PR/MT_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('h1', class_ = 'title') # date
	#print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.find('h1', class_ = 'title')
	#title = noStarchSoup.select('h2')
	#print re.split("</", re.split('">', str(title))[1])[0]
	print title
	#print re.split('\n', re.split('>\n', str(title))[1])[0]
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print title
	#print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	
	montana = open('MTgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				montana.write(re.split("</", re.split('">', str(title))[1])[0])
				montana.write('\n')
				montana.write('\n')
				try:
					montana.write(re.split('\n', re.split('</i>', str(pub))[1])[0].strip())
					montana.write('\n')
				except:
					pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			montana.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			montana.write(pElems[i].getText().encode("utf-8"))
			montana.write("\n")
			
			
### Massachusetts

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.massgop.com/press?page=2)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 31): #31
	x = "http://www.massgop.com/press?page=" + str(i) #+ "/"
	#resp = urllib2.urlopen(x)
	try:
		req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
		resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		#if re.search('massgop.com', str(link)) and not re.search('#comments', str(link)):
		#	print link['href']
		#	links = links + [link['href']]
		if not re.search('http', str(link)) and len(str(link['href'])) > 10 and not re.search('twitter', str(link)):
			print link['href']
			links = links + ['http://www.massgop.com/' + str(link['href'])]
		
links = list(set(links))
print len(links)

counter = 1

#os.makedirs('MA_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('div', class_ = 'byline')
	#print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.select('h2')
	print title
	#print re.split('\n', re.split('>\n', str(title))[1])[0]
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print title
	#print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	
	massachusetts = open('MAgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				massachusetts.write(re.split("</", re.split('">', str(title))[1])[0])
				massachusetts.write('\n')
				try:
					massachusetts.write(re.split('\n', re.split('</i>', str(pub))[1])[0].strip())
					massachusetts.write('\n')
				except:
					pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			massachusetts.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			massachusetts.write(pElems[i].getText().encode("utf-8"))
			massachusetts.write("\n")

			
### Pennsyvlania

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://www.pagop.org/category/pressreleases/page/13/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 107): 
	x = "https://www.pagop.org/category/pressreleases/page/" + str(i) + "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://www.pagop.org/201', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('pennsylvaniaGOP_press_releases')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/scripts/alaskaGOP_press_releases')
for link in links:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	pub = noStarchSoup.select('time')
	#title = noStarchSoup.select('h1')
	title = noStarchSoup.find('h1', attrs={'class': 'entry-title'})
	print str(pub)
	print str(title)
	#pennsylvania = open('PA_' + link[30:-1] + '.txt', 'w')
	pennsylvania = open('PAgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt 
		if i == 0:
			try:
				print str(pub)
				print str(title)
				pennsylvania.write(re.split('<', re.split('>', str(title))[1])[0])
				pennsylvania.write('\n')
				pennsylvania.write(re.split('<', re.split('>', str(pub))[1])[0])
				pennsylvania.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			pennsylvania.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			pennsylvania.write(pElems[i].getText().encode("utf-8"))
			pennsylvania.write("\n")

			
### New Jersey

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.njgop.org/news/page/13/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 14): 
	x = "http://www.njgop.org/news/page/" + str(i) + "/"
	try:
		resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('http://www.njgop.org/201', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('newjerseyGOP_press_releases')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/scripts/alaskaGOP_press_releases')
for link in links:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.select('h1')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	print str(pub)
	#print str(title)
	#newjersey = open('NJgop_' + link[32:-1] + '.txt', 'w')
	newjersey = open('NJgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				newjersey.write(re.split('<', re.split('>', str(title))[1])[0])
				newjersey.write('\n')
				newjersey.write(re.split('</', re.split('>', str(pub))[1])[0])
				newjersey.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			newjersey.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			newjersey.write(pElems[i].getText().encode("utf-8"))
			newjersey.write("\n")

			
# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (http://www.florida.gop/press_releases?page=2)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 11): #11
	x = "http://www.florida.gop/press_releases?page=" + str(i) #+ "/"
	try:
		resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', class_ = 'btn btn-primary btn-sm btn-square marginbottomless'):  #soup.find_all('a', href=True)
		if re.search('', str(link)):
			print link['href']
			links = links + ['http://www.florida.gop' + str(link['href'])] 
			print links

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('californiaGOP_press_releases')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/scripts/alaskaGOP_press_releases')
for link in links:
	res = ''
	while res=='':
		try:
			res = requests.get(link)
		except:
			break
#	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
		
	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	pub = noStarchSoup.select('time')
	#pub = noStarchSoup.find('time', attrs={'class': 'entry-date published updated'})  
	title = noStarchSoup.select('h1')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	print str(pub)
	#print str(title)
	#florida = open(re.sub('/','_',('FLgop_' + link[22:-1] + '.txt')), 'w')
	florida = open('FLgop_' + str(counter) + '.txt', 'w')
	#print pElems
	counter += 1
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				print str(pub)
				print str(title)
				florida.write(re.split('<', re.split('>', str(title))[1])[0])
				florida.write('\n')
				florida.write(re.split('H', re.split('datetime="', str(pub))[1])[0])
				florida.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search("Optional email code", str(pElems[i])):
			florida.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			florida.write(pElems[i].getText().encode("utf-8"))
			florida.write("\n")
			
			
### California

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://www.cagop.org/news?page=2)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 7): #7
	x = "https://www.cagop.org/news?page=" + str(i) #+ "/"
	try:
		resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', title = 'Read More'):  #soup.find_all('a', href=True)
		if re.search('', str(link)):
			print link['href']
			links = links + ['https://www.cagop.org' + str(link['href'])]

links = list(set(links))
print len(links)

counter = 1

#os.makedirs('californiaGOP_press_releases')
#os.chdir('C:/Users/Steve/Desktop/State_Party_PR/scripts/alaskaGOP_press_releases')
for link in links:
	try:
		res = requests.get(link)
	except:
		break
#	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
		
	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	pub = noStarchSoup.select('time')
	#pub = noStarchSoup.find('time', attrs={'class': 'entry-date published updated'})  
	title = noStarchSoup.select('h1')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	print str(pub)
	#print str(title)
	#california = open(re.sub('/','_',('CAgop_' + link[22:-1] + '.txt')), 'w')
	california = open('CAgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				print str(pub)
				print str(title)
				california.write(re.split('<', re.split('>', str(title))[1])[0])
				california.write('\n')
				california.write(re.split('H', re.split('datetime="', str(pub))[1])[0])
				california.write('\n')
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search("Today, it's as important as ever to stand up and make sure you're a part of the solution for", str(pElems[i])):
			california.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			california.write(pElems[i].getText().encode("utf-8"))
			california.write("\n")

			
### Maryland

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (https://www.mdgop.org/news?page=2)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 14): #24 
	x = "https://www.mdgop.org/news?page=" + str(i) #+ "/"
	#resp = urllib2.urlopen(x)
	try:
		req = urllib2.Request(x, headers={'User-Agent' : "Magic Browser"})
		resp = urllib2.urlopen( req )
		#resp = urllib2.urlopen(x)
	except:
		pass
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		#if re.search('www.mdgop.org', str(link)) and not re.search('#comments', str(link)):
		#	print link['href']
		#	links = links + [link['href']]
		if not re.search('http', str(link)) and len(str(link['href'])) > 1:
			print link['href']
			links = links + ['https://www.mdgop.org/' + str(link['href'])]
		
links = list(set(links))
print len(links)

counter = 1

#os.makedirs('MD_gop')
for link in links:
	#if not re.search('http:', str(link)):
	#	res = requests.get(str('http:' + str(link)))
	#else:
	res = requests.get(link)
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
	#print type(noStarchSoup)
	#pElems = noStarchSoup.select('paragraph')
	pElems = noStarchSoup.find_all('p')
	#pElems = noStarchSoup.find_all('div', class_ = 'paragraph')
	#pub = noStarchSoup.select('time')
	pub = noStarchSoup.find('div', class_ = 'byline')
	#print pub
	#print re.split('\n', re.split('</i>', str(pub))[1])[0].strip()
	#pub = noStarchSoup.find('small', attrs={'class': 'date'})  
	title = noStarchSoup.select('h1')
	print title
	#print re.split('\n', re.split('>\n', str(title))[1])[0]
	#title = noStarchSoup.find('h2', class_ = 'blog-title')
	#title = noStarchSoup.find('h1', attrs={'class': 'col-md-8 col-md-offset-2'})
	#print str(pub)
	#print title
	#print re.split('</', re.split('text">', str(pub))[1])[0].strip()
	#print str(title)
	
	maryland = open('MDgop_' + str(counter) + '.txt', 'w')
	counter += 1
	#print pElems
	for i in range(len(pElems)):
		# Write parsed date to beginning of .txt   
		if i == 0:
			try:
				#print str(pub)
				#print str(title)
				maryland.write(re.split("</", re.split('">', str(title))[1])[0])
				maryland.write('\n')
				try:
					maryland.write(re.split('\n', re.split('</i>', str(pub))[1])[0].strip())
					maryland.write('\n')
				except:
					pass
			except:
				pass
		# When a paragraph with "###" is reached, the for loop breaks and the next url is parsed
		# This ensures that comments under the press release are not included in .txt
		if re.search('###', str(pElems[i])):
			maryland.write("###")
			break
		# For all paragraphs that do not contain "###" (used to indicate end of PR), write to .txt
		if not re.search('###', str(pElems[i])):
			#print pElems[i].getText().encode("utf-8")
			#print pElems[i].getText().encode("utf-8")
			maryland.write(pElems[i].getText().encode("utf-8"))
			maryland.write("\n")
