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
df = sns.load_dataset("titanic")
df.head()

# 2.SORU

df["sex"].value_counts()

# 3. SORU

def col_unique(dataframe,columns):
    print("*** Değişken Adı :", dataframe[columns].name)
    print("Benzersiz Değeri: ", dataframe[columns].unique())
    print("***************************")

for col in df.columns:
    col_unique(df,col)

# 4.SORU
df["pclass"].nunique()

# 5.SORU
p_list = ["pclass","parch"]
df[p_list].nunique()

# 6.SORU
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
df["embarked"].dtypes
str(df["embarked"].dtypes)

df.info()

# 7.SORU
df_embarkedc = df[df["embarked"] == "C"]
df_embarkedc.head()
df_embarkedc.info()


# 8.SORU
df_embarked = df[df["embarked"] != "S"]
df_embarked.describe().T
df_embarked.head()

# 9.SORU
yeni_list = ["class","age","sex"]
df.loc[(df["age"] < 30) & (df["sex"] == 'female'),yeni_list]

# 10.SORU
yeni_list2 = ["class","age","sex","fare"]
print("********* Fare'i 500'den büyük veya yaşı 70'den büyük yolcuların listesi")
df.loc[(df["fare"]> 500) | (df["age"] > 70),yeni_list2]

# 11.SORU
df.isnull().sum()

# 12.SORU
df.drop("who",axis=1,inplace=True)

# 13.SORU
df.deck = df.deck.fillna(df.deck.mode()[0])
df.isnull().sum()

# 14.SORU
df.isnull().sum()
df.age = df.age.fillna(df.age.median())
df.isnull().sum()

# 15.SORU
list_2 = ["pclass","sex"]
df.groupby(list_2).agg({"survived":["sum","mean","count"]})

# 16.SORU
df["age2"] = df["age"].apply(lambda x: x - 2)
df.head()


# 17.SORU
df = sns.load_dataset("tips")
df.head()

# 18.SORU
df.info()
df["time"].unique()

statistic_arg = ["sum","min","max","mean"]
df.groupby("time").agg({"total_bill":(statistic_arg)})

# 19.SORU
day_and_time = ["day","time"]
df.groupby(day_and_time).agg({"total_bill":(statistic_arg)})

# 20.SORU
# Time - Lunch seçilecek
# Müşteri - Kadın

# Groupby- Day

# Kırılımlar : Total Bill ve Tip
df=sns.load_dataset("tips")
df.columns

yeni_list3 = ["time","sex","day","total_bill","tip"]
new_df = df.loc[(df["time"] == 'Lunch') & (df["sex"] == 'Female'),yeni_list3]

new_df.groupby("day").agg({"total_bill":(statistic_arg),
                           "tip":(statistic_arg)})

# 21.SORU
tip_and_tot_bill = ["tip","total_bill"]
df.loc[(df["size"] < 3 ) & (df["total_bill"] > 10 ),tip_and_tot_bill].mean()

# 22.SORU
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

# 23.SORU
# total bill değişkeni için kadın ve erkek için ayrı ayrı ortalaması
# ortalamaların altında olanlara 0 , üstünde ve eşit 1 - total_bill_flag


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

df = sns.load_dataset("tips")

# ERKEKLERİN TOTAL BILL ORTALAMASI
df.loc[(df["sex"] == "Male" ),"total_bill"].mean()

# KADINLARIN TOTAL BILL ORTALAMASI
df.loc[(df["sex"] == "Female" ),"total_bill"].mean()


df['total_bill_flag'] = df['total_bill'].apply(lambda x:'1' if x >=20 else '0')


def func(cinsiyet,tot_bill):
    for col in df[cinsiyet]:
        if "Fe" in col:
            df['total_bill_flag'] = df[tot_bill].apply(lambda x:'1' if x >= df.loc[(df[cinsiyet] == "Female" ),
                                                                               "total_bill"].mean() else '0')

        else:
            df['total_bill_flag'] = df[tot_bill].apply(lambda x: '1' if x >= df.loc[(df[cinsiyet] == "Male" ),
                                                                               "total_bill"].mean() else '0')

func("sex","total_bill")


########################################333
# PRATIK ALIŞTIRMA
for col in df["sex"]:
    if "Female" in col:
        df['total_bill_flag'] = df["total_bill"].apply(lambda x:'1' if x >= df.loc[(df["sex"] == "Female" ),
                                                                               "total_bill"].mean() else '0')
        print("********************")
    else:
        df['total_bill_flag'] = df["total_bill"].apply(lambda x: '0' if x <= df.loc[(df["sex"] == "Male"),
                                                                                "total_bill"].mean() else '1')
        print("**")

df.head(25)

df['total_bill_flag'] = df["total_bill"].apply(lambda x:'1' if x >= df.loc[(df["sex"] == "Male" ),
                                                                               "total_bill"].mean() else '0')

##############################################3

## 24.SORU
df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag": ["count"]})


### 25.SORU
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
new_df = df.sort_values("total_bill_tip_sum",ascending=False).head(30)
new_df




########################################
df['total_bill_flag'] = df.apply(lambda x:'1' if x["total_bill"] >=20 else '0')

df.head()

df['name_match'] = df['first_name'].apply(lambda x: 'Match' if x == 'Bill' else 'Mismatch')

df.loc[(df['first_name'] != 'Bill') & (df['first_name'] != 'Emma'), 'name_match'] = 'Mismatch'




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