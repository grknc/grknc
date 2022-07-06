
#################################################

# Customer Segmentation with RFM

############################################3

# 1. Business Problem
# 2. Data Understanding
# 3. Data Preparation
# 4. Calculating RFM Metrics
# 5. Calculating RFM Scores
# 6. Creating & Analysing RFM Segments
# 7. Tüm Sürecin Fonksiyonlaştırılması



# 1. Business Problem
##################################

# Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu segmentlere göre
# pazarlama stratejilerini belirlemek istiyor.


# Veri Seti Hikayesi


# Online Retail II isimli veri seti


# Değişkenler ( Variables)

# InvoiceNo : Fatura Numarası ( C ile başlıyorsa iptal edilen işlem)
# StockCode
# Description
# Quantity
# InvoiceDate
# UnitPrice ( Ürün fiyatı- GBP cinsinden)
# CustomerID ( Eşsiz müşteri numarası)
# Country ( Ülke ismi)

########################################
# 2 . Data Understanding

import datetime as dt
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
# pd.set_option('display_max_rows',None)
pd.set_option('display.float_format',lambda x : '%.3f' % x)


df_= pd.read_excel("/Users/mgurk/PycharmProjects/pythonProject1/datasets/online_retail_II.xlsx",sheet_name="Year 2009-2010")

df= df_.copy()
df.head()

# Qunatity : Ürünlerden kaçar tane alındığını gösteriyor.
# Price : Birim Fiyatı gösteriyor. (Unit Price)

# Eğer toplam fiyatı öğrenmek istersek TotPrice = Quantity * Price

# Bir faturada birden çok stok kodu olduğu için fatura bedelini hesaplarken her bir stok biriminin toplam fiyatlarını
# hesaplayıp sonrasında bu değerleri toplamamız gerekmektedir.


df.shape

df.isnull().sum()

# Veri setindeki eşsiz değerlerin sayısı :
df["Description"].nunique()

# Hangi üründen kaçar adet mevcuttur?
df["Description"].value_counts().head(10)

# En çok sipariş edilen ürün hangisidir?
df.groupby("Description").agg({"Quantity": "sum"}).head(10)
# Out[21]:
#                                    Quantity
# Description
# 21494                                    -720
# 22467                                      -2
# 22719                                       2
#  DOORMAT UNION JACK GUNS AND ROSES       179
# 3 STRIPEY MICE FELTCRAFT                 690
# 4 PURPLE FLOCK DINNER CANDLES            207
# ANIMAL STICKERS                          385
# BLACK PIRATE TREASURE CHEST               57
# BROWN  PIRATE TREASURE CHEST              59
# Bank Charges                              -2

# Data çalışmasına rağmen Quantity - değer gösterdiği için hatalı bir yorum mevcut.

# En çok sipariş edilen ürün hangisidir? ( BÜyükten küçüğe sıralı) Hangi üründen kaçar adet satıldı?
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity",ascending=False).head(10)
# Out[23]:
#                                    Quantity
# Description
# WHITE HANGING HEART T-LIGHT HOLDER     57733
# WORLD WAR 2 GLIDERS ASSTD DESIGNS      54698
# BROCADE RING PURSE                     47647
# PACK OF 72 RETRO SPOT CAKE CASES       46106
# ASSORTED COLOUR BIRD ORNAMENT          44925
# 60 TEATIME FAIRY CAKE CASES            36326
# PACK OF 60 PINK PAISLEY CAKE CASES     31822
# JUMBO BAG RED RETROSPOT                30727
# SMALL POPCORN HOLDER                   29500
# STRAWBERRY CERAMIC TRINKET BOX         26563


df.head()

# Fatura başına toplam kaç para kazanılmıştır?

df["TotPrice"] = df["Quantity"] * df["Price"]
df.head()

df.groupby("Invoice").agg({"TotPrice":"sum"}).head(10)


###################################################
# 3. Data Preparation

df.shape
df.isnull().sum()
df.dropna(inplace=True)

df.describe().T

# Invoice da iade edilen faturalardan dolayı Quantity (min ve max) değerleri absürt görünmektedir.

df.head()

# İade olmayan faturaları görmek için :
df[~df["Invoice"].str.contains("C",na=False)]


# İade olan Faturaları görmek için :
df[df["Invoice"].str.contains("C",na=False)]


# df dataframe bunları aktarmak için :

df = df[~df["Invoice"].str.contains("C",na=False)]

df.describe().T


###################################################################
# 4. Calculating RFM Metrics

# Recency, Frequency, Monetary

df["InvoiceDate"].max()
# Out[41]: Timestamp('2010-12-09 20:01:00')

# Recency değeri için son kesilen fatura tarihinden 2 gün sonrayı düşünerek analizimizi ona göre düşünürüz.
# Bu bir varsayım diyebiliriz.(2010-12-11 gibi)

today_date = dt.datetime(2010,12,11)
type(today_date)
# datatime diye bir değişken

# Bütün müşterilere göre groupby alacağız.

# Recency için : today date - groupby aldıktan sonra her bir müşterinin max.tarihini çıkaracağız.

# CustomerID Groupby aldıktan her bir müşterinin eşsiz fatura sayısı (işlem sayısını) yani satınalma

# CustomerID groupby yapıldıktan sonra TotPrice sum değerlerini alırsak her bir müşterinin toplam kaç para
# bıraktığını hesaplamış oluruz.

df.head()

rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda  date: (today_date- date.max()).days,
                                    'Invoice': lambda  num : num.nunique(),
                                    'TotPrice' : lambda  TotPrice : TotPrice.sum()})


# nunique : Eşsiz değerleri , kaç adet fatura mevcut?

rfm.head()
rfm.columns = ['recency','frequency','monetary']

rfm.describe().T

rfm = rfm[rfm['monetary']>0]
rfm.head()

# Müşteri ID lerine göre veriyi tekilleştirmemiz gerekiyordu. Bu şekilde segmentasyonu sağlamış olduk.
# Bu metrik değerler oldu.

rfm.shape


########################################################
# 5. RFM Skorlarının Hesaplanması( Calculating RFM Scores)

# qcut fonksiyonu quamtile değerlerine bölen bir fonksiyon türüdür.

rfm['recency_score'] = pd.qcut(rfm['recency'],5,labels=[5,4,3,2,1])

# qcut : fonksiyonu Quantile küçükten büyüğe doğru sıralamaktadır. O yüzden yukarıda belirttiğimiz 5 en küçük,
# 1 en büyük değer olacaktır.

rfm.head(10)

rfm['monetary_score'] = pd.qcut(rfm['monetary'],5,labels=[1,2,3,4,5])

rfm['frequency_score'] = pd.qcut(rfm['frequency'].rank(method="first"),5,labels=[1,2,3,4,5])

rfm.head(10)

# RF Score
# RF değerlerini bir araya getirmemiz gerekmektedir.

rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str)+ rfm['frequency_score'].astype(str) )

rfm.head()

rfm.describe().T

#####
# CONCLUSION

# Champions (En iyi müşteriler)
rfm[rfm["RFM_SCORE"]=="55"]

# Kaçırmamız gereken müşteriler
rfm[rfm["RFM_SCORE"]=="15"]


####################################################################
# 6. Creating & Analysing RFM Segments
####################################################

# regex

# RFM isimlendirmesi

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_the_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'

}

rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map,regex=True)

### çok güzel bir yapı ###
rfm[["segment","recency","frequency","monetary"]].groupby("segment").agg(["mean","count"])
#Out[39]:
#                     recency       frequency       monetary
#                        mean count      mean count     mean count
# segment
# about_the_sleep      53.819   343     1.201   343  441.320   343
# at_Risk             152.159   611     3.074   611 1188.878   611
# cant_loose          124.117    77     9.117    77 4099.450    77
# champions             7.119   663    12.554   663 6852.264   663
# hibernating         213.886  1015     1.126  1015  403.978  1015
# loyal_customers      36.287   742     6.830   742 2746.067   742
# need_attention       53.266   207     2.449   207 1060.357   207
# new_customers         8.580    50     1.000    50  386.199    50
# potential_loyalists  18.793   517     2.017   517  729.511   517
# promising            25.747    87     1.000    87  367.087    87


#################
# Pazarlama Departmanı için Ön Görülerde bulunulabilir?

rfm[rfm["segment"]== "need_attention"].head(10)

rfm[rfm["segment"]== "cant_loose"].head(10)
rfm[rfm["segment"]== "cant_loose"].index

rfm[rfm["segment"]== "new_customers"].index


##########################
new_df = pd.DataFrame()
new_df["new_customer_id"] = rfm[rfm["segment"]== "new_customers"].index
new_df

new_df["new_customer_id"].astype(int)

new_df.to_csv("new_customers.csv")
rfm.head(10)

rfm.to_csv("rfm.csv")


########################################
# TÜM SÜRECİN FONKSİYONLAŞTIRILMASI

def create_rfm(dataframe, csv=False):

    # VERIYI HAZIRLAMA
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]

    # RFM METRIKLERININ HESAPLANMASI
    today_date = dt.datetime(2011, 12, 11)
    rfm = dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'Invoice': lambda num: num.nunique(),
                                                "TotalPrice": lambda price: price.sum()})
    rfm.columns = ['recency', 'frequency', "monetary"]
    rfm = rfm[(rfm['monetary'] > 0)]

    # RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # cltv_df skorları kategorik değere dönüştürülüp df'e eklendi
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                        rfm['frequency_score'].astype(str))


    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
    rfm = rfm[["recency", "frequency", "monetary", "segment"]]
    rfm.index = rfm.index.astype(int)

    if csv:
        rfm.to_csv("rfm.csv")

    return rfm

df = df_.copy()

rfm_new = create_rfm(df, csv=True)
rfm_new

###
# RFM Segmentasyonu ile ilgili geri bildirimler alınmamaktadır.
# Departmanlarla sürekli haberleşme durumunda olmalılar.