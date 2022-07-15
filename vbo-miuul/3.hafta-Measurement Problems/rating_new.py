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

# Python Courses
# Puan: 4.71 (4.714209)
# Toplam Puan: 3025

df = pd.read_csv("C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/course_reviews_2020.csv",sep=";")
df.head()

df.shape

df["Rating"].value_counts()

df["Questions Asked"].value_counts()


###################################3
# AVERAGE
####################################

# Ortalama Puan
df["Rating"].mean()


####################
# Time-Based Weighted Average
####################
# Puan Zamanlarına Göre Ağırlıklı Ortalama

df.info()

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

current_date =pd.to_datetime('2021-01-05')
current_date

df["days"] = (current_date - df["Timestamp"]).dt.days


df.head(10)

df.loc[df["days"]<= 15,"Rating"].mean()

df.loc[(df["days"] > 15) & (df["days"] <= 30) ,"Rating"].mean()

df.loc[(df["days"] > 30) & (df["days"] <= 60) ,"Rating"].mean()

df.loc[(df["days"] > 60) & (df["days"] <= 90) ,"Rating"].mean()

df.loc[df["days"] > 90,"Rating"].mean()


def time_based_weighted_average(dataframe, w1, w2, w3, w4,w5):
    return dataframe.loc[dataframe["days"]<= 15,"Rating"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["days"] > 15) & (dataframe["days"] <= 30) , "Rating"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["days"] > 30) & (dataframe["days"] <= 60) , "Rating"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["days"] > 60) & (dataframe["days"] <= 90), "Rating"].mean()  * w4 / 100 + \
           dataframe.loc[dataframe["days"] > 90, "Rating"].mean() * w5 / 100

time_based_weighted_average(df,30,24,20,16,10)
# Out[30]: 4.71066527027193

################################
# USER BASED WEIGHTED AVERAGE
##################################

# Kursu izleme oranlarına göre daha farklı bir ağırlık verebiliriz.

df.groupby("Progress").agg({"Rating":"mean"}).tail(20)

df.describe().T

df["Progress"].value_counts().head(20)


df.loc[df["Progress"] <= 5 ,"Rating"].mean() * 16/100 +\
df.loc[(df["Progress"] > 5) & (df["Progress"] <= 20), "Rating"].mean() * 18 / 100 + \
df.loc[(df["Progress"] > 20) & (df["Progress"] <= 40), "Rating"].mean() * 20 / 100 + \
df.loc[(df["Progress"] > 40) & (df["Progress"] <= 60), "Rating"].mean() * 22 / 100 + \
df.loc[(df["Progress"] > 60), "Rating"].mean() * 24 / 100

def user_based_weighted_average(dataframe, u1, u2, u3, u4,u5):
    return dataframe.loc[dataframe["Progress"] <= 5 ,"Rating"].mean() * u1/100 +\
           dataframe.loc[(dataframe["Progress"] > 5) & (dataframe["Progress"] <= 20), "Rating"].mean() * u2 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 20) & (dataframe["Progress"] <= 40), "Rating"].mean() * u3 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 40) & (dataframe["Progress"] <= 60), "Rating"].mean() * u4 / 100 + \
           dataframe.loc[(dataframe["Progress"] > 60), "Rating"].mean() * u5 / 100

user_based_weighted_average(df, 16, 18, 20, 22,24)


#######################################33
# WEIGHTED RATING #
########################################

def course_weighted_rating(dataframe, user_w):
    time_w = 100-user_w
    return time_based_weighted_average(dataframe,w1=30,w2=24,w3=20,w4=16,w5=10) * time_w/100 + \
           user_based_weighted_average(dataframe,u1=16,u2=18,u3=20,u4=22,u5=24)*user_w/100

course_weighted_rating(df,40)
