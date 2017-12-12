
# coding: utf-8

# # Project 1
# 
# In this first project you will create a framework to scope out data science projects. This framework will provide you with a guide to develop a well-articulated problem statement and analysis plan that will be robust and reproducible.

# ### Read and evaluate the following problem statement: 
# Determine which free-tier customers will covert to paying customers, using demographic data collected at signup (age, gender, location, and profession) and customer useage data (days since last log in, and activity score 1 = active user, 0= inactive user) based on Hooli data from Jan-Apr 2015. 
# 

# #### 1. What is the outcome?

# Answer: indicator for free-tier customer that coverts to paying customer (Y/N)

# #### 2. What are the predictors/covariates? 

# Answer: age, gender, location, profession, days since last log in  and activity score

# #### 3. What timeframe is this data relevent for?

# Answer: Jan-Apr 2015

# #### 4. What is the hypothesis?

# Answer: Demographic data and users activity allow us to predict if customers covert or not

# ## Let's get started with our dataset

# 1. Create a data dictionary 

# Answer: 
# 
# Variable | Description | Type of Variable
# ---| ---| ---
# admit | 0 = not thing 1 = thing | categorical
# gre | thing in unit X | continuous 
# gpa | thing in unit X| continues
# prestige | thing in unit X | ctegorical
# 

# We would like to explore the association between X and Y 

# #### 2. What is the outcome?

# Answer:  admission into graduate school (Y/N)

# #### 3. What are the predictors/covariates? 

# Answer: gre, gpa, prestige

# #### 4. What timeframe is this data relevent for?

# Answer: 03 Mar 2013

# #### 4. What is the hypothesis?

# Answer:  Determine which students will be admitted into graduate school, using dataset admissions.csv (GRA,GPA and prestige) based on UCLA data from 03 Mar 2013.

#     Using the above information, write a well-formed problem statement. 
# 

# ## Problem Statement

# ### Exploratory Analysis Plan

# Using the lab from a class as a guide, create an exploratory analysis plan. 

# #### 1. What are the goals of the exploratory analysis? 

# Answer: It is an approach to analyzing data sets to summarize their main characteristics, often with visual methods.

# #### 2a. What are the assumptions of the distribution of data? 

# Answer: We usually assume that the data follow a normal distribution.

# #### 2b. How will determine the distribution of your data? 

# Answer: You can start by creating a histogram of your data. In this way, you can immediately see if the shape of the histogram resembles any of the widely known and used statistical distributions 

# #### 3a. How might outliers impact your analysis? 

# Answer: Most parametric statistics, like means, standard deviations, and correlations, and every statistic based on these, are highly sensitive to outliers.

# #### 3b. How will you test for outliers? 

# Answer: there are several methods (Grubbs Test, Generalized Extreme Studentized Deviate (ESD) Test, Tietjen-Moore Test

# #### 4a. What is colinearity? 

# Answer:  one predictor variable in a multiple regression model can be linearly predicted from the others. 

# #### 4b. How will you test for colinearity? 

# Answer: For quantitative variables, correlation is tested by Pearson correlation coefficient (if the variable is approximately normally distributed) while for ordinal variables by Spearman rank correlation coefficient.
# Association between nominal (binominal or multinominal) variables can be tested by a chi-square test (and P-value).
# Association between a categorical and a continuous variable can be assessed by t-test (if the categorical variable has 2 categories) or ANOVA (>2 categories)

# #### 5. What is your exploratory analysis plan?
# Using the above information, write an exploratory analysis plan that would allow you or a colleague to reproduce your analysis 1 year from now. 

# Answer: 1. analyzing data sets to summarize their main characteristics, with visual methods (histogram)
#         2. determine the distribution of your data
#         3. test data for outliers and exlude that if there are
#         4. test for colinearity

# ## Bonus Questions:
# 1. Outline your analysis method for predicting your outcome
# 2. Write an alternative problem statement for your dataset
# 3. Articulate the assumptions and risks of the alternative model
