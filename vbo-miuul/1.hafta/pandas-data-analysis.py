## PANDAS ##


#Veri Manipülasyonu ya da veri analizi denildiğinde akıllara ilk gelen python kütüphanelerinden biridir.
#Öncelikle ekonomik ve finansal çalışmalar için doğmuş olup sonraki yıllarda veri analitiği üzerinde kullanılan bir kütüphane olmuştur.
#Temeli 2008 yılında oluşturulnuş
#Farklı veri yapısı ile çalışma imkanı sunar
#Farklı veri kaynaklarından veri okur.



# İçerik

# Pandas Series
# Reading Data
# Quick Look at Data
# Selection in Pandas
# Aggregation & Grouping
# Apply vs Lambda
# Join Operations

# PANDAS SERIES


#Pandas Data Frame ve Pandas Serileri
#Pandas serileri : Tek boyutlu ve index bilgisi barındıran veri tipidir.
#Pandas data-frame : Çok boyutlu ve index bilgisi barından veri tipidir.


import pandas as pd
pd.Series([10,55,45,35,25])
# Çıktı da sol tarafta bulunan değerler index bilgisini gösteriyor. Bu pandas serisinin iç özelliğidir.

d = pd.Series([10,55,45,35,25])
type(d)

#Veri yapıları bu noktada çok önemlidir. Çünkü fonksiyon oluştururken ihtiyaç olan liste,tuple ya da Pandas serisi gibi
#doğru veri yapılarını bilmek ve buna göre işlemler yapmak gerekmektedir. Eğer yanlış bir veri yapısı ile işlem yaparsak
#hata almış oluruz. Diğer bir durumda, veri yapılarını bilirseniz çıktılarda hata ya da hatalar alsanız dahi düzeltme şansınız
#daha kolay olacaktır.

d.index

# içerisindeki verinin tip bilgisini vermektedir.
d.dtype

# İçerisindeki eleman sayısına ise
d.size

# Boyut bilgisi
d.ndim
# Tek boyutlu bir yapıya sahiptir.

# Değerler
d.values

type(d.values)

# İlk 5 Gözlem
d.head()

pd.Series()


##pandas.core.series class Series(base.IndexOpsMixin, NDFrame)
#One-dimensional ndarray with axis labels (including time series).
#Labels need not be unique but must be a hashable type. The object supports both
#integer- and label-based indexing and provides a host of methods for performing operations involving the index.
#Statistical methods from ndarray have been overridden to automatically exclude missing data (currently represented as NaN).
#

#Constructing Series from a dictionary with an Index specified

d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
ser

"""
Çıktı :
a   1
b   2
c   3
dtype: int64

"""

d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['x', 'y', 'z'])
ser

"""
Çıktı : 
x   NaN
y   NaN
z   NaN
dtype: float64

"""

# READING DATA

import pandas as pd


df = pd.read_csv("datasets\Advertising.csv")
df.head(5)

# QUICK LOOK AT DATA

import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

### survived değişken : bağımlı değişken , ana değişken

#Boyut bilgisi
df.shape

# Detaylı bilgi için :
df.info()

## "object ve category" her ikisini de kategorik değişken olarak adlandırabiliriz.

# Değişken isimleri
df.columns

# Index. bilgisi
df.index

# Özet İstatistik Verileri (mean,max,min,std,vb. gibi)
df.describe().T


# En az bir tane dahi eksik veri ya da gözlem mevcut mu?
df.isnull().values.any()

type(df.isnull().values)

# Her bir değişkende kaç tane eksik değer mevcuttur? :
df.isnull().sum()

# Kaç tane sınıf mevcut? Bunlardan kaçar adet mevcut bilgisi için :
df["sex"].value_counts()


# PANDAS SEÇİM İŞLEMLERİ

df.index

# belirli aralık seçimi için :
df[0:12]

# Silme işlemleri için :
df.drop(0, axis=0).head()
# Bu şekilde 0.index in satır değerleri silinmiş oldu.

delete_indexes = [2,5,8,10]
df.drop(delete_indexes,axis=0).head(10)

# Kalıcı işlem yapabilmek için "inplace" argümanı kullanabiliriz. Inplace= True gibi.
# Birçok data frame de değişkeni Index e ya da Index i değişkene çevirme ihtiyacı olmaktadır!!!

# Değişkeni Index e Çevirmek

df["age"].head()
df.age.head()



df.index = df["age"]

df.drop("age",axis=1).head()

df.drop("age",axis=1,inplace=True)
df.head()


# Index i Değişkene Çevirmek

df["age"] = df.index
df.head()

df.drop("age",axis=1,inplace=True)

#### DİĞER YÖNTEM

df.reset_index().head()

# Index resetlemesi yaptı ve tekrardan 0'dan itibaren gösterdi.


# DEĞİŞKENLER ÜZERİNDE İŞLEMELER

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()


"age" in df

df["age"].head()

type(df["age"].head())
#Çıktı : pandas.core.series.Series

df[["age"]].head()
type(df[["age"]].head())
# Çıktı : pandas.core.frame.DataFrame

# Belirlenen seçtiğiniz değişken için eğer tek bir parantez içerisine alırsanız tip bilgisi Pandas Series,
# eğer çift parantez içerisine alırsanız tip bilgisini Pandas Data Frame olarak alırsınız.

df[["age","survived"]].head()

col_names = ["age","embarked","alive"]
df[col_names]
# Değişkenleri bu şekilde liste olarak belirleyip bir data frame oluşturabiliriz.

df["age2"] = df["age"]**2
df.head()

df["age3"] = df["age"] / df["age2"]


# Belli bir değişkeni silmek için aşağıdaki yöntemi uygulayabiliriz:
df.drop("age3",axis=1).head()

df.drop(col_names,axis=1).head()

# Yüksek sayıda değişkene erişebilmek için "loc" ifadesi kullanılır. df.loc["satır","sütun"] şeklinde kullanılır.

#.contains methodu ile string veri yapılarına uygulanan bir methottur. Bununla bir string ifade mevcut mu değil mi diye
# arama yapmaktadır.

df.loc[:,df.columns.str.contains("age")].head()

# Bunun dışında diyebilmek için ~ ifadesini kullanmalıyız.
df.loc[:,~df.columns.str.contains("age")].head()

# "loc" data framelerde seçme işlemi için kullanılan özel yapılardan biridir.

#######################################################
#iloc & loc

# iloc - integer based selection

# loc - indexlerdeki labellara göre seçim yapmaktadır. (label based selection)

df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
# Beklenen Çıktı
"""
   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
0         0       3    male  22.0      1      0   7.2500        S  Third   
1         1       1  female  38.0      1      0  71.2833        C  First   
2         1       3  female  26.0      0      0   7.9250        S  Third   
     who  adult_male deck  embark_town alive  alone    age2      age3  
0    man        True  NaN  Southampton    no  False   484.0  0.045455  
1  woman       False    C    Cherbourg   yes  False  1444.0  0.026316  
2  woman       False  NaN  Southampton   yes   True   676.0  0.038462  
"""


df.loc[0:3]
# Beklenen Çıktı
"""
   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
0         0       3    male  22.0      1      0   7.2500        S  Third   
1         1       1  female  38.0      1      0  71.2833        C  First   
2         1       3  female  26.0      0      0   7.9250        S  Third   
3         1       1  female  35.0      1      0  53.1000        S  First   
     who  adult_male deck  embark_town alive  alone    age2      age3  
0    man        True  NaN  Southampton    no  False   484.0  0.045455  
1  woman       False    C    Cherbourg   yes  False  1444.0  0.026316  
2  woman       False  NaN  Southampton   yes   True   676.0  0.038462  
3  woman       False    C  Southampton   yes  False  1225.0  0.028571  
"""

## loc ifadesi label based selection olduğu için indeks olarak belirtilen son değeri de kapsayarak seçim yaparken,
# iloc ifadesi indeks değerine kadar olup son değeri kapsamamaktadır. Bununla birlikte iloc ifadesi bizden "index" beklemektedir.

# "satır" ya da "değişkenler" göre seçim yapmak istersek "loc" ifadesini KULLANMAKTAYIZ!
# iloc ifadesi ile yalnızca index değerler kullanılıp seçilebilir.


df.iloc[0:3,0:3]

df.loc[0:2,"age"]

col_names = ["survived","age","sex"]

df.loc[0:4, col_names]

# Birden fazla değişkeni seçerek "loc" ifadesi ile SEÇEBİLİRİZ.


# Koşullu Seçim(Conditional Selection)

df[df["age"] > 50].head()
df[df["age"] > 50].count()

df_age = df[df["age"] > 50]
df_age["age"].count()


yeni_list = ["class","age"]
df.loc[df["age"] > 50,yeni_list].head()

# Yaşı 50'den büyük cinsiyeti "man" olanları seçmek için :

yeni_list2 = ["class","age","sex"]
df.loc[(df["age"] > 50) & (df["sex"] == 'male'),yeni_list2].head()
# Yukarıda kısa yöntemi bulunmaktadır.


###Uzun Yöntem :)
new_df = df_age[df_age['sex'] == 'male']
new_df

new_df.loc[:,yeni_list2].head()

# Yeni bir örnek yapalım.

# Değişken sayısını arttıralım :

yeni_list3 = ["class","age","sex","embark_town"]
df.loc[(df["age"] > 50)
       & (df["sex"] == 'male')
       & (df["embark_town"] == 'Southampton'),
       yeni_list3].tail()

# Değişken içerisinde ilave opsiyonlar girelim :

df_embark = df.loc[(df["age"] > 50)
       & (df["sex"] == 'male')
       & ((df["embark_town"] == 'Southampton') | (df["embark_town"] == 'Cherbourg')),
       yeni_list3]

df_embark

df["embark_town"].value_counts()

df_embark["embark_town"].value_counts()

# Sayısal ifadeler ve kategorik değişkenler için seçim işlemleri yaptık. (loc)

######################################33
# Aggregation & Grouping

# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()
# pivot table

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head(10)

# Cinsiyete göre kadın/erkek gruplarının yaş ortalaması nedir?

df.groupby("sex")["age"].mean()
# ilgili hesaplanmak istenen değer için aggregation fonksiyonu kullanılır.
# cinsiyet kırılımında yaş ortalamasının hesabı yukarıdaki gibi olacaktır.

# Cinsiyete göre yaş ortalaması farklı bir yöntem:

df.groupby("sex").agg({"age":"mean"})

df.groupby("sex").agg({"age":["mean","sum"]})
# Birçok parametreye göre hesap yapmak istiyorsak bu yöntem daha mantıklı ve güzel olacaktır.
# Cinsiyete göre veriyi kırıp yaşların ortalaması ve toplamını ayrı ayrı göstermiş olduk.

# Farklı bir örnekler yapalım.
df.groupby("sex").agg({"age":["mean","sum"],
                       "embark_town":"count"})


# Farklı örnekler devam edelim :

df.groupby("sex").agg({"age":["mean","sum"],
                       "survived":"mean"})
# Bu sonuçlara göre cinsiyet kırılımında yaş ortalamasının yanı sıra hayatta kalıp kalmama durumunu da
# analiz edebiliyoruz. ( Garibanin yüzü gülür mü :) )


# Örnekler ( Çok seviyeli groupby)

df.groupby(["sex","embark_town"]).agg({"age":["mean"],
                       "survived":"mean"})
# Birden fazla değişken olduğunda liste formunda ifade etmek daha doğru olacaktır.

list_sxtown = ["sex","embark_town"]
df.groupby(list_sxtown).agg({"age":["mean"],
                       "survived":"mean"})


# Örnekler ( 3 seviyeli kırılım groupby)

list_cltowns = ["sex","embark_town","class"]

df.groupby(list_cltowns).agg({"age":["mean"],
                       "survived":"mean"})


# Örnekler ( 3 seviyeli kırılım )

df.groupby(list_cltowns).agg({"age":["mean"],
                       "survived":"mean",
                        "sex": "count"})


###### NEW CHART - PIVOT TABLE #######

df.pivot_table("survived","sex","embark_town")

# Kesişim kümesi "survived"
# Satır "sex"
# Sütun "embark_town"

df.pivot_table("survived","sex","embark_town", aggfunc="std")
# Bu şekilde standart sapmayı da görüşmüş olduk.

# Örnekler

df.pivot_table("survived","sex",["embarked","class"])


# Sayısal değişkeni kategorik değişkene çevirmek

df["new_age"] = pd.cut(df["age"],[0,10,18,25,40,90])
df.head()

################# !!!!!!!!!!!!!!!!! ##########################
# pd.cut verilerde sayısal değişkeni kategorik değişkene çevirmek için kullanılan en yaygın fonksiyondur.
# Sayısal değişkeni hangi kategorilere bölmek istediğinizi biliyorsanız "cut" fonksiyonu
# Sayısal değişkeni hangi kategorilere bölmeyi bilemiyorsak verileri küçükten büyüğe doğru sıralayıp çeyreklik ifadelerde
# bunları gösteren fonksiyonlar "qcut" fonksiyonudur. Çok sık kullanılmaktadır.

df.pivot_table("survived","sex","new_age")

# Örnekler Devam
df.pivot_table("survived","sex",["new_age","class"])

# Örnkeler Devam

df.pivot_table("survived",["sex","new_age"],["embarked","class"])
# En Güzel Durum Bu Oldu Sanırım :)

pd.set_option('display.width',500)



############# APPLY & LAMBDA ###############3

# Apply :  Satır ve sütunlarda otomatik olarak fonksiyon çalıştırmayı sağlar.
# Bir data frame i apply ile istediğimiz fonk. uygulayabiliriz.

# Lambda : Bir fonksiyon tanımlama şeklidir. Tıpkı "def" gibidir. Fakat kullan-at fonksiyonudur. Kod akışı esnasında
# bir kez kullanayım sonrasında

df= sns.load_dataset("titanic")
df["age_new"] = df["age"]*2
df["age_new2"] = df["age"]* 5
df.head()

# Değişkenler için fonksiyon yazacağız.

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = (df[col]/10)

df.head()

# Apply ve Lambda Kullanarak Uygulamak

df[["age","age_new","age_new2"]].apply(lambda x : x/10).head()

# loc ile apply&lambda kullanmak

df.loc[:,df.columns.str.contains("age")].apply(lambda x : x/10).head()

# Standartlaştırma - Normalizasyon Fonksiyonunu Kullanmak
df.loc[:,df.columns.str.contains("age")].apply(lambda x : (x-x.mean())/ x.std()).head()

# Diğer bir yöntem !!!
def standart_scaler(col_name):
    return (col_name-col_name.mean()) / col_name.std()

df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()

# Bunu dataya aktarabilmek ve kaydetmek için :

df.loc[:,["age","age_new","age_new2"]] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()

df.head()

######### BİRLEŞTİRME ( JOIN) İŞLEMLERİ ############

import numpy as np
import pandas as pd
m = np.random.randint(1,30,size=(5,3))
df1 = pd.DataFrame(m,columns=["v1","v2","v3"])
df1
df2 = df1 + 90
df2

pd.concat([df1,df2])

# Yeni Data Frame yapısının indexlerini yeniden tanımlamak için :
pd.concat([df1,df2],ignore_index=True)

# MERGE İŞLEMLERİ

df1 = pd.DataFrame({'employees': ['John','Dennis','Mark','Maria'],
                    'group':['accounting','engineering','engineering','hr']})

df2 = pd.DataFrame({'employees': ['Dennis','John','Mark','Maria'],
                    'start_date':[2007,2009,2012,2014]})
print(df1)
print(df2)

pd.merge(df1,df2)

df3 = pd.merge(df1,df2,on="employees")

# Her çalışanın müdür bilgisine erişmek istiyoruz.

df4 = pd.DataFrame({'group': ['accounting','engineering','egineering','hr'],
                    'manager':['Yiğit','Ayşe','Meltem','Hilal']})

pd.merge(df3,df4)

