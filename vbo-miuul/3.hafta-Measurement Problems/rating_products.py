

##############################33
# RATING PRODUCTS #
###############################33

# - Average
# - Time-Based Weighted Average
# - User-Based Weighted Average
# - Weighted Rating

############################################
# Uygulama: Kullanıcı ve Zaman Ağırlıklı Kurs Puanı Hesaplama
############################################

import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# (50+ Saat) Python A-Z™: Veri Bilimi ve Machine Learning
# Puan: 4.8 (4.764925)
# Toplam Puan: 4611
# Puan Yüzdeleri: 75, 20, 4, 1, <1
# Yaklaşık Sayısal Karşılıkları: 3458, 922, 184, 46, 6

df = pd.read_csv("C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/course_reviews.csv")
df.head()

df.shape

df["Rating"].value_counts()
# 5.00000    3267
# 4.50000     475
# 4.00000     383
# 3.50000      96
# 3.00000      62
# 1.00000      15
# 2.00000      12
# 2.50000      11
# 1.50000       2
# Name: Rating, dtype: int64

# Kaç kişi ne kadar soru sormuş?
df["Questions Asked"].value_counts()
# 0.00000     3867
# 1.00000      276
# 2.00000       80
# 3.00000       43
# 4.00000       15
# 5.00000       13
# 6.00000        9
# 8.00000        5
# 9.00000        3
# 14.00000       2
# 11.00000       2
# 7.00000        2
# 10.00000       2
# 15.00000       2
# 22.00000       1
# 12.00000       1
# Name: Questions Asked, dtype: int64


df.groupby("Rating").agg({"Questions Asked":"count"})

df.groupby("Questions Asked").agg({"Questions Asked":"count",
                                   "Rating":"mean"})
#                  Questions Asked  Rating
# Questions Asked
# 0.00000                     3867 4.76519
# 1.00000                      276 4.74094
# 2.00000                       80 4.80625
# 3.00000                       43 4.74419
# 4.00000                       15 4.83333
# 5.00000                       13 4.65385
# 6.00000                        9 5.00000
# 7.00000                        2 4.75000
# 8.00000                        5 4.90000
# 9.00000                        3 5.00000
# 10.00000                       2 5.00000
# 11.00000                       2 5.00000
# 12.00000                       1 5.00000
# 14.00000                       2 4.50000
# 15.00000                       2 3.00000
# 22.00000                       1 5.00000

###################################3
# AVERAGE
####################################

# Ortalama Puan
df["Rating"].mean()

# orta çıkayabilecek bazı yanlılıkları göz ardı etme durumumuz ortaya çıkacaktır.

# bu durum zaman zaman müşteri memnuniyetini kaçırabilmemizi sağlayabilmektedir.
# yeni trendleri kaçırabiliriz.

####################
# Time-Based Weighted Average
####################
# Puan Zamanlarına Göre Ağırlıklı Ortalama

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4323 entries, 0 to 4322
# Data columns (total 6 columns):
#  #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   Rating              4323 non-null   float64
#  1   Timestamp           4323 non-null   object
#  2   Enrolled            4323 non-null   object
#  3   Progress            4323 non-null   float64
#  4   Questions Asked     4323 non-null   float64
#  5   Questions Answered  4323 non-null   float64
# dtypes: float64(4), object(2)
# memory usage: 202.8+ KB


# time stamp değişkenini zaman değişkenine çevirmemiz gerekmektedir.

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

current_date =pd.to_datetime('2021-02-10')
current_date

df["days"] = (current_date - df["Timestamp"]).dt.days

df.head(10)
#    Rating           Timestamp             Enrolled  Progress  Questions Asked  Questions Answered  days
# 0 5.00000 2021-02-05 07:45:55  2021-01-25 15:12:08   5.00000          0.00000             0.00000     4
# 1 5.00000 2021-02-04 21:05:32  2021-02-04 20:43:40   1.00000          0.00000             0.00000     5
# 2 4.50000 2021-02-04 20:34:03  2019-07-04 23:23:27   1.00000          0.00000             0.00000     5
# 3 5.00000 2021-02-04 16:56:28  2021-02-04 14:41:29  10.00000          0.00000             0.00000     5
# 4 4.00000 2021-02-04 15:00:24  2020-10-13 03:10:07  10.00000          0.00000             0.00000     5
# 5 4.00000 2021-02-04 12:42:36  2021-02-01 15:40:13   1.00000          0.00000             0.00000     5
# 6 5.00000 2021-02-04 12:25:30  2020-11-30 19:23:54  85.00000          0.00000             4.00000     5

df[df["days"]<= 30].count()
# Out[24]:
# Rating                194
# Timestamp             194
# Enrolled              194
# Progress              194
# Questions Asked       194
# Questions Answered    194
# days                  194
# dtype: int64

df.loc[df["days"]<= 30,"Rating"].mean()

df.loc[(df["days"] > 30) & (df["days"] <= 90) ,"Rating"].mean()

df.loc[(df["days"] > 90) & (df["days"] <= 100) ,"Rating"].mean()

df.loc[(df["days"] > 100) ,"Rating"].mean()


# Alternatif ağırlıklı ortalama hgesabı

df.loc[df["days"]<= 30,"Rating"].mean()* 28/100 + \
df.loc[(df["days"] > 30) & (df["days"] <= 90) ,"Rating"].mean()*26/100+\
df.loc[(df["days"] > 90) & (df["days"] <= 100) ,"Rating"].mean()*24/100+\
df.loc[(df["days"] > 100) ,"Rating"].mean()*22/100

# Fonksiyon

def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[df["days"] <= 30, "Rating"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["days"] > 30) & (dataframe["days"] <= 90), "Rating"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["days"] > 90) & (dataframe["days"] <= 180), "Rating"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["days"] > 180), "Rating"].mean() * w4 / 100

time_based_weighted_average(df)

time_based_weighted_average(df,30,26,22,22)


################################
# USER BASED WEIGHTED AVERAGE
##################################

# Kullanıcılar verdiği puanlar aynı ağırlığa sahip olmamalıdır.

# Kursu izleme oranlarına göre daha farklı bir ağırlık verebiliriz.

# IMDB filmlerin puanlama sistemi

# Social Proof

# User quality or user based

df.groupby("Progress").agg({"Rating":"mean"}).tail(10)
#  Out[35]:
#            Rating
# Progress
# 87.00000  5.00000
# 89.00000  4.79412
# 90.00000  4.92308
# 91.00000  5.00000
# 93.00000  4.83333
# 94.00000  5.00000
# 95.00000  4.79412
# 97.00000  5.00000
# 98.00000  5.00000
# 100.00000 4.86632

df.loc[df["Progress"] <= 10 ,"Rating"].mean() * 22/100 +\
df.loc[(df["Progress"] > 10) & (df["Progress"] <= 45), "Rating"].mean() * 24 / 100 + \
df.loc[(df["Progress"] > 45) & (df["Progress"] <= 75), "Rating"].mean() * 26 / 100 + \
df.loc[(df["Progress"] > 75), "Rating"].mean() * 28 / 100

def user_based_weighted_average(dataframe, w1=22, w2=24, w3=26, w4=28):
    return dataframe.loc[dataframe["Progress"] <= 10, "Rating"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 10) & (dataframe["Progress"] <= 45), "Rating"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 45) & (dataframe["Progress"] <= 75), "Rating"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 75), "Rating"].mean() * w4 / 100


user_based_weighted_average(df, 20, 24, 26, 30)


#######################################33
# WEIGHTED RATING #
########################################

def course_weighted_rating(dataframe, user_w):
    time_w = 100 -user_w
    return time_based_weighted_average(dataframe) * time_w/100 + user_based_weighted_average(dataframe)*user_w/100

course_weighted_rating(df,60)

course_weighted_rating(df, time_w=30, user_w=70)



def course_weighted_rating(dataframe, time_w=50, user_w=50):
    return time_based_weighted_average(dataframe) * time_w/100 + user_based_weighted_average(dataframe)*user_w/100

course_weighted_rating(df)

course_weighted_rating(df, time_w=40, user_w=60)

course_weighted_rating(df, time_w=40, user_w=55)