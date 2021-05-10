#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import gzip
import json


# In[4]:


def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('Cell_Phones_and_Accessories_5.json.gz')


# In[5]:


df.to_csv('cell_phone_and_accessories_review.csv')

