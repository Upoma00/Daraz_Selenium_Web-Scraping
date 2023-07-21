#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd


# In[3]:


#Creating a driver Object
driver = webdriver.Chrome()


# In[ ]:


https://scrapinghub.github.io/xpath-playground/


# In[4]:


url = 'https://www.daraz.com.bd/smartphones/?page=2&spm=a2a0e.home.cate_6.1.573712f73RbHzd'


# In[5]:


# pass the url
driver.get(url)


# In[6]:


all_phones = []
phones = driver.find_elements('xpath','//div[@data-spm="list"]/div')
for phone_index, phone in enumerate(phones, 1):
    title = driver.find_element('xpath',f'(//div[@class="title--wFj93"]/a)[{phone_index}]')
    discount_price = driver.find_element('xpath',f'(//div[@class="price--NVB62"]/span)[{phone_index}]')
    try:
        previous_price = driver.find_element('xpath', f'(//del[@class="currency--GVKjl"])[{phone_index}]').text
    except:
        previous_price = ''
    data = {
        'title' : title.text,
        'url':title.get_attribute('href'),
        'discount_price':discount_price.text,
        'previous_price':previous_price
    }
    all_phones.append(data)


# In[7]:


all_phones


# In[9]:


df = pd.DataFrame(all_phones)
df.to_csv('daraz_smartphone.csv',index=False)


# In[10]:


list_ = [23,45,6,763,34,65]

for index ,value in enumerate(list_,1):
    print(index,value)


# In[15]:


from time import sleep

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # You need to have ChromeDriver installed and in PATH

all_phones = []

for page in range(1, 10):
    url = f'https://www.daraz.com.bd/smartphones/?page={page}&spm=a2a0e.home.cate_6.1.3fbe12f72Iocse'
    # pass the url
    driver.get(url)
    sleep(5)
    phones = driver.find_elements_by_xpath('//div[@data-spm="list"]/div')
    for phone_index, phone in enumerate(phones, 1):
        title = driver.find_element_by_xpath(f'(//div[@class="title--wFj93"]/a)[{phone_index}]')
        discount_price = driver.find_element_by_xpath(f'(//div[@class="price--NVB62"]/span)[{phone_index}]')
        try:
            previous_price = driver.find_element_by_xpath(f'(//del[@class="currency--GVKjl"])[{phone_index}]').text
        except:
            previous_price = ''
        data = {
            'title': title.text,
            'url': title.get_attribute('href'),
            'discount_price': discount_price.text,
            'previous_price': previous_price
        }
        all_phones.append(data)

# Quit the WebDriver after scraping all pages
driver.quit()


# In[ ]:


df = pd.DataFrame(all_phones)
df.to_csv('daraz_smartphone.csv',index=False)


# In[ ]:




