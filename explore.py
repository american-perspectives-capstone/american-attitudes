#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

from sklearn.model_selection import train_test_split

from scipy import stats
from sklearn.linear_model import LinearRegression

# python display
from IPython.display import HTML, display_html, display

#Feature Selection
from sklearn.feature_selection import SelectKBest, f_regression, RFE

from prepare import *


# In[135]:


class Attitudes_explore():
    '''
    Performs a series of analyses and explore functions on various features in our data.
    '''
    
    def __init__(self, df: pd.DataFrame, target: str, subset_title: str):
        '''
        Initializes the self of the class.
        '''
        self.target = target
        
        self.subset_title = subset_title
        
        # Pull the categorical features from dataframe
        try: 
            self.categorical_features = df.drop(columns = ['qkey', "weight", target]).columns.to_list()
        except:
            self.categorical_features = df.drop(columns= [target]).columns.to_list()
        
        # Split the dataframe
        train, validate, test = train_validate_test_split(df, target)
        
        # Make train datasets
        self.X_train = train.drop(columns=[target])
        self.y_train = train[target]
        
        # Make validate datasets
        self.X_validate = validate.drop(columns=[target])
        self.y_validate = validate[target]
        
        # Make test datasets
        self.X_test = test.drop(columns=[target])
        self.y_test = test[target]
        
        
        
    def run_statistical_tests(self):
        '''This method will iterate though the categorical feature columns and run various statistical tests
        and will print the results for each test.
        The tests being performed are:
        chi_squared
        significant_p_val
        list_significant_columns
        insignificant_p_val
        list_insignificant_columns
        '''
        
        # Create column_based_dict statistic attributes
        self.chi2_df = pd.DataFrame(columns=['chi2', 'p_val', 'deg_free', 'expected_freq'])
        
        # Iterate through the categorical features
        for col in self.categorical_features:
            
            #Create contingency table
            contingency_table = pd.crosstab(self.X_train[col], self.y_train)
            
            #Get test results of chi-squared test
            chi2, p, deg_free, expect_freq = stats.chi2_contingency(contingency_table)
            # Add to the dataframe
            self.chi2_df.loc[col]= [chi2, p, deg_free, expect_freq]
    
    def plot_bar_graphs(self, n=5, saved=False):
        '''Plots the target and each variable for top 'n' results from the chi2 test
        '''
        display(HTML(f'''<html><h1>{self.subset_title}</h1></html>'''))
        # Select the n most relevant p_vals
        
        for col in self.chi2_df.head(n).index:
            plt.figure(figsize=(10, 5))
            sns.barplot(x= self.y_train, y = self.X_train[col]).set_title(
                label=f'{self.target.title()} vs {col.title()} Barplot')
            plt.xticks(rotation = 90, horizontalalignment='right', fontsize = 12)
            if saved:
                plt.savefig(f"images/{self.subset_title.replace(' ', '_').lower()}{col.lower()}_bar_plot.png")
            plt.show()
            
    def countplots(self, n=5, saved=False):
        '''Runs the countplot method from Seaborn on the top n=5 (in terms of lowest p-val) columns
        from the dataset, and then shows the plots. If the 'saved' flag is True, it will save the plts to the images
        folder to be read into the README.
        '''
        HTML(f'''<html><h1><center>{self.subset_title}</h1></center></html>''')
    


# In[143]:


def generate_and_return_obj(df: pd.DataFrame):
    # This will drop the columns that you don't want to target yet
    tmp = df[[col for col in df.columns if col not in [
        'pes_val', 'is_very_pes', 'is_very_opt', 'attitude', 'avg_family']]]

    # Create instance
    o = Attitudes_explore(tmp, target='is_pes', subset_title = 'Whole dataset with top 5 lowest p-vals')

    # Create accessable dict results
    o.run_statistical_tests()
    # Return the object that was created with the statistical tests being run
    return o
    


# In[ ]:




