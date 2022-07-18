"""
Author : Mustafa Gürkan Çanakçi
LinkedIn : https://www.linkedin.com/in/mgurkanc/
"""

# Project Name : Rating Product & Sorting Reviews in Amazon


#############################################################################################################
#                                       BUSINESS PROBLEM                                                    #
#############################################################################################################

# In e-commerce marketing, one of the most important issues is the correct calculation of the after-sales service to
# the products.

# The method that we will use to solve this problem is as follows:
# * Providing greater customer satisfaction for the e-commerce site
# * Bringing a product into prominence for the sellers
# * Unproblematic shopping experience for the buyers

# Another issue is the correct ordering of the comments given to the products. The misleading comments will directly
# affect the sale of the product so it will cause both financial loss and loss of customers. The solution of these 2
# basic situations will increase the sales of the e-commerce site and the sellers, while the customers will complete
# the purchasing journey without any problems.


#############################################################################################################
#                                       THE STORY OF DATASET                                                #
#############################################################################################################

# reviewerID        : User ID
# asin              : Product ID
# reviewerName      : Username
# helpful           : Usefull rating
# revieweText       : Assessment
# overall           : Product Rating
# summary           : Evaluation summary
# unixReviewTime    : Evaluation time
# reviewTime        : Evaluation time raw
# day_diff          : Number of days since evaluation
# helpful_yes       : Number of useful
# total_vote        : Number of votes


#############################################################################################################
# Mission 1 : Calculate "Average Rating" by Current Comments and Compare it with the existing average rating.
#############################################################################################################

import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Import dataset
df = pd.read_csv("C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/amazon_review.csv")
df.head()

# Average Rating
df["overall"].mean()
# Out[34]: 4.587589013224822

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4915 entries, 0 to 4914
# Data columns (total 12 columns):
#  #   Column          Non-Null Count  Dtype
# ---  ------          --------------  -----
#  0   reviewerID      4915 non-null   object
#  1   asin            4915 non-null   object
#  2   reviewerName    4914 non-null   object
#  3   helpful         4915 non-null   object
#  4   reviewText      4914 non-null   object
#  5   overall         4915 non-null   float64
#  6   summary         4915 non-null   object
#  7   unixReviewTime  4915 non-null   int64
#  8   reviewTime      4915 non-null   object
#  9   day_diff        4915 non-null   int64
#  10  helpful_yes     4915 non-null   int64
#  11  total_vote      4915 non-null   int64
# dtypes: float64(1), int64(4), object(7)
# memory usage: 460.9+ KB


# Convert some variables to date format
df["reviewTime"] = pd.to_datetime(df["reviewTime"])
current_date =pd.to_datetime('2014-12-10')

df["days"] = (current_date - df["reviewTime"]).dt.days


df.head()

# Numerical analysis of the "days" variable
df["days"].describe([0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).T
# Out[67]:
# count   4915.00000
# mean     439.36704
# std      209.43987
# min        3.00000
# 10%      169.00000
# 25%      283.00000
# 50%      433.00000
# 75%      603.00000
# 80%      640.00000
# 90%      710.00000
# 95%      750.00000
# 99%      945.00000
# max     1066.00000
# Name: days, dtype: float64


q1 = df["days"].quantile(0.25)
q2 = df["days"].quantile(0.50)
q3 = df["days"].quantile(0.75)

df.loc[df["days"]<= q1,"overall"].mean()
# Out[30]: 4.6957928802588995

df.loc[(df["days"] > q1) & (df["days"] <= q2) ,"overall"].mean()
# Out[31]: 4.636140637775961

df.loc[(df["days"] > q2) & (df["days"] <= q3) ,"overall"].mean()
# Out[32]: 4.571661237785016

df.loc[df["days"] > q3,"overall"].mean()
# Out[33]: 4.4462540716612375


# Definiton of Time-Based Weighted Average Function
def time_based_weighted_average(dataframe,w1,w2,w3,w4):
    return  df.loc[df["days"]<= q1,"overall"].mean() * w1/100 + \
            df.loc[(df["days"] > q1) & (df["days"] <= q2) ,"overall"].mean()* w2/100 +\
            df.loc[(df["days"] > q2) & (df["days"] <= q3) ,"overall"].mean()* w3/100 + \
            df.loc[df["days"] > q3,"overall"].mean()* w4/100

time_based_weighted_average(df,30,26,24,20)
# Out[39]: 4.600583941300071


#############################################################################################################
# Mission 2 : Specify 20 reviews for the product to be displayed on the product detail page.
#############################################################################################################

df.head()

# The number of unhelpful votes
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]


# Define a new dataframe
df = df[["reviewerID","overall","reviewTime","day_diff","total_vote","helpful_yes","helpful_no"]]

df.head(10)


# Define score_pos_neg_diff, score_average_rating and wilson_lower_bound functions
def score_pos_neg_diff(up, down):
    return up - down

def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)

def wilson_lower_bound(up, down, confidence=0.95):
    """
    Wilson Lower Bound Score hesapla

    - Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.
    - Hesaplanacak skor ürün sıralaması için kullanılır.
    - Not:
    Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.
    Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

    Parameters
    ----------
    up: int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)


# Calculate new scores by these functions and create new variables
df["score_pos_neg_diff"] = df.apply(lambda x: score_pos_neg_diff(x["helpful_yes"], x["helpful_no"]), axis=1)

df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)

df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

df.head()


# Sorting the first 20 comments by "wilson_lower_bound"
df.sort_values("wilson_lower_bound", ascending=False).head(20)
# Out[54]:
#           reviewerID  overall reviewTime  day_diff  total_vote  helpful_yes  helpful_no  score_pos_neg_diff  score_average_rating  wilson_lower_bound
# 2031  A12B7ZMXFI6IXY  5.00000 2013-01-05       702        2020         1952          68                1884               0.96634             0.95754
# 3449   AOEAD7DPLZE53  5.00000 2012-09-26       803        1505         1428          77                1351               0.94884             0.93652
# 4212   AVBMZZAFEKO58  1.00000 2013-05-08       579        1694         1568         126                1442               0.92562             0.91214
# 317   A1ZQAQFYSXL5MQ  1.00000 2012-02-09      1033         495          422          73                 349               0.85253             0.81858
# 4672  A2DKQQIZ793AV5  5.00000 2014-07-03       158          49           45           4                  41               0.91837             0.80811
# 1835  A1J6VSUM80UAF8  5.00000 2014-02-28       283          68           60           8                  52               0.88235             0.78465
# 3981  A1K91XXQ6ZEBQR  5.00000 2012-10-22       777         139          112          27                  85               0.80576             0.73214
# 3807   AFGRMORWY2QNX  3.00000 2013-02-27       649          25           22           3                  19               0.88000             0.70044
# 4306   AOHXKM5URSKAB  5.00000 2012-09-06       823          65           51          14                  37               0.78462             0.67033
# 4596  A1WTQUOQ4WG9AI  1.00000 2012-09-22       807         109           82          27                  55               0.75229             0.66359
# 315   A2J26NNQX6WKAU  5.00000 2012-08-13       847          48           38          10                  28               0.79167             0.65741
# 1465   A6I8KXYK24RTB  4.00000 2014-04-14       238           7            7           0                   7               1.00000             0.64567
# 1609  A2TPXOZSU1DACQ  5.00000 2014-03-26       257           7            7           0                   7               1.00000             0.64567
# 4302  A2EL2GWJ9T0DWY  5.00000 2014-03-21       262          16           14           2                  12               0.87500             0.63977
# 4072  A22GOZTFA02O2F  5.00000 2012-11-09       759           6            6           0                   6               1.00000             0.60967
# 1072  A2O96COBMVY9C4  5.00000 2012-05-10       942           5            5           0                   5               1.00000             0.56552
# 2583  A3MEPYZVTAV90W  5.00000 2013-08-06       489           5            5           0                   5               1.00000             0.56552
# 121   A2Z4VVF1NTJWPB  5.00000 2012-05-09       943           5            5           0                   5               1.00000             0.56552
# 1142  A1PLHPPAJ5MUXG  5.00000 2014-02-04       307           5            5           0                   5               1.00000             0.56552
# 1753   ALPLKR59QMBUX  5.00000 2012-10-22       777           5            5           0                   5               1.00000             0.56552


