#!/usr/bin/env python
# coding: utf-8

# # Import Modules

# In[17]:


import pandas as pd
# This module displays Markdown and helps with visability within Juypter Notebooks
from IPython.display import Markdown
import os


# ### Check to see if that statistical data is present within the current directory

# In[3]:


def get_atp_w41_spss_data():
    '''Check to see if the .sav file is within the current directory. If it is not in the 
    current directory path, it will download it from Kaggle at:
    
    "https://www.kaggle.com/shankanater/american-trends-panel-pewresearch/download"
    
    and will return the data as a Pandas DataFrame.
    '''
    # Set default filename
    filename = 'ATP W41.sav'
    # Check if the file exists within the current directory
    if os.path.exists(filename):
        # if it exists read into Pandas DataFrame and return 
        return pd.read_spss(filename)
    # If the file does not exist, let the user know
    else:
        print('The file was not found, you will need to download it from Kaggle https://www.kaggle.com/shankanater/american-trends-panel-pewresearch/download')


# ### If this is the main file, then run below here

# In[20]:


if __name__ == '__main__':
    # Get the spss data, and download it if it does not exist.
    df = get_atp_w41_spss_data()

    # Look at the dataframe
    df.head()


# In[ ]:




