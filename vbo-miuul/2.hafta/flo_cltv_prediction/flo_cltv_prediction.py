

# CUSTOMER LIFETIME VALUE PREDICTION

# BUSINESS PROBLEM:

# FLO,an online shoe store,wants to segment its customers and determine marketing strategies
# according to these segments. In this regard, the behavior of customers will be defined and
# groups will be formed according to the clustering in these behaviors.



# Story of Dataset

# The dataset shows the customers which last purchases from the FLO store on Omnichannel(both online and offline
# shopping store)in 2020-2021. However, these customers have consist of infomation from their past shopping behavior.


# master_id : Unique Customer Number
# order_channel : Which channel of the shopping platform is used (Android, ios, Desktop, Mobile))
# last_order_channel : The channel where the most recent purchase was made
# first_order_date : The customer's first purchase date
# last_order_date : The customer's last purchase date
# last_order_date_online :  The customer's last purchase date in online shopping platform
# last_order_date_offline : The customer's last purchase date in offline shopping platform
# order_num_total_ever_online : The customer's total purchases in online shopping platform
# order_num_total_ever_offline :  The customer's total purchases in offline shopping platform
# customer_value_total_ever_offline : The total expenditure by customer in offline shopping platform
# customer_value_total_ever_online : The total expenditure by customer in online shopping platform
# interested_in_categories_12 : List of categories the customer has shopped in the last 12 months


##############################################################################################
#                          MISSION 1 : DATA UNDERSTANDING AND PREPARATION                    #
##############################################################################################

# STEP 1 -
#
# IMPORT LIBRARIES

import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 500)
# pd.set_option('display_max_rows',None)
pd.set_option('display.float_format',lambda x : '%.5f' % x)

# READ DATASET
df_= pd.read_csv("/Users/mgurk/PycharmProjects/pythonProject1/2.hafta/customer_lifetime_value/flo_data_20k.csv")
df = df_.copy()

# CHECKING THE DATA

def datacheck(dataframe):
    print("******Head******")
    print(dataframe.head(10))
    print("******Shape******")
    print(dataframe.shape)
    print("******Info********")
    print(dataframe.info())
    print("******Describe********")
    print(dataframe.describe().T)
    print("***** NAN Values********")
    print(dataframe.isnull().sum())

datacheck(df)
# ******Head******
#                               master_id order_channel last_order_channel first_order_date last_order_date last_order_date_online last_order_date_offline  order_num_total_ever_online  order_num_total_ever_offline  customer_value_total_ever_offline  customer_value_total_ever_online       interested_in_categories_12
# 0  cc294636-19f0-11eb-8d74-000d3a38a36f   Android App            Offline       2020-10-30      2021-02-26             2021-02-21              2021-02-26                      4.00000                       1.00000                          139.99000                         799.38000                           [KADIN]
# 1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f   Android App             Mobile       2017-02-08      2021-02-16             2021-02-16              2020-01-10                     19.00000                       2.00000                          159.97000                        1853.58000  [ERKEK, COCUK, KADIN, AKTIFSPOR]
# 2  69b69676-1a40-11ea-941b-000d3a38a36f   Android App        Android App       2019-11-27      2020-11-27             2020-11-27              2019-12-01                      3.00000                       2.00000                          189.97000                         395.35000                    [ERKEK, KADIN]
# 3  1854e56c-491f-11eb-806e-000d3a38a36f   Android App        Android App       2021-01-06      2021-01-17             2021-01-17              2021-01-06                      1.00000                       1.00000                           39.99000                          81.98000               [AKTIFCOCUK, COCUK]
# 4  d6ea1074-f1f5-11e9-9346-000d3a38a36f       Desktop            Desktop       2019-08-03      2021-03-07             2021-03-07              2019-08-03                      1.00000                       1.00000                           49.99000                         159.99000                       [AKTIFSPOR]
# 5  e585280e-aae1-11e9-a2fc-000d3a38a36f       Desktop            Offline       2018-11-18      2021-03-13             2018-11-18              2021-03-13                      1.00000                       2.00000                          150.87000                          49.99000                           [KADIN]
# 6  c445e4ee-6242-11ea-9d1a-000d3a38a36f   Android App        Android App       2020-03-04      2020-10-18             2020-10-18              2020-03-04                      3.00000                       1.00000                           59.99000                         315.94000                       [AKTIFSPOR]
# 7  3f1b4dc8-8a7d-11ea-8ec0-000d3a38a36f        Mobile            Offline       2020-05-15      2020-08-12             2020-05-15              2020-08-12                      1.00000                       1.00000                           49.99000                         113.64000                           [COCUK]
# 8  cfbda69e-5b4f-11ea-aca7-000d3a38a36f   Android App        Android App       2020-01-23      2021-03-07             2021-03-07              2020-01-25                      3.00000                       2.00000                          120.48000                         934.21000             [ERKEK, COCUK, KADIN]
# 9  1143f032-440d-11ea-8b43-000d3a38a36f        Mobile             Mobile       2019-07-30      2020-10-04             2020-10-04              2019-07-30                      1.00000                       1.00000                           69.98000                          95.98000                [KADIN, AKTIFSPOR]

# ******Shape******
# (19945, 12)

# ******Info********
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 19945 entries, 0 to 19944
# Data columns (total 12 columns):
#  #   Column                             Non-Null Count  Dtype
# ---  ------                             --------------  -----
#  0   master_id                          19945 non-null  object
#  1   order_channel                      19945 non-null  object
#  2   last_order_channel                 19945 non-null  object
#  3   first_order_date                   19945 non-null  object
#  4   last_order_date                    19945 non-null  object
#  5   last_order_date_online             19945 non-null  object
#  6   last_order_date_offline            19945 non-null  object
#  7   order_num_total_ever_online        19945 non-null  float64
#  8   order_num_total_ever_offline       19945 non-null  float64
#  9   customer_value_total_ever_offline  19945 non-null  float64
#  10  customer_value_total_ever_online   19945 non-null  float64
#  11  interested_in_categories_12        19945 non-null  object
# dtypes: float64(4), object(8)
# memory usage: 1.8+ MB
# None

# ******Describe********
#                                         count      mean       std      min       25%       50%       75%         max
# order_num_total_ever_online       19945.00000   3.11085   4.22565  1.00000   1.00000   2.00000   4.00000   200.00000
# order_num_total_ever_offline      19945.00000   1.91391   2.06288  1.00000   1.00000   1.00000   2.00000   109.00000
# customer_value_total_ever_offline 19945.00000 253.92260 301.53285 10.00000  99.99000 179.98000 319.97000 18119.14000
# customer_value_total_ever_online  19945.00000 497.32169 832.60189 12.99000 149.98000 286.46000 578.44000 45220.13000

# ***** NAN Values********
# master_id                            0
# order_channel                        0
# last_order_channel                   0
# first_order_date                     0
# last_order_date                      0
# last_order_date_online               0
# last_order_date_offline              0
# order_num_total_ever_online          0
# order_num_total_ever_offline         0
# customer_value_total_ever_offline    0
# customer_value_total_ever_online     0
# interested_in_categories_12          0
# dtype: int64


# STEP 2 Define the function for outlier threshold and replace with threshold values

def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.25)
    quartile3 = dataframe[variable].quantile(0.75)
    interquantile_range = quartile3 - quartile1
    up_limit = round(quartile3 + 1.5 * interquantile_range)
    low_limit = round(quartile1 - 1.5 * interquantile_range)
    return low_limit, up_limit


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    #dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

# STEP 3
replace_with_thresholds(df, "order_num_total_ever_online")
replace_with_thresholds(df, "order_num_total_ever_offline")
replace_with_thresholds(df, "customer_value_total_ever_offline")
replace_with_thresholds(df, "customer_value_total_ever_online")

df.describe().T

df.describe(percentiles=[.50,.60,.70,.80,.90]).T
#                                         count      mean       std      min       50%       60%       70%       80%        90%        max
# order_num_total_ever_online       19945.00000   2.68864   2.17485  1.00000   2.00000   2.00000   3.00000   4.00000    7.00000    8.00000
# order_num_total_ever_offline      19945.00000   1.76691   0.99798  1.00000   1.00000   2.00000   2.00000   3.00000    4.00000    4.00000
# customer_value_total_ever_offline 19945.00000 232.45157 173.96741 10.00000 179.98000 220.86000 281.86800 365.05800  519.95000  650.00000
# customer_value_total_ever_online  19945.00000 416.85156 352.89099 12.99000 286.46000 371.94400 491.52600 690.86800 1082.03600 1221.00000

# STEP 4

# Total purchases for omnichannel customers
df["total_purchases_number"] = df["order_num_total_ever_online"] +  df["order_num_total_ever_offline"]

# Total expense for omnichannel customers
df["total_customer_expense"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]


# STEP 5

convert =["first_order_date","last_order_date","last_order_date_online","last_order_date_offline"]
df[convert] = df[convert].apply(pd.to_datetime)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 19945 entries, 0 to 19944
# Data columns (total 14 columns):
#  #   Column                             Non-Null Count  Dtype
# ---  ------                             --------------  -----
#  0   master_id                          19945 non-null  object
#  1   order_channel                      19945 non-null  object
#  2   last_order_channel                 19945 non-null  object
#  3   first_order_date                   19945 non-null  datetime64[ns]
#  4   last_order_date                    19945 non-null  datetime64[ns]
#  5   last_order_date_online             19945 non-null  datetime64[ns]
#  6   last_order_date_offline            19945 non-null  datetime64[ns]
#  7   order_num_total_ever_online        19945 non-null  float64
#  8   order_num_total_ever_offline       19945 non-null  float64
#  9   customer_value_total_ever_offline  19945 non-null  float64
#  10  customer_value_total_ever_online   19945 non-null  float64
#  11  interested_in_categories_12        19945 non-null  object
#  12  total_purchases_number             19945 non-null  float64
#  13  total_customer_expense             19945 non-null  float64
# dtypes: datetime64[ns](4), float64(6), object(4)
# memory usage: 2.1+ MB


##############################################################################################
#                          MISSION 2 : CREATING CLTV DATA STRUCTURE                          #
##############################################################################################

df["last_order_date"].max()
#  '2021-05-30'
last_date = dt.datetime(2021,5,30)
type(last_date)
#  datetime.datetime

today_date = dt.datetime(2021, 6, 2)

cltv_df = pd.DataFrame({"customer_id": df["master_id"],
             "recency_cltv_weekly": ((df["last_order_date"] - df["first_order_date"]).dt.days)/7,
             "T_weekly": ((today_date - df["first_order_date"]).astype('timedelta64[D]'))/7,
             "frequency": df["total_purchases_number"],
             "monetary_cltv_avg": df["total_customer_expense"] / df["total_purchases_number"]})

cltv_df.head()
#                             customer_id  recency_cltv_weekly   T_weekly  frequency  monetary_cltv_avg
# 0  cc294636-19f0-11eb-8d74-000d3a38a36f             17.00000 -491.14286    5.00000          187.87400
# 1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f            209.85714 -296.85714   10.00000          138.09700
# 2  69b69676-1a40-11ea-941b-000d3a38a36f             52.28571 -442.85714    5.00000          117.06400
# 3  1854e56c-491f-11eb-806e-000d3a38a36f              1.57143 -500.85714    2.00000           60.98500
# 4  d6ea1074-f1f5-11e9-9346-000d3a38a36f             83.14286 -426.28571    2.00000          104.99000


##############################################################################################
#            MISSION 3 : CREATING BG/NBD,GAMMA GAMMA MODELS AND CALCULATING CLTV             #
##############################################################################################

# STEP 1 : Fit the BG/NBD Model

bgf = BetaGeoFitter(penalizer_coef=0.001)

bgf.fit(cltv_df['frequency'],
       cltv_df['recency_cltv_weekly'],
       cltv_df['T_weekly'])

cltv_df["exp_sales_3_month"] = bgf.conditional_expected_number_of_purchases_up_to_time(4*3,
                                                        cltv_df['frequency'],
                                                        cltv_df['recency_cltv_weekly'],
                                                        cltv_df['T_weekly'])

cltv_df["exp_sales_6_month"] = bgf.predict(4*6,
                                       cltv_df['frequency'],
                                       cltv_df['recency_cltv_weekly'],
                                       cltv_df['T_weekly'])

cltv_df.head(10)
#                             customer_id  recency_cltv_weekly  T_weekly  frequency  monetary_cltv_avg  exp_sales_3_month  exp_sales_6_month
# 0  cc294636-19f0-11eb-8d74-000d3a38a36f             17.00000  30.71429    5.00000          187.87400            0.83886            1.67772
# 1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f            209.85714 225.00000   10.00000          138.09700            0.52953            1.05907
# 2  69b69676-1a40-11ea-941b-000d3a38a36f             52.28571  79.00000    5.00000          117.06400            0.62216            1.24431
# 3  1854e56c-491f-11eb-806e-000d3a38a36f              1.57143  21.00000    2.00000           60.98500            0.62282            1.24563
# 4  d6ea1074-f1f5-11e9-9346-000d3a38a36f             83.14286  95.57143    2.00000          104.99000            0.39457            0.78914
# 5  e585280e-aae1-11e9-a2fc-000d3a38a36f            120.85714 132.42857    3.00000           66.95333            0.38399            0.76798
# 6  c445e4ee-6242-11ea-9d1a-000d3a38a36f             32.57143  65.00000    4.00000           93.98250            0.60313            1.20626
# 7  3f1b4dc8-8a7d-11ea-8ec0-000d3a38a36f             12.71429  54.71429    2.00000           81.81500            0.49370            0.98740
# 8  cfbda69e-5b4f-11ea-aca7-000d3a38a36f             58.42857  70.85714    5.00000          210.93800            0.65049            1.30099
# 9  1143f032-440d-11ea-8b43-000d3a38a36f             61.71429  96.14286    2.00000           82.98000            0.39347            0.78693

# STEP 2 : Fit the Gamma Gamma Model

ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])

cltv_df["exp_average_profit"] = ggf.conditional_expected_average_profit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])

cltv = ggf.customer_lifetime_value(bgf,
                                       cltv_df['frequency'],
                                       cltv_df['recency_cltv_weekly'],
                                       cltv_df['T_weekly'],
                                       cltv_df['monetary_cltv_avg'],
                                       time=6,  # 6 aylık
                                       freq="W",  # T'nin frekans bilgisi.
                                       discount_rate=0.01)

cltv_df["cltv"] = cltv

cltv_df.sort_values("cltv",ascending=False)[:10]
#                                 customer_id  recency_cltv_weekly  T_weekly  frequency  monetary_cltv_avg  exp_sales_3_month  exp_sales_6_month  exp_average_profit      cltv
# 6402   851de3b4-8f0c-11eb-8cb8-000d3a38a36f              8.28571   9.57143    2.00000          650.24500            0.68340            1.36680           696.45019 998.76478
# 9055   47a642fe-975b-11eb-8c2a-000d3a38a36f              2.85714   8.00000    4.00000          467.75000            0.89972            1.79943           484.12080 914.02279
# 15123  635b5e0a-a686-11eb-a6d3-000d3a299ebf              2.00000   5.28571    3.00000          447.11000            0.81528            1.63056           468.26758 801.12374
# 10792  f1f89712-84e5-11eb-8a3c-000d3a38a36f              7.28571  11.42857    2.00000          522.45000            0.67277            1.34553           560.00323 790.59175
# 7173   8897f4a8-c793-11ea-b753-000d3a38a36f             40.14286  45.85714    3.00000          597.14333            0.60018            1.20035           624.92315 787.04984
# 7153   5a351e90-b984-11eb-a757-000d3a38a36f              0.00000   1.85714    2.00000          451.98500            0.73143            1.46286           484.76761 744.05095
# 8496   c1f0cd2c-8d51-11eb-8604-000d3a38a36f              0.00000   9.85714    3.00000          430.27000            0.78364            1.56727           450.68428 741.11280
# 14858  031b2954-6d28-11eb-99c4-000d3a38a36f             14.85714  15.71429    3.00000          450.65333            0.74651            1.49302           471.96731 739.34100
# 14833  b09765ae-29a1-11eb-b280-000d3a38a36f              1.57143  28.00000    2.00000          552.81000            0.59074            1.18148           592.41865 734.38112
# 4087   5ee23224-ad83-11ea-b736-000d3a38a36f             49.57143  50.57143    2.00000          631.10500            0.50661            1.01321           676.01437 718.65986



##############################################################################################
#            MISSION 4 : CREATING SEGMENT ACCORDING CLTV VALUES                              #
##############################################################################################

cltv_df["cltv_segment"] = pd.qcut(cltv_df["cltv"], 4, labels=["D", "C", "B", "A"])

cltv_df.head(3)
#                             customer_id  recency_cltv_weekly  T_weekly  frequency  monetary_cltv_avg  exp_sales_3_month  exp_sales_6_month  exp_average_profit      cltv cltv_segment
# 0  cc294636-19f0-11eb-8d74-000d3a38a36f             17.00000  30.71429    5.00000          187.87400            0.83886            1.67772           193.60204 340.79797            A
# 1  f431bd5a-ab7b-11e9-a2fc-000d3a38a36f            209.85714 225.00000   10.00000          138.09700            0.52953            1.05907           140.28486 155.88455            B
# 2  69b69676-1a40-11ea-941b-000d3a38a36f             52.28571  79.00000    5.00000          117.06400            0.62216            1.24431           120.94931 157.90656            B

cltv_df.groupby("cltv_segment").agg({"count","mean","sum"})
#              recency_cltv_weekly                     T_weekly                    frequency                   monetary_cltv_avg                     exp_sales_3_month                  exp_sales_6_month                  exp_average_profit                          cltv
#                             mean count          sum      mean count          sum      mean count         sum              mean count           sum              mean count        sum              mean count        sum               mean count           sum      mean count           sum
# cltv_segment
# D                      138.72425  4987 691817.85714 161.97141  4987 807751.42857   3.74093  4987 18656.00000          92.38507  4987  460724.32698           0.40452  4987 2017.35046           0.80904  4987 4034.70091           97.79566  4987  487706.94067  79.45112  4987  396222.75123
# C                      100.80173  4986 502597.42857 120.79726  4986 602295.14286   4.35780  4986 21728.00000         126.95077  4986  632976.55825           0.49045  4986 2445.39334           0.98090  4986 4890.78668          133.23154  4986  664292.46104 131.79758  4986  657142.73509
# B                       81.95705  4986 408637.85714 100.59805  4986 501581.85714   4.74007  4986 23634.00000         158.50378  4986  790299.84401           0.54990  4986 2741.77839           1.09979  4986 5483.55679          165.64402  4986  825901.06379 183.88841  4986  916867.59852
# A                       59.56223  4986 296977.28571  75.08255  4986 374361.57143   4.98355  4986 24848.00000         218.70167  4986 1090446.52566           0.64156  4986 3198.82105           1.28312  4986 6397.64210          228.34154  4986 1138510.92410 292.31831  4986 1457499.10773




cltv_df.groupby("cltv_segment").agg({"count","mean","sum"})
