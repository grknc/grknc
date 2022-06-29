



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

#############################################################
# GÖREV 1

#########
# 1. SORU
df = pd.read_csv("datasets\persona.csv")
df.head()

# Detay Bilgi
df.info()

# Boyut Bilgisi
df.shape

# Değişken isimleri
df.columns

# Numerik değişkenlerin verileri
df.describe().T

# En az 1 tane dahi eksik veri mevcut mu?
df.isnull().values.any()

# Eksik verilerin toplamı:
df.isnull().sum()

# Sonuç :   Veri setinde toplamda 5 değişken mevcut olup bunlardan 3 tanesi kategorik, kalan 2 tanesi ise numerik değişkendir.
#           Veri setinin boyutu (5000,5)

#########
# 2.SORU
df["SOURCE"].unique()
df["SOURCE"].nunique()

df["SOURCE"].value_counts()

# Android ve ios olmak üzere 2 farklı kaynak tespit edilmiştir.
# Bununla birlikte android 2972 kişi , ios 2026 kişi kullanmaktadır.

########
# 3.SORU
df["PRICE"].unique()
df["PRICE"].nunique()
# 6 farklı tipte fiyat mevcuttur.


########
# 4.SORU
df["PRICE"].value_counts()
# Fiyatlar oranında 29 ve 39 EUR üzerinden satılan ürünler en fazla sayıda satılmıştır.

########
# 5.SORU
df["COUNTRY"].value_counts()
# Ülkelere göre satış grafiklerini ele aldığımızda en yüksek 2065 ile ABD gelmektedir.
# Türkiye 451 satış ile listenin 4.sırasında yer almaktadır.

########
# 6.SORU
df.groupby(["COUNTRY"]).agg({"PRICE":["sum"]})
# Ülkere göre satışlardan en fazla gelir kazanan, 70225 ile USA'dir.

########
# 7.SORU
df.groupby(["SOURCE"]).agg({"PRICE":["count"]})
# Kaynak türlerine göre Android , IOS 'tan daha fazla satış yapmıştır.

########
# 8.SORU
df.groupby(["COUNTRY"]).agg({"PRICE":["mean"]})
# Ülkelere göre fiyat ortalaması en ucuz ülke Fransa'dır.

########
# 9.SORU
df.groupby(["SOURCE"]).agg({"PRICE":["mean"]})
# Kaynak türlerine göre fiyat ortalaması birbirine çok yakındır.

########
# 10.SORU
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":["mean"]})
# Türkiye'nin Android kaynağındaki fiyatı en pahalıdır.


#############################################################
# GÖREV 2

df = pd.read_csv("datasets\persona.csv")
df.head()

list_cososag = ["COUNTRY","SOURCE","SEX","AGE"]
df.groupby(list_cososag).agg({"PRICE":["mean"]}).head

#############################################################
# GÖREV 3

agg_df = df.groupby(['COUNTRY' , 'SOURCE' , 'SEX' , 'AGE']).agg({'PRICE': 'mean'})
agg_df


agg_df.sort_values(by=["PRICE"],ascending=False, inplace=True)

agg_df.head()

# GÖREV 4
agg_df.reset_index(inplace=True)
agg_df.head()


# GÖREV 5
agg_df['AGE_CAT'] = pd.cut(x = agg_df['AGE'],
                         bins = [0 , 18 , 23, 30 , 40 , 70],
                         labels = ['0_18' , '19_23' , '24_30' , '31_40' , '41_70'])
agg_df.head()


# GÖREV 6
# Yeni seviye tabanlı müşterileri(persona) tanımlayınız.
agg_df_not_ap = agg_df.drop(["AGE","PRICE"],axis=1)
agg_df_not_ap.head()

agg_df["customers_level_based"] = ["_".join(i).upper() for i in agg_df_not_ap.values]
agg_df.drop(["COUNTRY","SOURCE","SEX","AGE","AGE_CAT"],axis=1)


agg_df.head()
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" +
                                   row[2].upper() + "_" + row[5].upper()
                                   for row in agg_df.values]


# GÖREV 7
# Yeni müşterileri(personaları) segmentlere ayırınız.

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],4 ,labels=["D","C","B","A"])
agg_df


agg_df.reset_index(inplace= True)
agg_df.head()

agg_df_final = agg_df.groupby(["SEGMENT","COUNTRY"]).agg({"PRICE":["mean","max","sum"]})
agg_df_final
agg_df["yeni"] = agg_df.groupby(["SEGMENT"]).agg({"PRICE":["mean","max","sum"]})
# GÖREV 8


agg_df

female_and_tur = 'TUR_ANDROID_FEMALE_31_40'



agg_df[agg_df["customers_level_based"] == female_and_tur]

agg_df[agg_df["customers_level_based"] == female_and_tur].agg({"PRICE":"mean"})


female_ios_fra = 'FRA_IOS_FEMALE_31_40'

agg_df[agg_df["customers_level_based"] == female_ios_fra]

female_and_bra = 'BRA_ANDROID_FEMALE_31_40'
agg_df[agg_df["customers_level_based"] == female_and_bra]


agg_df


agg_df = sns.load_dataset("titanic")
