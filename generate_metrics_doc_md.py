#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


# exact metrics info from file
def get_metrics(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    metrics = {}
    for li in lines:

        if not li.startswith('#'):
            continue

        words_list = li[:-1].split(' ')
        name = words_list[2]

        if name not in metrics:
            metrics[name] = {}

        metrics[name][words_list[1]] = ' '.join(words_list[3:])
        
    return metrics


# In[3]:


base_path = './istio_metrics_example/'
paths = os.listdir(base_path)

# write metrics info to metrics_doc.md
with open('metrics_doc.md','w') as f:
    
    for p in paths:

        f.write('### %s\n' % p)

        metrics = get_metrics(base_path + p)

        f.write('|name|help|type|\n')
        f.write('|---|---|---|\n')
        for k in metrics:
            met = metrics[k]
            hh = met['HELP'] if 'HELP' in met else ''
            tt = met['TYPE'] if 'TYPE' in met else ''
            f.write('|%s|%s|%s|\n' % (k, hh, tt))


# In[ ]:




