"""
Author : Mustafa Gürkan Çanakçi
LinkedIn : https://www.linkedin.com/in/mgurkanc/

"""

# Project Name : Potential Customer Yield Calculation with Rule-Based-Segmentation

# Content :
# * Create new customer-level-based
# * Segment by new customer level based
# * Predict how much earn on average money to the company by new customers


# Import Necessary Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

#############################################################
# STEP 1

# 1. Read the "persona.csv" data
df = pd.read_csv("datasets\persona.csv")
df.head()

#Out[134]:
#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

# Detailed Information
df.info()
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 5000 entries, 0 to 4999
# Data columns (total 5 columns):
 #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
# 0   PRICE    5000 non-null   int64
# 1   SOURCE   5000 non-null   object
# 2   SEX      5000 non-null   object
# 3   COUNTRY  5000 non-null   object
# 4   AGE      5000 non-null   int64
#dtypes: int64(2), object(3)


df.shape
# Out[136]: (5000, 5)

# Data Variables
df.columns
#Out[137]: Index(['PRICE', 'SOURCE', 'SEX', 'COUNTRY', 'AGE'], dtype='object')

# Describe the datas
df.describe().T
#Out[138]:
#        count     mean        std   min   25%   50%   75%   max
# PRICE  5000.0  34.1320  12.464897   9.0  29.0  39.0  39.0  59.0
# AGE    5000.0  23.5814   8.995908  15.0  17.0  21.0  27.0  66.0


# Any missing data
df.isnull().values.any()

# Sum of null values for each variable
df.isnull().sum()
# Out[140]:
# PRICE      0
# SOURCE     0
# SEX        0
# COUNTRY    0
# AGE        0
# dtype: int64



#########
# 2. How many unique Source are there? What are their frequencies?
df["SOURCE"].unique()
df["SOURCE"].nunique()
# Out[142]: 2

df["SOURCE"].value_counts()
# Out[143]:
# android    2974
# ios        2026
# Name: SOURCE, dtype: int64


########
# 3.How many unique Price are there?
df["PRICE"].unique()
df["PRICE"].nunique()
# Out[144]: 6


########
# 4.How many sales were made in which "PRICE" variables?
df["PRICE"].value_counts()
# Out[146]:
# 29    1305
# 39    1260
# 49    1031
# 19     992
# 59     212
# 9      200
# Name: PRICE, dtype: int64


########
# 5.How many sales were made in which "COUNTRY"?
df["COUNTRY"].value_counts()
# Out[147]:
# usa    2065
# bra    1496
# deu     455
# tur     451
# fra     303
# can     230
# Name: COUNTRY, dtype: int64



# 6. How much was earned in total from sales by country?
df.groupby(["COUNTRY"]).agg({"PRICE":["sum"]})
# Out[148]:
#         PRICE
#           sum
# COUNTRY
# bra      51354
# can       7730
# deu      15485
# fra      10177
# tur      15689
# usa      70225


# 7. What are sales figures by "SOURCE" types?
df.groupby(["SOURCE"]).agg({"PRICE":["count"]})
# Out[149]:
#         PRICE
#         count
# SOURCE
# android  2974
# ios      2026


# 8.What are average PRICE by Country?
df.groupby(["COUNTRY"]).agg({"PRICE":["mean"]})
# Out[150]:
#              PRICE
#               mean
# COUNTRY
# bra      34.327540
# can      33.608696
# deu      34.032967
# fra      33.587459
# tur      34.787140
# usa      34.007264


# 9. What are average PRICE by SOURCE variables?
df.groupby(["SOURCE"]).agg({"PRICE":["mean"]})
# Out[151]:
#             PRICE
#              mean
# SOURCE
# android  34.174849
# ios      34.069102

# 10. What are average PRICE by both SOURCE and COUNTRY?
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":["mean"]})
# Out[152]:
#                      PRICE
#                       mean
# COUNTRY SOURCE
# bra     android  34.387029
#         ios      34.222222
# can     android  33.330709
#         ios      33.951456
# deu     android  33.869888
#         ios      34.268817
# fra     android  34.312500
#         ios      32.776224
# tur     android  36.229437
#         ios      33.272727
# usa     android  33.760357
#         ios      34.371703


#############################################################
# STEP 2

# Target : Find the average "PRICE" by Country,Source,Sex and Age

# First, we create a new list
list_cososag = ["COUNTRY","SOURCE","SEX","AGE"]
df.groupby(list_cososag).agg({"PRICE":["mean"]}).head
# Out[154]:
# <bound method NDFrame.head of    PRICE
#                                  mean
# COUNTRY SOURCE  SEX    AGE
# bra     android female 15   38.714286
#                        16   35.944444
#                        17   35.666667
#                        18   32.255814
#                        19   35.206897
#                                ...
# usa     ios     male   42   30.250000
#                        50   39.000000
#                        53   34.000000
#                        55   29.000000
#                        59   46.500000
# [348 rows x 1 columns]>


#############################################################
# STEP 3

# Create new data frame named agg_df
agg_df = df.groupby(['COUNTRY' , 'SOURCE' , 'SEX' , 'AGE']).agg({'PRICE': 'mean'})

# Sort the prices in descending order
agg_df.sort_values(by=["PRICE"],ascending=False, inplace=True)
agg_df.head()
#Out[157]:
#                             PRICE
# COUNTRY SOURCE  SEX    AGE
# bra     android male   46    59.0
# usa     android male   36    59.0
# fra     android female 24    59.0
# usa     ios     male   32    54.0
# deu     android female 36    49.0


# STEP 4
# Define a new index for this data frame
agg_df.reset_index(inplace=True)
agg_df.head()
# Out[159]:
#   COUNTRY   SOURCE     SEX  AGE  PRICE
# 0     bra  android    male   46   59.0
# 1     usa  android    male   36   59.0
# 2     fra  android  female   24   59.0
# 3     usa      ios    male   32   54.0
# 4     deu  android  female   36   49.0

# STEP 5
# You realize that the type of "Age" variables are numeric. We want to convert this variable to categorical variable type.

# Define a new variable named "AGE_CAT". After that, we add this new variable to agg_df data frame.
agg_df['AGE_CAT'] = pd.cut(x = agg_df['AGE'],
                         bins = [0 , 18 , 23, 30 , 40 , 70],
                         labels = ['0_18' , '19_23' , '24_30' , '31_40' , '41_70'])
agg_df.head()
# Out[160]:
#   COUNTRY   SOURCE     SEX  AGE  PRICE AGE_CAT
# 0     bra  android    male   46   59.0   41_70
# 1     usa  android    male   36   59.0   31_40
# 2     fra  android  female   24   59.0   24_30
# 3     usa      ios    male   32   54.0   31_40
# 4     deu  android  female   36   49.0   31_40


# STEP 6
# Target : "Define "New Customers Level Based " (Persona)

agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" +
                                   row[2].upper() + "_" + row[5].upper()
                                   for row in agg_df.values]
agg_df.head()
# Out[162]:
#   COUNTRY   SOURCE     SEX  AGE  PRICE AGE_CAT     customers_level_based
# 0     bra  android    male   46   59.0   41_70    BRA_ANDROID_MALE_41_70
# 1     usa  android    male   36   59.0   31_40    USA_ANDROID_MALE_31_40
# 2     fra  android  female   24   59.0   24_30  FRA_ANDROID_FEMALE_24_30
# 3     usa      ios    male   32   54.0   31_40        USA_IOS_MALE_31_40
# 4     deu  android  female   36   49.0   31_40  DEU_ANDROID_FEMALE_31_40

# Alternative Solution

#agg_df_not_ap = agg_df.drop(["AGE","PRICE"],axis=1)
#agg_df_not_ap.head()

#agg_df["customers_level_based"] = ["_".join(i).upper() for i in agg_df_not_ap.values]
#agg_df.drop(["COUNTRY","SOURCE","SEX","AGE","AGE_CAT"],axis=1)


# STEP 7
# Target : Segment new customers_level_based.

agg_df = agg_df.reset_index()
agg_df_final = agg_df.groupby("customers_level_based").agg({"PRICE" : "mean"})
agg_df_final
# Out[163]:
#                              PRICE
# customers_level_based
# BRA_ANDROID_FEMALE_0_18   35.645303
# BRA_ANDROID_FEMALE_19_23  34.077340
# BRA_ANDROID_FEMALE_24_30  33.863946
# BRA_ANDROID_FEMALE_31_40  34.898326
# BRA_ANDROID_FEMALE_41_70  36.737179
#                              ...
# USA_IOS_MALE_0_18         33.983495
# USA_IOS_MALE_19_23        34.901872
# USA_IOS_MALE_24_30        34.838143
# USA_IOS_MALE_31_40        36.206324
# USA_IOS_MALE_41_70        35.750000


agg_df_final["SEGMENT"] = pd.qcut(agg_df_final["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df_final.groupby("SEGMENT").agg({"PRICE": "mean"})
# Out[164]:
#              PRICE
# SEGMENT
# D        29.206780
# C        33.509674
# B        34.999645
# A        38.691234


agg_df = agg_df.reset_index()
agg_df_final = agg_df_final.reset_index()

# STEP 8
# Target : Classify new customers and estimate how much revenue they can generate.

female_and_tur = 'TUR_ANDROID_FEMALE_31_40'
agg_df_final[agg_df_final["customers_level_based"] == female_and_tur]
# Out[165]:
#       customers_level_based      PRICE SEGMENT
# 72  TUR_ANDROID_FEMALE_31_40  41.833333       A

female_ios_fra = 'FRA_IOS_FEMALE_31_40'
agg_df_final[agg_df_final["customers_level_based"] == female_ios_fra]
# Out[166]:
#   customers_level_based      PRICE SEGMENT
# 63  FRA_IOS_FEMALE_31_40  32.818182       C


female_and_bra = 'BRA_ANDROID_FEMALE_31_40'
agg_df_final[agg_df_final["customers_level_based"] == female_and_bra]
# Out[167]:
#      customers_level_based      PRICE SEGMENT
# 3  BRA_ANDROID_FEMALE_31_40  34.898326       B


agg_df_final.loc[(agg_df_final["SEGMENT"] == "A")].head()
#Out[168]:
#       customers_level_based      PRICE SEGMENT
# 4   BRA_ANDROID_FEMALE_41_70  36.737179       A
# 9     BRA_ANDROID_MALE_41_70  40.041667       A
# 11      BRA_IOS_FEMALE_19_23  36.403846       A
# 25    CAN_ANDROID_MALE_19_23  40.111111       A
# 27    CAN_ANDROID_MALE_41_70  37.571429       A
