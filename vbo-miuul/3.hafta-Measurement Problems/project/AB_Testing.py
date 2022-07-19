"""
Author : Mustafa Gürkan Çanakçi
LinkedIn : https://www.linkedin.com/in/mgurkanc/
"""

# Project Name : Applying A/B Test on the Purchasing Averages of two different groups which are Control and Test

#############################################
#               Business Problem            #
#############################################
# A company introduced a new bidding type called 'average bidding as an alternative to the maximum bidding.
# One of our customers decided to test this new feature and they expects us to analyze the results
# by doing an A/B test.
# The measure of success is "Purchase" in this project.Therefore, it should be focus on the "Purchase" variable
# for statistical tests


#############################################
#          The Story of Dataset             #
#############################################
# In this dataset, there is information such as the number of advertisements that users see and click,
# as well as earnings information from here. There are two separate datasets that are the control and test groups.


#############################################
#         The Variable of Dataset           #
#############################################
# Impression  :Ad views
# Click       :Number of clicks on the displayed ad
# Purchase    :Number of products purchased after ads clicked
# Earning     :Earnings after purchased products


###############################################################################################
#                       MISSION 1 : DATA PREPROCESSING                                        #
###############################################################################################

# Import Libraries and Set the display of columns and rows
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Read the dataset
df_control = pd.read_excel("C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/ab_testing.xlsx",sheet_name="Control Group")
df_control.head()


df_test = pd.read_excel("C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/ab_testing.xlsx",sheet_name="Test Group")

df_control.describe().T

df_test.describe().T


# Missing Value Analysis - Function
def missing_values(dataframe):
    na_columns_ = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    n_miss = dataframe[na_columns_].isnull().sum().sort_values(ascending=True)
    ratio_ = (dataframe[na_columns_].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=True)
    missing_df = pd.concat([n_miss, np.round(ratio_, 2)], axis=1, keys=['Total Missing Values', 'Ratio'])
    missing_df = pd.DataFrame(missing_df)
    return missing_df

def check_df(dataframe, head=5, column="Purchase"):
    print("--------------------- Shape ---------------------")
    print(dataframe.shape)

    print("---------------------- Types --------------------")
    print(dataframe.dtypes)

    print("--------------------- Head ---------------------")
    print(dataframe.head(head))

    print("--------------------- Missing Value Analysis ---------------------")
    print(missing_values(dataframe))

    print("--------------------- Quantiles ---------------------")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df_control)

check_df(df_test)


# Step 3 :

df_control["Group"] = "Control"
df_test["Group"] = "Test"

df = pd.concat([df_control,df_test],ignore_index=True)
df
# Out[27]:
#      Impression      Click  Purchase    Earning    Group
# 0   82529.45927 6090.07732 665.21125 2311.27714  Control
# 1   98050.45193 3382.86179 315.08489 1742.80686  Control
# 2   82696.02355 4167.96575 458.08374 1797.82745  Control
# 3  109914.40040 4910.88224 487.09077 1696.22918  Control
# 4  108457.76263 5987.65581 441.03405 1543.72018  Control
# ..          ...        ...       ...        ...      ...
# 75  79234.91193 6002.21358 382.04712 2277.86398     Test
# 76 130702.23941 3626.32007 449.82459 2530.84133     Test
# 77 116481.87337 4702.78247 472.45373 2597.91763     Test
# 78  79033.83492 4495.42818 425.35910 2595.85788     Test
# 79 102257.45409 4800.06832 521.31073 2967.51839     Test

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 80 entries, 0 to 79
# Data columns (total 5 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   Impression  80 non-null     float64
#  1   Click       80 non-null     float64
#  2   Purchase    80 non-null     float64
#  3   Earning     80 non-null     float64
#  4   Group       80 non-null     object
# dtypes: float64(4), object(1)
# memory usage: 3.2+ KB




###############################################################################################
#                       MISSION 2 : DEFINE THE HYPOTHESIS OF A/B TEST                         #
###############################################################################################

df.groupby("Group").agg({"Purchase":"mean"})
# Out[29]:
#          Purchase
# Group
# Control 550.89406
# Test    582.10610

# Step 1:  Define the hipotesis

# H0 : M1 = M2
# (There is no statistically significant difference between the purchase averages for the Control and Test groups.)

# H1 : M1!= M2
# (There is Statistically Significant difference between the purchase averages for the Control and Test groups.)



#############################################################################################
#                       MISSION 3 : PERFORMING THE HYPOTHESIS TEST                          #
#############################################################################################

# Step 1 : Assumption Control

# Normal Assumption:
test_stat, pvalue = shapiro(df.loc[df["Group"] == "Control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9773, p-value = 0.5891

test_stat, pvalue = shapiro(df.loc[df["Group"] == "Test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9589, p-value = 0.1541

# Conclusion:
# H0 cannot be rejected since p value > 0.05 in both groups.
# The assumption of normal distribution is provided.

# Variance Homogenity:

test_stat, pvalue = levene(df.loc[df["Group"] == "Control", "Purchase"],
                           df.loc[df["Group"] == "Test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 2.6393, p-value = 0.1083

# Conclusion:
# H0 cannot be rejected since p value > 0.05.
# The variances are homogenous.


# Step 2 : Implementation of Appropriate Hypothesis Testing

# The two independent sample T-tests that is parametric tests can be applied because the assumptions are provided.

test_stat, pvalue = ttest_ind(df.loc[df["Group"] == "Control", "Purchase"],
                              df.loc[df["Group"] == "Test", "Purchase"],
                              equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = -0.9416, p-value = 0.3493

# Conclusion
# H0 hypothesis can not be rejected because p value > 0.05.
# With an accuracy rate of 95%, M1 = M2 .So we can state that there is no statistically significant difference
# between the purchase averages for the Control and Test Groups.(M1=M2)







