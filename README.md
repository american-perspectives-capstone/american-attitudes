<center><h1>American Attitude Topic Sentiment Prediction</center>

<a name ='toc'></a>
# Table of Contents 
1. [Project Planning](#project_planning)
    1. [Project Objectives](#project_objectives)
    2. [Business Goals](#business_goals)
    3. [Audience](#audience)
    4. [Deliverables](#deliverables)
2. [Executive Summary](#exe_sum)
    1. [Goals](#goals)
    2. [Findings](#findings)
3. [Acquire Data](#acquire)
    1. [Working with American Trends Panel Data](#working_with_data)
    2. [Data Dictonary](#data_dict) 
    3. [Acquire Takeaways](#acquire_takeaways)
4. [Prepare Data](#prep_data)
    1. [Distributions](#distributions)
    2. [Prepare Takeaways](#prepare_takeaways)
5. [Data Exploration](#explore)
    1. [Correlations](#correlations)
    2. [Pairplot](#pairplot)
    3. [Hypothesis & Testing](#hypotheses)
    4. [Explore Takeaways](#explore_takeaways)
6. [Modeling & Evaluation](#modeling)
    1. [Cross-Validation](#cross_validation)
    2. [Modeling Takeaways](#modeling_takeaways)
7. [Project Delivery](#delivery)
    1. [Conclusion & Next Steps](#conclusion_and_next_steps)
    2. [Project Replication](#replicate)
    3. [Data Use Agreements](#data_use)

<hr style="border-top: 10px groove tan; margin-top: 5px; margin-bottom: 5px"></hr>

<a name='project_planning'></a>
# Project Planning
✓ 🟢 **Plan** ➜ ☐ _Acquire_ ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

<a name='project_objectives'></a>
## Project Objectives 
> - Utilize American Trends Panel Datasets (accessable <a href="https://www.kaggle.com/shankanater/american-trends-panel-pewresearch/download">here</a>), with Natural Language Processing techniques to assess and attempt to predict sentiment toward particular topics.
> - This will culminate into a well-built well-documented jupyter notebook that contains our process and derivation of these predictions.
> - Modules will be created that abstract minutiae aspects of the data pipeline process.

<a name='business_goals'></a>
## Business Goals 
> - Utilize tabulated statistical data aquired from Pew Research American Trends Surveys.
> - Prepare, explore and formulate hypthoesis about the data.
> - Build models that can predict future American sentiment toward certain topics, and utilize hyperparameter optimization and feature engineering to improve validation model performance prior to evaluating on test data.
> - Document all these steps throughly.

<a name='audience'></a>
## Audience 
> - General population and individuals without specific knowledge or understanding of the topic or subject.

<a name='deliverables'></a>
## Deliverables
> - A clearly named final notebook. This notebook will contain more detailed processes other than noted within the README and have abstracted scripts to assist on readability.
> - A README that explains what the project is, how to reproduce the project, and notes about the project.
> - A Python module and associated modules that automate the data acquisition and preparation process. 

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='exe_sum'></a>
# Executive Summary
> - 
> - 
> - 

<a name='goals'></a>
## Goals
> - Build a model that can predict future American sentiment toward certain topics, utilizing split survey data as the training dataset.

<a name='findings'></a>
## Findings
> - 

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='acquire'></a>
# Acquire Data
✓ _Plan_ ➜ 🟢 **Acquire** ➜ ☐ _Prepare_ ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

> - 
> - 
> - 

<a name="working_with_data"></a>
## Working with American Trends Panel Data 

### Demographic Profile Variables
> Each ATP dataset comes with a number of variables prefixed by “F_” (for “frame”) that contain demographic profile data. These variables are not measured every wave; instead, they are sourced from panel profile surveys conducted on a less frequent basis. Some profile variables are also occasionally asked on panel waves and are accordingly updated for each panelist. Profile information is based on panelists’ most recent response to the profile questions. Some variables are coarsened to help protect the confidentiality of our panelists. Interviewer instructions in `[ ]` and voluntary responses in `( )` are included if the source of a profile variable was ever presented in phone (CATI) mode. See Appendix I for the profile variable codebook.

###  Unique Identifier
> The variable `QKEY` is a unique identifier assigned to each respondent. `QKEY` can be used to link multiple panel waves together. Note that except in a few instances, `WEIGHT_W41` are only provided for single waves. Use caution when analyzing data from multiple waves without weights that are designed for use with multiple waves.

### Data Variable Types
 > American Trends Panel datasets contain single-punch or multi-punch variables. For questions in a 'Check all that apply' format, each option has its own variable indicating whether a respondent selected the item or not. For some datasets there is an additional variable indicating whether a respondent did not select any of the options. Open-end string variables are not included in ATP datasets. Coded responses to open-end questions are included when available.

### Dataset Format
> The dataset is formatted as a .sav file and can be read with the SPSS software program. The dataset can also be read with the R programming language, using the `foreign` package. R is a free, open-source program for statistical analysis that can be downloaded <a href="https://cran.r-project.org/">here</a>. It can also be used to export data in .csv format for use with other software programs.

> **NOTE**: Using other tools to directly convert the .sav file to another format such as .csv may ERASE value
labels. For this reason, it is highly recommended that you use either SPSS or R to read the file directly.

<a name='data_dict'></a>
## DataFrame Dictionary

<table>
    <th>Variable</th><th>Name</th><th>Description</th>
    <tr>
        <td><code>NEW_Device_Type_W41</code>
        <td>Type of device</td>
        <td>
    <ul>1 Mobile phone</ul>
<ul>2 Desktop</ul>
<ul>3 Tablet</ul>
</td>
    </tr>
    <tr>
        <td><code>F_LANGUAGE</code>
        <td>Type of spoken language</td>
        <td>
    <ul>1 English</ul>
<ul>2 Spanish</ul>
</td>
    </tr>
    <tr>
        <td><code>FORM_W41</code>
        <td>Which survey form was used</td>
        <td>
    <ul>1 Form 1</ul>
<ul>2 Form 2</ul>
</td>
    </tr>
    <tr>
        <td><code>OPTIMIST_W41</code>
        <td>Their judge on their optimisim</td>
        <td>
    <ul>1 Somewhat optimistic</ul>
<ul>2 Somewhat pessimistic</ul>
<ul>3 Very optimistic</ul>
<ul>4 Very pessimistic</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>AVGFAM_W41</code>
        <td>Average family outlook</td>
        <td>
    <ul>1 Get worse</ul>
<ul>2 Get better</ul>
<ul>3 Stay about the same</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENa_W41</code>
        <td>What do you think will happen to the economy in the future?</td>
        <td>
    <ul>1 The U.S. economy will be STRONGER</ul>
<ul>2 The U.S. economy will be WEAKER</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENb_W41</code>
        <td>What do you think will happen to healthcare in the future?</td>
        <td>
    <ul>1 Health care will be MORE affordable</ul>
<ul>2 Health care will be LESS affordable</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENc_W41</code>
        <td>What do you think will happen race relations in the future?</td>
        <td>
    <ul>1 Race relations will IMPROVE</ul>
<ul>2 Race relations will GET WORSE</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENd_W41</code>
        <td>What do you think will happen the United States importance in the future?</td>
        <td>
    <ul>1 The U.S. will be MORE important in the world</ul>
<ul>2 The U.S. will be LESS important in the world</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENe_W41</code>
        <td>What do you think will happen to wealth gap in the future?</td>
        <td>
    <ul>1 The gap between the rich and the poor will GROW</ul>
<ul>2 The gap between the rich and the poor will GET SMALLER</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENf_W41</code>
        <td>None</td>
        <td>
    <ul>1 The public education system will GET WORSE</ul>
<ul>2 The public education system will IMPROVE</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENg_W41</code>
        <td>None</td>
        <td>
    <ul>1 Religion will become LESS important</ul>
<ul>2 Religion will be ABOUT AS important as it is now</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENhF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 People 65 and older will have a WORSE standard of living</ul>
<ul>2 Refused</ul>
<ul>3 People 65 and older will have a BETTER standard of living</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENiF2_W41</code>
        <td>None</td>
        <td>
<ul>1 Children will have a BETTER standard of living</ul>
<ul>2 Children will have a WORSE standard of living</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPENj_W41</code>
        <td>None</td>
        <td>
    <ul>1 The country will be LESS politically divided</ul>
<ul>2 The country will be MORE politically divided</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPEN2a_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPEN2b_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
    </tr>
    <tr>
        <td><code>HAPPEN2c_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPEN2d_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
    </tr>
    <tr>
        <td><code>HAPPEN2e_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPEN2f_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HAPPEN2g_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will definitely happen</ul>
<ul>3 Will probably happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
    </tr>
    <tr>
        <td><code>HAPPEN2h_W41</code>
        <td>None</td>
        <td>
    <ul>1 Will probably not happen</ul>
<ul>2 Will probably happen</ul>
<ul>3 Will definitely happen</ul>
<ul>4 Will definitely not happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>NATDEBT_W41</code>
        <td>None</td>
        <td>
    <ul>1 Stay about the same</ul>
<ul>2 Grow larger</ul>
<ul>3 Refused</ul>
<ul>4 Be reduced</ul>
<ul>5 Be eliminated</ul>
</td>
    </tr>
    <tr>
        <td><code>ENVC_W41</code>
        <td>None</td>
        <td>
    <ul>1 Worse than it is now</ul>
<ul>2 About the same as it is now</ul>
<ul>3 Better than it is now</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>POPPROB_W41</code>
        <td>None</td>
        <td>
    <ul>1 Minor problem</ul>
<ul>2 Major problem</ul>
<ul>3 Not a problem</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FTRWORRYa_W41</code>
        <td>None</td>
        <td>
    <ul>1 Not too worried</ul>
<ul>2 Fairly worried</ul>
<ul>3 Very worried</ul>
<ul>4 Not at all worried</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FTRWORRYb_W41</code>
        <td>None</td>
        <td>
    <ul>1 Fairly worried</ul>
<ul>2 Very worried</ul>
<ul>3 Not too worried</ul>
<ul>4 Not at all worried</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FTRWORRYc_W41</code>
        <td>None</td>
        <td>
    <ul>1 Fairly worried</ul>
<ul>2 Very worried</ul>
<ul>3 Not too worried</ul>
<ul>4 Not at all worried</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FTRWORRYd_W41</code>
        <td>None</td>
        <td>
    <ul>1 Fairly worried</ul>
<ul>2 Very worried</ul>
<ul>3 Not too worried</ul>
<ul>4 Not at all worried</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FTRWORRYe_W41</code>
        <td>None</td>
        <td>
    <ul>1 Fairly worried</ul>
<ul>2 Very worried</ul>
<ul>3 Not too worried</ul>
<ul>4 Not at all worried</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FTRWORRYf_W41</code>
        <td>None</td>
        <td>
    <ul>1 Not too worried</ul>
<ul>2 Not at all worried</ul>
<ul>3 Very worried</ul>
<ul>4 Fairly worried</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ELDCARE_W41</code>
        <td>None</td>
        <td>
    <ul>1 LESS prepared financially for retirement than older adults today</ul>
<ul>2 BETTER prepared financially for retirement than older adults are today</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ELDFINANCEF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 Family members</ul>
<ul>2 Older Americans themselves</ul>
<ul>3 Government</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ELDFINANCEF2_W41</code>
        <td>None</td>
        <td>
<ul>1 Government</ul>
<ul>2 Family members</ul>
<ul>3 Older Americans themselves</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOa_W41</code>
        <td>None</td>
        <td>
    <ul>1 A lower priority</ul>
<ul>2 A top priority</ul>
<ul>3 An important, but not a top priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOb_W41</code>
        <td>None</td>
        <td>
    <ul>1 An important, but not a top priority</ul>
<ul>2 A top priority</ul>
<ul>3 Should not be done</ul>
<ul>4 A lower priority</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOc_W41</code>
        <td>None</td>
        <td>
    <ul>1 A lower priority</ul>
<ul>2 A top priority</ul>
<ul>3 An important, but not a top priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOd_W41</code>
        <td>None</td>
        <td>
    <ul>1 An important, but not a top priority</ul>
<ul>2 A lower priority</ul>
<ul>3 Should not be done</ul>
<ul>4 A top priority</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOe_W41</code>
        <td>None</td>
        <td>
    <ul>1 A top priority</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A lower priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOfF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 A lower priority</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 Should not be done</ul>
<ul>4 A top priority</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOgF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 A top priority</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A lower priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOhF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 A top priority</ul>
<ul>2 Should not be done</ul>
<ul>3 An important, but not a top priority</ul>
<ul>4 A lower priority</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOiF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 A top priority</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A lower priority</ul>
<ul>4 Should not be done</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOjF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 A top priority</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A lower priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOkF2_W41</code>
        <td>None</td>
        <td>
<ul>1 An important, but not a top priority</ul>
<ul>2 A lower priority</ul>
<ul>3 A top priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOlF2_W41</code>
        <td>None</td>
        <td>
<ul>1 Should not be done</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A lower priority</ul>
<ul>4 A top priority</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOmF2_W41</code>
        <td>None</td>
        <td>
<ul>1 A top priority</ul>
<ul>2 A lower priority</ul>
<ul>3 An important, but not a top priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOnF2_W41</code>
        <td>None</td>
        <td>
<ul>1 Should not be done</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A top priority</ul>
<ul>4 A lower priority</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GOVPRIOoF2_W41</code>
        <td>None</td>
        <td>
<ul>1 A top priority</ul>
<ul>2 An important, but not a top priority</ul>
<ul>3 A lower priority</ul>
<ul>4 Should not be done</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>GNATPROB_W41</code>
        <td>None</td>
        <td>
    <ul>1 That the government will be too involved in problems that should be left to businesses and individuals</ul>
<ul>2 That the government will do too little to solve problems facing the country</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>WRKTRN1F1_W41</code>
        <td>None</td>
        <td>
    <ul>1 Employers</ul>
<ul>2 Individuals themselves</ul>
<ul>3 Government</ul>
<ul>4 The education system</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>WRKTRN1F2_W41</code>
        <td>None</td>
        <td>
<ul>1 Individuals themselves</ul>
<ul>2 The education system</ul>
<ul>3 Government</ul>
<ul>4 Employers</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>WRKTRN2F1_W41</code>
        <td>None</td>
        <td>
    <ul>1 The education system</ul>
<ul>2 Employers</ul>
<ul>3 Individuals themselves</ul>
<ul>4 Government</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>WRKTRN2F2_W41</code>
        <td>None</td>
        <td>
<ul>1 The education system</ul>
<ul>2 Government</ul>
<ul>3 Individuals themselves</ul>
<ul>4 Employers</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>JOBSECURITY_W41</code>
        <td>None</td>
        <td>
    <ul>1 Less job security</ul>
<ul>2 About the same</ul>
<ul>3 More job security</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>JOBBENEFITS_W41</code>
        <td>None</td>
        <td>
    <ul>1 Not as good as they are now</ul>
<ul>2 About the same as they are now</ul>
<ul>3 Better than they are now</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>AUTOWKPLC_W41</code>
        <td>None</td>
        <td>
    <ul>1 Neither helped nor hurt</ul>
<ul>2 Mostly hurt American workers</ul>
<ul>3 Mostly helped American workers</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ROBWRK_W41</code>
        <td>None</td>
        <td>
    <ul>1 Probably not happen</ul>
<ul>2 Probably happen</ul>
<ul>3 Definitely happen</ul>
<ul>4 Definitely not happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ROBWRK2_W41</code>
        <td>None</td>
        <td>
<ul>1 A very bad thing for the country</ul>
<ul>2 A somewhat bad thing for the country</ul>
<ul>3 A somewhat good thing for the country</ul>
<ul>4 A very good thing for the country</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>AUTOLKLY_W41</code>
        <td>None</td>
        <td>
    <ul>1 Definitely not happen</ul>
<ul>2 Probably happen</ul>
<ul>3 Probably not happen</ul>
<ul>4 Definitely happen</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ROBIMPACTa_W41</code>
        <td>None</td>
        <td>
    <ul>1 Yes, likely</ul>
<ul>2 No, not likely</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ROBIMPACTb_W41</code>
        <td>None</td>
        <td>
    <ul>1 No, not likely</ul>
<ul>2 Yes, likely</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>LEGALIMG_W41</code>
        <td>None</td>
        <td>
    <ul>1 Maintained at current levels</ul>
<ul>2 Decreased</ul>
<ul>3 Increased</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTRCLASSa_W41</code>
        <td>None</td>
        <td>
    <ul>1 Increase</ul>
<ul>2 Decrease</ul>
<ul>3 Stay about the same</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTRCLASSb_W41</code>
        <td>None</td>
        <td>
    <ul>1 Stay about the same</ul>
<ul>2 Decrease</ul>
<ul>3 Increase</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTRCLASSc_W41</code>
        <td>None</td>
        <td>
    <ul>1 Increase</ul>
<ul>2 Decrease</ul>
<ul>3 Stay about the same</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1F1a_W41</code>
        <td>None</td>
        <td>
    <ul>1 Major problem</ul>
<ul>2 Minor problem</ul>
<ul>3 Not a problem</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1F1b_W41</code>
        <td>None</td>
        <td>
    <ul>1 Major problem</ul>
<ul>3 Minor problem</ul>
<ul>4 Not a problem</ul>
<ul>2 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1F1c_W41</code>
        <td>None</td>
        <td>
    <ul>1 Minor problem</ul>
<ul>2 Major problem</ul>
<ul>3 Not a problem</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1F1d_W41</code>
        <td>None</td>
        <td>
    <ul>1 Minor problem</ul>
<ul>2 Major problem</ul>
<ul>3 Not a problem</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1NOWRKF2a_W41</code>
        <td>None</td>
        <td>
<ul>2 Minor problem</ul>
<ul>3 Major problem</ul>
<ul>4 Not a problem</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1NOWRKF2c_W41</code>
        <td>None</td>
        <td>
    <ul>1 Minor problem</ul>
<ul>2 Major problem</ul>
<ul>3 Not a problem</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS1NOWRKF2d_W41</code>
        <td>None</td>
        <td>
    <ul>1 Minor problem</ul>
<ul>2 Major problem</ul>
<ul>3 Not a problem</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS3F1_W41</code>
        <td>None</td>
        <td>
    <ul>1 Has made it harder for men</ul>
<ul>2 Hasn't made much difference</ul>
<ul>3 Has made it easier for men</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS3NOWRKF2_W41</code>
        <td>None</td>
        <td>
<ul>1 Hasn't made much difference</ul>
<ul>2 Has made it harder for men</ul>
<ul>3 Has made it easier for men</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS4_W41</code>
        <td>None</td>
        <td>
    <ul>1 No</ul>
<ul>2 Yes</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>HARASS5_W41</code>
        <td>None</td>
        <td>
<ul>1 Both</ul>
<ul>2 In a professional or work setting</ul>
<ul>3 Outside of a professional or work setting</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ETHNCMAJMOD_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat good thing</ul>
<ul>2 A somewhat bad thing</ul>
<ul>3 Neither a good nor bad thing</ul>
<ul>4 A very bad thing</ul>
<ul>5 A very good thing</ul>
<ul>6 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ETHNCMAJ3_W41</code>
        <td>None</td>
        <td>
    <ul>1 Fewer conflicts between racial and ethnic groups</ul>
<ul>2 Not much of an impact</ul>
<ul>3 More conflicts between racial and ethnic groups</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>ETHNCMAJ4_W41</code>
        <td>None</td>
        <td>
    <ul>1 Strengthen American customs and values</ul>
<ul>2 Weaken American customs and values</ul>
<ul>3 Not much of an impact</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>AGEMAJ_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat bad thing</ul>
<ul>2 A somewhat good thing</ul>
<ul>3 Neither a good nor bad thing</ul>
<ul>4 A very bad thing</ul>
<ul>5 A very good thing</ul>
<ul>6 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>INTRMAR_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat good thing</ul>
<ul>2 A very bad thing</ul>
<ul>3 Neither a good nor bad thing</ul>
<ul>4 A somewhat bad thing</ul>
<ul>5 A very good thing</ul>
<ul>6 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SSMONEY_W41</code>
        <td>None</td>
        <td>
    <ul>1 Yes, but at reduced levels</ul>
<ul>2 Yes, at current levels</ul>
<ul>3 No</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SSCUT_W41</code>
        <td>None</td>
        <td>
    <ul>1 Social Security benefits should not be reduced in any way</ul>
<ul>2 Some reductions in benefits for future retirees will need to be made</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTR_ABR_W41</code>
        <td>None</td>
        <td>
    <ul>1 Legal but with some restrictions</ul>
<ul>2 Legal with no restrictions</ul>
<ul>3 Illegal except in certain cases</ul>
<ul>4 Illegal with no exceptions</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTR_DIV_W41</code>
        <td>None</td>
        <td>
    <ul>1 About as likely to get divorced as people are now</ul>
<ul>2 More likely to get divorced than people are now</ul>
<ul>3 Less likely to get divorced than people are now</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTR_M_W41</code>
        <td>None</td>
        <td>
    <ul>1 More likely to get married than people are now</ul>
<ul>2 Less likely to get married than people are now</ul>
<ul>3 About as likely to get married as people are now</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>FUTR_K_W41</code>
        <td>None</td>
        <td>
    <ul>1 About as likely to have children as people are now</ul>
<ul>2 Less likely to have children than people are now</ul>
<ul>3 More likely to have children than people are now</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBa_W41</code>
        <td>None</td>
        <td>
    <ul>1 A very positive impact</ul>
<ul>2 A somewhat negative impact</ul>
<ul>3 A somewhat positive impact</ul>
<ul>4 A very negative impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBb_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat positive impact</ul>
<ul>2 A somewhat negative impact</ul>
<ul>3 A very negative impact</ul>
<ul>4 A very positive impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBc_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat positive impact</ul>
<ul>2 A somewhat negative impact</ul>
<ul>3 A very positive impact</ul>
<ul>4 A very negative impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBdF1_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat positive impact</ul>
<ul>2 A very negative impact</ul>
<ul>3 A somewhat negative impact</ul>
<ul>4 A very positive impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBeF2_W41</code>
        <td>None</td>
        <td>
<ul>1 A somewhat negative impact</ul>
<ul>2 A very positive impact</ul>
<ul>3 A very negative impact</ul>
<ul>4 A somewhat positive impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBf_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat negative impact</ul>
<ul>2 A very negative impact</ul>
<ul>3 A somewhat positive impact</ul>
<ul>4 A very positive impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBg_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat positive impact</ul>
<ul>2 A very positive impact</ul>
<ul>3 A very negative impact</ul>
<ul>4 A somewhat negative impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBh_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat positive impact</ul>
<ul>2 A very negative impact</ul>
<ul>3 A very positive impact</ul>
<ul>4 A somewhat negative impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>SOLVPROBi_W41</code>
        <td>None</td>
        <td>
    <ul>1 A somewhat positive impact</ul>
<ul>2 A very positive impact</ul>
<ul>3 A somewhat negative impact</ul>
<ul>4 A very negative impact</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_METRO</code>
        <td>Metropolitan area indicator.</td>
        <td>
    <ul>1 Metropolitan</ul>
<ul>2 Non-metropolitan</ul>
</td>
    </tr>
    <tr>
        <td><code>F_CREGION</code>
        <td>Census region.</td>
        <td>
    <ul>1 Northeast</ul>
<ul>2 South</ul>
<ul>3 Midwest</ul>
<ul>4 West</ul>
</td>
    </tr>
    <tr>
        <td><code>F_AGECAT</code>
        <td>Four-way category based on the panelist age as calculated from their date of birth. If only YOB is
available, age is calculated as calendar year July 1 – YOB. If DOB and YOB are both unavailable, age is
calculated as calendar year of recruitment survey – self-reported age at the time of recruitment. Age is
updated annually during the annual profile survey.</td>
        <td>
    <ul>1 18-29</ul>
    <ul>2 30-49</ul>
    <ul>3 50-64</ul>
    <ul>4 65+</ul>
    <ul>5 DK/REF</ul>
</td>
    </tr>
    <tr>
        <td><code>F_SEX</code>
        <td>Self-reported sex.</td>
        <td>
    <ul>1 Female</ul>
<ul>2 Male</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_EDUCCAT</code>
        <td>Three-way category coded from self-reported educational attainment.</td>
        <td>
    <ul>1 College graduate+ (EDUC_ACS =11,12,13,14)</ul>
<ul>2 H.S. graduate or less (EDUC_ACS =1,2,3,4,5,6,7)</ul>
<ul>3 Some College (EDUC_ACS =8,9,10)</ul>
<ul>4 Don't know/Refused (EDUC_ACS =Refused)</ul>
</td>
    </tr>
    <tr>
        <td><code>F_EDUCCAT2</code>
        <td>Six-way category coded from self-reported educational attainment.</td>
        <td>
     <ul>5 Less than high school (EDUC_ACS=1,2,3,4,5)</ul>
     <ul>2 High school graduate (EDUC_ACS =6,7)</ul>
     <ul>6 Some college, no degree (EDUC_ACS=8,9)</ul>
     <ul>3 Associate's degree (EDUC_ACS=10)</ul>
     <ul>4 College graduate/some post grad (EDUC_ACS =11)</ul>
     <ul>1 Postgraduate (EDUC_ACS =12,13,14)</ul>
    <ul>7 Don't know/Refused (EDUC_ACS =Refused)</ul>
</td>
    </tr>
    <tr>
        <td><code>F_HISP</code>
        <td>Are you of Hispanic, Latino, or Spanish origin, such as Mexican, Puerto Rican or Cuban?</td>
        <td>
    <ul>1 No</ul>
<ul>2 Yes</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_RACECMB</code>
        <td>Combining race.</td>
        <td>
    <ul>1 White</ul>
<ul>2 Mixed Race</ul>
<ul>3 Or some other race</ul>
<ul>4 Black or African American</ul>
<ul>5 Asian or Asian-American</ul>
<ul>6 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_RACETHN</code>
        <td>Race-ethnicity.</td>
        <td>
    <ul>1 White non-Hispanic</ul>
<ul>2 Other</ul>
<ul>3 Hispanic</ul>
<ul>4 Black non-Hispanic</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_NATIVITY</code>
        <td>Were you born in the United States, on the island of Puerto Rico, or in another country?</td>
        <td>
    <ul>1 U.S.</ul>
<ul>2 Another country</ul>
<ul>3 Puerto Rico</ul>
<ul>4 Other U.S. territory</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_CITIZEN</code>
        <td>Are you a citizen of the United States?</td>
        <td>
    <ul>1 Yes</ul>
<ul>2 No</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_MARITAL</code>
        <td>Marital status.</td>
        <td>
    <ul>1 Married</ul>
<ul>2 Divorced</ul>
<ul>3 Never been married</ul>
<ul>4 Widowed</ul>
<ul>5 Living with a partner</ul>
<ul>6 Separated</ul>
<ul>7 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_RELIG</code>
        <td>Religion.</td>
        <td>
    <ul>1 Roman Catholic</ul>
<ul>2 Protestant (for example, Baptist, Methodist, Non-denominational, Lutheran, Presbyterian, Pentecostal, Episcopalian, Refo</ul>
<ul>3 Nothing in particular</ul>
<ul>4 Atheist</ul>
<ul>5 Something else, Specify</ul>
<ul>6 Jewish</ul>
<ul>7 Agnostic</ul>
<ul>8 Mormon (Church of Jesus Christ of Latter-day Saints or LDS)</ul>
<ul>9 Hindu</ul>
<ul>10 Muslim</ul>
<ul>11 Orthodox (such as Greek, Russian, or some other Orthodox church)</ul>
<ul>12 Buddhist</ul>
<ul>13 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_BORN</code>
        <td>Born-again or evangelical Christian.</td>
        <td>
    <ul>1 No, not born-again or evangelical Christian</ul>
<ul>2 Yes, born-again or evangelical Christian</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_ATTEND</code>
        <td>Aside from weddings and funerals, how often do you attend religious services?</td>
        <td>
    <ul>1 A few times a year</ul>
<ul>2 More than once a week</ul>
<ul>3 Once a week</ul>
<ul>4 Seldom</ul>
<ul>5 Once or twice a month</ul>
<ul>6 Never</ul>
<ul>7 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_PARTY_FINAL</code>
        <td>In politics today, do you consider yourself a…</td>
        <td>
    <ul>1 Democrat</ul>
<ul>2 Republican</ul>
<ul>3 Independent</ul>
<ul>4 Something else</ul>
<ul>5 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_PARTYLN_FINAL</code>
        <td>As of today do you lean more to…</td>
        <td>
<ul>1 The Republican Party</ul>
<ul>2 The Democratic Party</ul>
<ul>3 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_PARTYSUM_FINAL</code>
        <td>Party summary.</td>
        <td>
    <ul>1 Dem/Lean Dem</ul>
<ul>2  Rep/Lean Rep</ul>
<ul>3 DK/Refused/No lean</ul>
</td>
    </tr>
    <tr>
        <td><code>F_INCOME</code>
        <td>Family income.</td>
        <td>
    <ul>1 Less than $10,000</ul>
    <ul>2 $10,000 to less than $20,000</ul>
    <ul>3 $20,000 to less than $30,000</ul>
    <ul>4 $30,000 to less than $40,000</ul>
    <ul>5 $40,000 to less than $50,000</ul>
    <ul>6 $50,000 to less than $75,000</ul>
    <ul>7 $75,000 to less than $100,000</ul>
    <ul>8 $100,000 to less than $150,000</ul>
    <ul>9 $150,000 or more</ul>
    <ul>10 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_INCOME_RECODE</code>
        <td>Three-way category coded from self-reported family income.</td>
        <td>
    <ul>1 <$30,000</ul>
    <ul>2 $30-$74,999</ul>
    <ul>3 $75,000+</ul>
    <ul>4 Don't know/Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_REG</code>
        <td>Which of these statements best describes you?</td>
        <td>
    <ul>1 You are ABSOLUTELY CERTAIN that you are registered to vote at your current address</ul>
<ul>2 You are NOT registered to vote at your current address</ul>
<ul>3 You are PROBABLY registered, but there is a chance your registration has lapsed</ul>
<ul>4 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_IDEO</code>
        <td>In general, would you describe your political views as…
[PROGRAMMING NOTE: REVERSE RESPONSE OPTION SCALE FOR RANDOM HALF OF
RESPONDENTS]</td>
        <td>
    <ul>1 Liberal</ul>
<ul>2 Conservative</ul>
<ul>3 Moderate</ul>
<ul>4 Very conservative</ul>
<ul>5 Very liberal</ul>
<ul>6 Refused</ul>
</td>
    </tr>
    <tr>
        <td><code>F_INTUSER</code>
        <td>Do you personally have access to the internet at your home?</td>
        <td>
    <ul>1 Internet User</ul>
<ul>2 Non Internet User</ul>
</td>
    </tr>
    <tr>
        <td><code>F_VOLSUM</code>
        <td>Self-reported volunteerism status.</td>
        <td>
    <ul>1 No</ul>
<ul>2 Yes</ul>
<ul>3 Refused</ul>
</td>
    </tr>
</table>


<a name='acquire_takeaways'></a>
## Takeaways from Acquire:
> - 
> - 
> - 
> - 

<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>


<a name='prep_data'></a>
# Prepare Data
✓ _Plan_ ➜ ✓ _Acquire_ ➜ 🟢 **Prepare** ➜ ☐ _Explore_ ➜ ☐ _Model_ ➜ ☐ _Deliver_

> - 
> - 
> - 
> - 


<a name='prepare_takeaways'></a>
## Prepare Takeaways

> - 
                     
<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>


<a name='explore'></a>
# Explore Data
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ 🟢 **Explore** ➜ ☐ _Model_ ➜ ☐ _Deliver_

> - 
> - 
> - 
> - 

<a name='correlations'></a>
## Correlations


### Correlation Heatmap


### Correlations Table


<a name='pairplot'></a>
## Pair Plot

<a name='hypotheses'></a>
## Hypotheses & Testing

### Hypothesis 1
> - H<sub>0</sub>: 
> - H<sub>a</sub>: 
> - &#x0251;: 0.05

#### Hypothesis 1 Takeaways 
> - 
> - 

### Hypothesis 2
> - H<sub>0</sub>: 
> - H<sub>a</sub>: 
> - &#x0251; = 0.05

#### Hypothesis 2 Takeaways 
> - 
> - 

<a name='explore_takeaways'></a>
## Explore Takeaways

> - 
> - 
> - 
> - 


<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>


<a name='modeling'></a>
# Modeling & Evaluation
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ 🟢 **Model** ➜ ☐ _Deliver_

> - 
> - 

<a name='cross_validation'></a>
## Cross-Validation

<a name='modeling_takeaways'></a>
## Modeling Takeaways
> - 
> - 
> - 
> - 


<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>

<a name='delivery'></a>
# Project Delivery
✓ _Plan_ ➜ ✓ _Acquire_ ➜ ✓ _Prepare_ ➜ ✓ _Explore_ ➜ ✓ _Model_ ➜ 🟢 **Deliver**

> - 
> - 

<a name='conclusion_and_next_steps'></a>
## Conclusion and Next Steps
> -
> -

<a name='replication'></a>
## Project Replication
> - Statistical data can be downloaded from <a href="https://www.kaggle.com/shankanater/american-trends-panel-pewresearch/download">here</a>.
> - You can read the SPSS Statistic data file with `pandas.read_spss("ATP W41.sav")`

<a name='data_use'></a>
## Data Use Agreements
> - The source of the data with express reference to the center in accordance with the following citation: “Pew Research Center’s American Trends Panel”
> - Any hypothesis, insight and or result within this project in no way implies or suggests as attributing a particular policy or lobbying objective or opinion to the Center, and
> - “The opinions expressed herein, including any implications for policy, are those of the author and not of Pew Research Center.”
> - More information on these user agreements can be found at <a href="https://www.pewresearch.org/about/terms-and-conditions/">Pew Research</a>.



<div style="text-align: right"><a href='#toc'>Table of Contents</a></div>
<hr style="border-top: 10px groove tan; margin-top: 1px; margin-bottom: 1px"></hr>