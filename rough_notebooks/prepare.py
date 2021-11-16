#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

from sklearn.model_selection import train_test_split

from IPython.display import Markdown

from acquire import *


# ## It looks like the columns of `QKEY` & `WEIGHT_W41` are float64 and the rest are categories

# In[ ]:


def from_categorical_to_object(df: pd.DataFrame, exclude = ['QKEY', 'WEIGHT_W41']) -> pd.DataFrame:
    '''Takes a dataframe and a column name and will iterate through and input into an object
    and then return the dataframe with that column as an object with rows
    '''
    
    # Iterates through dataframe column names and will switch from categorical to object/string
    for col in [name for name in df.columns if name not in exclude]:
            # Targets each individual series
            df[col] = df[col].astype('str')
    
    return df


# In[ ]:


def train_validate_test_split(df: pd.DataFrame, target: str, seed=123):
    '''This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''

    train_validate, test = train_test_split(df, test_size=0.2, 

                                            random_state=seed, 

                                            stratify=df[target])

    train, validate = train_test_split(train_validate, test_size=0.3, 

                                       random_state=seed,

                                       stratify=train_validate[target])

    return train, validate, test


# In[ ]:


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    '''Will take the American Trends Dataframe and rename the columns to a less verbose name
    then it will return that new dataframe
    '''
    
    # Manual renaming of the columns to a name that is more indicative of the question
    manual_dict = {
        'FTRWORRYa_W41': 'worry_economy',
        'FTRWORRYb_W41': 'worry_public_schools',
        'FTRWORRYc_W41': 'worry_government',
        'FTRWORRYd_W41': 'worry_leaders',
        'FTRWORRYe_W41': 'worry_morals',
        'FTRWORRYf_W41': 'worry_climate',
        'ELDCARE_W41eldcare': 'elder_care',
        'ELDFINANCEF1_W41': 'elder_finance_1',
        'ELDFINANCEF2_W41': 'elder_finance_2',
        'GOVPRIOa_W41': 'priority_debt',
        'GOVPRIOb_W41': 'priority_education',
        'GOVPRIOc_W41': 'priority_healthcare',
        'GOVPRIOd_W41': 'priority_science',
        'GOVPRIOe_W41': 'priority_inequality',
        'GOVPRIOfF1_W41': 'priority_reduce_military',
        'GOVPRIOgF1_W41': 'priority_undocumented_immigration',
        'GOVPRIOhF1_W41': 'priority_reduce_social_security',
        'GOVPRIOjF1_W41': 'priority_increase_spending_infrastructure',
        'GOVPRIOjF1_W41': 'priority_avoid_tax_increase',
        'GOVPRIOkF2_W41': 'priority_increase_military',
        'GOVPRIOlF2_W41': 'priority_more_immigration',
        'GOVPRIOhF1_W41': 'priority_increase_social_security',
        'GOVPRIOnF2_W41': 'priority_reducing_spending_infrastructure',
        'GOVPRIOoF2_W41': 'priority_climate',
        'SOLVPROBa_W41': 'sci_tech',
        'SOLVPROBb_W41': 'major_corps',
        'SOLVPROBc_W41': 'rel_groups',
        'SOLVPROBdF1_W41': 'gov_in_wash',
        'SOLVPROBeF2_W41': 'state_local',
        'SOLVPROBf_W41': 'media',
        'SOLVPROBg_W41': 'military',
        'SOLVPROBh_W41': 'college_uni',
        'SOLVPROBi_W41': 'schools',
        'HARASS1F1a_W41': 'harass_false_f1',
        'HARASS1F1b_W41': 'harass_fired_f1',
        'HARASS1F1c_W41': 'harass_unpunished_f1',
        'HARASS1F1d_W41': 'harass_unbelieved_f1',
        'HARASS1NOWRKF2a_W41': 'harass_false_f2',
        'HARASS1NOWRKF2c_W41': 'harass_unpunished_f2',
        'HARASS1NOWRKF2d_W41': 'harass_unbelieved_f2',
        'HARASS3F1_W41': 'harass_interactions_f1',
        'HARASS3NOWRKF2_W41': 'harass_interactions_f2',
        'HARASS4_W41': 'harass_personal_exp',
        'HARASS5_W41': 'harass_sexual_personal_exp',
        'GNATPROB_W41': 'worries_federal_government',
        'WRKTRN1F1_W41': 'most_responsible_for_workers_f1',
        'WRKTRN2F1_W41': 'most_responsible_for_workers_f2',
        'WRKTRN2F1_W41': 'second_most_responsible_for_workers_f1',
        'WRKTRN2F2_W41': 'second_most_responsible_for_workers_f2',
        'JOBSECURITY_W41': 'job_security',
        'JOBBENEFITS_W41': 'job_benefits',
        'AUTOWKPLC_W41': 'automation_good_or_bad',
        'ROBWRK_W41': 'replacement_by_robots_likelihood',
        'ROBWRK2_W41': 'replacement_by_robots_good_or_bad',
        'AUTOLKLY_W41': 'likelihood_my_job_replaced_by_robots',
        'ROBIMPACTa_W41': 'robot_replacement_increase_inequality',
        'ROBIMPACTb_W41': 'robot_replacement_means_better_jobs_for_humans',
        'LEGALIMG_W41': 'legal_immigration_levels',
        'FUTRCLASSa_W41': 'share_americans_in_upper_class',
        'FUTRCLASSb_W41': 'share_americans_in_middle_class',
        'FUTRCLASSc_W41': 'share_americans_in_lower_class',
        'F_EDUCCAT': 'highest_education_three_categories',
        'F_EDUCCAT2': 'highest_education_six_categories',
        'F_HISP':'hispanic_or_latino',
        'F_RACECMB': 'race', 
        'F_RACETHN': 'race_and_ethnicity',
        'F_NATIVITY': 'birthplace',
        'F_CITIZEN': 'us_citizen',
        'F_MARITAL': 'marital_status',
        'F_RELIG': 'religion',
        'F_BORN': 'evangelical_christian',
        'F_ATTEND': 'church_attendance',
        'F_PARTY_FINAL': 'political_party_identity',
        'F_PARTYLN_FINAL': 'political_party_lean',
        'F_PARTYSUM_FINAL': 'summary_of_political_party_data',
        'F_INCOME': 'family_income_nine_categories',
        'F_INCOME_RECODE': 'family_income_three_categories',
        'F_REG': 'registered_to_vote',
        'F_IDEO': 'political_views',
        'F_INTUSER': 'internet_access',
        'F_VOLSUM': 'volunteer',
        'NEW_Device_Type_W41' : 'device_type',
        'F_LANGUAGE' : 'language',
        'FORM_W41' : 'form',
        'OPTIMIST_W41' : 'attitude',
        'AVGFAM_W41' : 'avg_family',
        'HAPPENa_W41' : 'happen_general',
        'HAPPENb_W41' : 'happen_health',
        'HAPPENc_W41' : 'happen_race',
        'HAPPENd_W41' : 'happen_usa',
        'HAPPENe_W41' : 'happen_wealthgap',
        'HAPPENf_W41' : 'happen_pub_ed',
        'HAPPENg_W41' : 'happen_rel',
        'HAPPENhF1_W41' : 'happen_65up_f1',
        'HAPPENiF2_W41' : 'happen_child_f2',
        'HAPPENj_W41' : 'happen_politics',
        'HAPPEN2a_W41' : 'happen_terroist',
        'HAPPEN2b_W41' : 'happen_energy',
        'HAPPEN2c_W41' : 'happen_alzheimers',
        'HAPPEN2d_W41' : 'happen_china',
        'HAPPEN2e_W41' : 'happen_female_pres',
        'HAPPEN2f_W41' : 'happen_hispanic_pres',
        'HAPPEN2g_W41' : 'happen_70yr_labor',
        'HAPPEN2h_W41' : 'happen_anti_semitism',
        'NATDEBT_W41' : 'debt_30yrs',
        'ENVC_W41' : 'envir_50yrs',
        'POPPROB_W41' : 'pop_growth',
        'ELDCARE_W41' : 'elder_care',
        'GOVPRIOiF1_W41' : 'priority_infra_f1',
        'GOVPRIOmF2_W41' : 'priority_pub_hcare_f2',
        'WRKTRN1F2_W41' : 'job_skills_f2',
        'ETHNCMAJMOD_W41' : 'ethnic_impact1',
        'ETHNCMAJ3_W41' : 'ethnic_conflict',
        'ETHNCMAJ4_W41' : 'ethnic_customs',
        'AGEMAJ_W41' : 'age_impact',
        'INTRMAR_W41' : 'inter_mar',
        'SSMONEY_W41' : 'ss_money',
        'SSCUT_W41' : 'ss_cut',
        'FUTR_ABR_W41' : 'fut_abortion',
        'FUTR_DIV_W41' : 'fut_divorce',
        'FUTR_M_W41' : 'fut_marriage',
        'FUTR_K_W41' : 'fut_kids',
        'F_METRO' : 'metro',
        'F_CREGION' : 'census_region',
        'F_AGECAT' : 'age',
        'F_SEX' : 'sex',
        'QKEY': 'qkey',
        'WEIGHT_W41': 'weight'
    }
    
    # Replace the column names and return the new dataframe
    return df.rename(columns=manual_dict)


# In[ ]:


def create_target_columns(df: pd.DataFrame, target: str) -> pd.DataFrame:
    '''Takes in a DataFrame and the target column and will add an int column 
    nammed `is_pes` where it is 1 if they answered any of the pessimistic question feelings
    and 0 otherwise.
    
    It will also add another column, named `pes_val` where the higher the value (highest of 3) is
    the most pesimistic answer and 0 is the lowest, being very optimistic. 
    
    `is_very_pes` is 1 if 'Very pessimistic' was answered and 0 otherwise
    
    `is_very_opt` is 1 if 'Very optimistic' was answered and 0 otherwise
    
    
    '''
    def find_boolean_and_value(x):
        '''Checks to see if the response is pessimistic or not and assigns an int and a boolean value
        to the response.
        '''
        if x == 'Very pessimistic':
            # is_pes, pes_val, is_very_pes, is_very_opt
            return 1, 3, 1, 0
        elif x == 'Somewhat pessimistic':
            # is_pes, pes_val, is_very_pes, is_very_opt
            return 1, 2, 0, 0
        elif x == 'Somewhat optimistic':
            # is_pes, pes_val, is_very_pes, is_very_opt
            return 0, 1, 0, 0
        else:    # Very optimistic
            # is_pes, pes_val, is_very_pes, is_very_opt
            return 0, 0, 0, 1

    # Iterate through each row and pass the target col to the function and return the tuple of values
    # into a MultiIndex in pandas, then expand that index into the new columns
    df[['is_pes', 'pes_val', 'is_very_pes', 'is_very_opt']] = df.apply(lambda x: find_boolean_and_value(x[target]), axis=1, result_type='expand')
        
    # Return the new dataframe
    return df


# In[ ]:


def convert_responses_to_numeric(df: pd.DataFrame, exclude_cols: list) -> (pd.DataFrame, dict, dict):
    '''Takes a dataframe and exclude columns list and will go through each of the values and maps them to
    an associated mapping and will return the mapping for the revert_key and the replacement_key
    '''
    # Remove the columns that you do not want the key-value replacement mapping to be performed on
    columns = [col for col in df.columns if col not in exclude_cols]
    
    # Origin Replacement Key Values - This will revert back to original values/responses
    revert_key_values = dict()
    
    # Replacement Key Values - This will change the values/responses to dummy values
    replacement_key_values = dict()
    
    # Iterate though each column
    for col in columns:
        # Select the series
        s = df[col]
        # Fetch the unique values from the series
        uniques = s.unique()
        
        # Build the series replacement dictionary
        temp_replace_dict = dict()
        
        # Build revert replacement dictionary
        temp_revert_dict = dict()
        
        # Enumerate through the unique values to assign the integers to the value
        for new_val, response in enumerate(uniques):
            # define the key for the replacement dic
            temp_replace_dict[response] = new_val
            # define the key for the replacement 
            temp_revert_dict[new_val] = response
            
        # Define the columns replacement values
        replacement_key_values[col] = temp_replace_dict

        # Define the columns for reversion dicts
        revert_key_values[col] = temp_revert_dict
    
    return revert_key_values, replacement_key_values
    


# In[ ]:


def wrangle_data():
    ''' Wrangles data and returns df, revert_key, and replace_key
    '''
    # Get origin data from the folder
    df = get_atp_w41_spss_data()

    # Convert the datafrom Categorical to Object/string
    df = from_categorical_to_object(df)

    # Remove optimisim_refused from the dataframe
    df = df[df.OPTIMIST_W41 != 'Refused']
    
    # Renames the columns and returns the renamed dataframe
    df = rename_columns(df)
    
    # Create the boolean and value columns from the target columns
    df = create_target_columns(df, 'attitude')
    
    # Creates a revert_key and replacement key with excluded columns ### INCLUDE ANY NEW TARGET COLS ###
    revert_key, replace_key = convert_responses_to_numeric(df, exclude_cols=[
        'qkey', 'weight', 'is_pes', 'pes_val', 'is_very_pes', 'is_very_opt'])
    
    # Change the qkey from float to an int
    df['qkey'] = df.qkey.astype('int')
    
    return df, revert_key, replace_key


# In[ ]:


if __name__ == '__main__':
    # Manual dict to input into into the tmp table to format and return for README
    manual_dict = {
        'FTRWORRYa_W41': 'worry_economy',
        'FTRWORRYb_W41': 'worry_public_schools',
        'FTRWORRYc_W41': 'worry_government',
        'FTRWORRYd_W41': 'worry_leaders',
        'FTRWORRYe_W41': 'worry_morals',
        'FTRWORRYf_W41': 'worry_climate',
        'ELDCARE_W41eldcare': 'elder_care',
        'ELDFINANCEF1_W41': 'elder_finance_1',
        'ELDFINANCEF2_W41': 'elder_finance_2',
        'GOVPRIOa_W41': 'priority_debt',
        'GOVPRIOb_W41': 'priority_education',
        'GOVPRIOc_W41': 'priority_healthcare',
        'GOVPRIOd_W41': 'priority_science',
        'GOVPRIOe_W41': 'priority_inequality',
        'GOVPRIOfF1_W41': 'priority_reduce_military',
        'GOVPRIOgF1_W41': 'priority_undocumented_immigration',
        'GOVPRIOhF1_W41': 'priority_reduce_social_security',
        'GOVPRIOjF1_W41': 'priority_increase_spending_infrastructure',
        'GOVPRIOjF1_W41': 'priority_avoid_tax_increase',
        'GOVPRIOkF2_W41': 'priority_increase_military',
        'GOVPRIOlF2_W41': 'priority_more_immigration',
        'GOVPRIOhF1_W41': 'priority_increase_social_security',
        'GOVPRIOnF2_W41': 'priority_reducing_spending_infrastructure',
        'GOVPRIOoF2_W41': 'priority_climate',
        'SOLVPROBa_W41': 'sci_tech',
        'SOLVPROBb_W41': 'major_corps',
        'SOLVPROBc_W41': 'rel_groups',
        'SOLVPROBdF1_W41': 'gov_in_wash',
        'SOLVPROBeF2_W41': 'state_local',
        'SOLVPROBf_W41': 'media',
        'SOLVPROBg_W41': 'military',
        'SOLVPROBh_W41': 'college_uni',
        'SOLVPROBi_W41': 'schools',
        'HARASS1F1a_W41': 'harass_false_f1',
        'HARASS1F1b_W41': 'harass_fired_f1',
        'HARASS1F1c_W41': 'harass_unpunished_f1',
        'HARASS1F1d_W41': 'harass_unbelieved_f1',
        'HARASS1NOWRKF2a_W41': 'harass_false_f2',
        'HARASS1NOWRKF2c_W41': 'harass_unpunished_f2',
        'HARASS1NOWRKF2d_W41': 'harass_unbelieved_f2',
        'HARASS3F1_W41': 'harass_interactions_f1',
        'HARASS3NOWRKF2_W41': 'harass_interactions_f2',
        'HARASS4_W41': 'harass_personal_exp',
        'HARASS5_W41': 'harass_sexual_personal_exp',
        'GNATPROB_W41': 'worries_federal_government',
        'WRKTRN1F1_W41': 'most_responsible_for_workers_f1',
        'WRKTRN2F1_W41': 'most_responsible_for_workers_f2',
        'WRKTRN2F1_W41': 'second_most_responsible_for_workers_f1',
        'WRKTRN2F2_W41': 'second_most_responsible_for_workers_f2',
        'JOBSECURITY_W41': 'job_security',
        'JOBBENEFITS_W41': 'job_benefits',
        'AUTOWKPLC_W41': 'automation_good_or_bad',
        'ROBWRK_W41': 'replacement_by_robots_likelihood',
        'ROBWRK2_W41': 'replacement_by_robots_good_or_bad',
        'AUTOLKLY_W41': 'likelihood_my_job_replaced_by_robots',
        'ROBIMPACTa_W41': 'robot_replacement_increase_inequality',
        'ROBIMPACTb_W41': 'robot_replacement_means_better_jobs_for_humans',
        'LEGALIMG_W41': 'legal_immigration_levels',
        'FUTRCLASSa_W41': 'share_americans_in_upper_class',
        'FUTRCLASSb_W41': 'share_americans_in_middle_class',
        'FUTRCLASSc_W41': 'share_americans_in_lower_class',
        'F_EDUCCAT': 'highest_education_three_categories',
        'F_EDUCCAT2': 'highest_education_six_categories',
        'F_HISP':'hispanic_or_latino',
        'F_RACECMB': 'race', 
        'F_RACETHN': 'race_and_ethnicity',
        'F_NATIVITY': 'birthplace',
        'F_CITIZEN': 'us_citizen',
        'F_MARITAL': 'marital_status',
        'F_RELIG': 'religion',
        'F_BORN': 'evangelical_christian',
        'F_ATTEND': 'church_attendance',
        'F_PARTY_FINAL': 'political_party_identity',
        'F_PARTYLN_FINAL': 'political_party_lean',
        'F_PARTYSUM_FINAL': 'summary_of_political_party_data',
        'F_INCOME': 'family_income_nine_categories',
        'F_INCOME_RECODE': 'family_income_three_categories',
        'F_REG': 'registered_to_vote',
        'F_IDEO': 'political_views',
        'F_INTUSER': 'internet_access',
        'F_VOLSUM': 'volunteer',
        'NEW_Device_Type_W41' : 'device_type',
        'F_LANGUAGE' : 'language',
        'FORM_W41' : 'form',
        'OPTIMIST_W41' : 'attitude',
        'AVGFAM_W41' : 'avg_family',
        'HAPPENa_W41' : 'happen_general',
        'HAPPENb_W41' : 'happen_health',
        'HAPPENc_W41' : 'happen_race',
        'HAPPENd_W41' : 'happen_usa',
        'HAPPENe_W41' : 'happen_wealthgap',
        'HAPPENf_W41' : 'happen_pub_ed',
        'HAPPENg_W41' : 'happen_rel',
        'HAPPENhF1_W41' : 'happen_65up_f1',
        'HAPPENiF2_W41' : 'happen_child_f2',
        'HAPPENj_W41' : 'happen_politics',
        'HAPPEN2a_W41' : 'happen_terroist',
        'HAPPEN2b_W41' : 'happen_energy',
        'HAPPEN2c_W41' : 'happen_alzheimers',
        'HAPPEN2d_W41' : 'happen_china',
        'HAPPEN2e_W41' : 'happen_female_pres',
        'HAPPEN2f_W41' : 'happen_hispanic_pres',
        'HAPPEN2g_W41' : 'happen_70yr_labor',
        'HAPPEN2h_W41' : 'happen_anti_semitism',
        'NATDEBT_W41' : 'debt_30yrs',
        'ENVC_W41' : 'envir_50yrs',
        'POPPROB_W41' : 'pop_growth',
        'ELDCARE_W41' : 'elder_care',
        'GOVPRIOiF1_W41' : 'priority_infra_f1',
        'GOVPRIOmF2_W41' : 'priority_pub_hcare_f2',
        'WRKTRN1F2_W41' : 'job_skills_f2',
        'ETHNCMAJMOD_W41' : 'ethnic_impact1',
        'ETHNCMAJ3_W41' : 'ethnic_conflict',
        'ETHNCMAJ4_W41' : 'ethnic_customs',
        'AGEMAJ_W41' : 'age_impact',
        'INTRMAR_W41' : 'inter_mar',
        'SSMONEY_W41' : 'ss_money',
        'SSCUT_W41' : 'ss_cut',
        'FUTR_ABR_W41' : 'fut_abortion',
        'FUTR_DIV_W41' : 'fut_divorce',
        'FUTR_M_W41' : 'fut_marriage',
        'FUTR_K_W41' : 'fut_kids',
        'F_METRO' : 'metro',
        'F_CREGION' : 'census_region',
        'F_AGECAT' : 'age',
        'F_SEX' : 'sex',
        'QKEY': 'qkey',
        'WEIGHT_W41': 'weight'
    }
    tmp = list()
    for k,v in manual_dict.items():
        tmp.append({'Original_Column_Name': f'<code>{k}</code>',
                    '': '&rarr;',
                    'New_Column_Name': f'<code>{v}</code>'})
    _ = pd.DataFrame(tmp).set_index('Original_Column_Name')

    print(_.to_markdown())


# In[ ]:




