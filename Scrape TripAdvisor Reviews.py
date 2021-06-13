#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as soup


# In[2]:


html = requests.get('https://www.tripadvisor.in/Hotels-g187147-Paris_Ile_de_France-Hotels.html')
html.status_code


# In[3]:


bsobj = soup(html.content,'lxml')


# In[4]:


links = []

for review in bsobj.findAll('a',{'class':'review_count'}):
    a = review['href']
    a = 'https://www.tripadvisor.in'+ a
    #links.append('https://www.tripadvisor.in/'+a)
    print(a)
        
    print(a.find('Reviews'))
    a = a[:(a.find('Reviews')+7)] + '-or{}' + a[(a.find('Reviews')+7):]
    print(a)
    links.append(a)
links


# In[5]:


from random import randint
from time import sleep

reviews = []

for link in links:
    d = [5,10,15,20,25]
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    html2 = requests.get(link.format(i for i in range(5,1000,5)),headers=headers)
    sleep(randint(1,5))
    bsobj2 = soup(html2.content,'lxml')
    for r in bsobj2.findAll('q'):
        reviews.append(r.span.text.strip())
        print(r.span.text.strip())
        
reviews

