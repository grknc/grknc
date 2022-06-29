# KEŞİFÇİ VERİ ANALİZİ

# GENEL RESİM
# KATEGORİK DEĞİŞKEN ANALİZİ
# SAYISAL DEĞİŞKEN ANALİZİ
# HEDEF DEĞİŞKEN ANALİZİ
# KORELASYON ANALİZİ

#### GENEL RESİM

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()

# Veri seti içerisinde son 5 data
df.tail()

# Veri seti içerisindeki satır-sütun bilgisi
df.shape

# Data Frame Detay Bilgi
df.info()

# Data Frame Değişkenler
df.columns

# Data Frame Index Bilgisi
df.index

# Data Frame Sayısal Değişkenleri Betimleme
df.describe().T

# Data Frame içerisinde eksik değer var mı yok mu?
df.isnull().values.any()

# Veri seti içerisindeki eksik değerlerin toplamı
df.isnull().sum()


def check_df(dataframe,head=5):
    print("#### Shape #### ")
    print(dataframe.shape)
    print("### Types ###")
    print(dataframe.dtypes)
    print("### Head ###")
    print(dataframe.head(head))
    print("### Tail ###")
    print(dataframe.tail(head))
    print("### NA ###")
    print(dataframe.isnull().sum())
    print("### Quantiles ###")
    print(dataframe.describe([0, 0.05,0.5,0.95,0.99,1]).T)

check_df(df)


new_df = sns.load_dataset("tips")

check_df(new_df)

###############################################
#### ANALYSIS OF CATEGORICAL VARIABLES

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()


# Tek bir değişkenin sınıf sayıları için :
df["embarked"].value_counts()

# Tek bir değişkenin unique değerleri için :
df["sex"].unique()

# Bir değişkende toplamda kaç eşsiz değer mevcuttur?
df["sex"].nunique()

# Bazı kategorik değişkenler, veri içerisinde tam gözükmemektedir. Bunu veriyi doğru analiz ettiğimizde fark edebiliriz.
# Kategorik değişken örnekleri; cinsiyet,eğitim durumu, ülkeler, futbol takımları, sınıf durumları vb. durumlar
###################################################################################
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

df["sex"].dtypes

str(df["sex"].dtypes)

str(df["sex"].dtypes) in ["object"]

df["survived"].value_counts()

# Sınıf sayılarına göre numerik kategoriye sahip olan değişkenleri analiz edelim. Bunlar içerisinde sınıf sayısı belli
# değerin altında olanları kategorik olarak yorumlayabiliriz.

###################################################################################
# Numerik görünümlü kategorik değişkenleri göstermek için :
num_but_cat = [col for col in df.columns if (df[col].nunique() < 10) and df[col].dtypes in ["int64","float64"]]
num_but_cat

# Diğer bir durumda kategorik olarak gözüküp aslında kategorik değişken sınıfına uygun olmayanları tespit etmektir.
# Çok fazla sayıda eşsiz bir değere sahip olmamalıdır.

###################################################################################
# Kategorik görünümlü numerik değerler mevcut mudur?
cat_b_num = [col for col in df.columns if (df[col].nunique() > 20) and str(df[col].dtypes) in ["category","object"]]
cat_b_num


cat_cols = cat_cols + num_but_cat
cat_cols

df[cat_cols]

# Kategorik değişkenlerin frekanslarına bakıyoruz.
df[cat_cols].nunique()

# Kategorik değişkenlerin dışında kalan değişkenler:
[col for col in df.columns if col not in cat_cols]


# Fonksiyon Yazılımı

# Hangi sınıftan kaçar tane mevcut?
df["survived"].value_counts()

# Sınıfların yüzdelik bilgisi
100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")

cat_summary(df,"sex")

# Tüm kategorik değişkenlerin durumuna yönelik hesaplama yaptığımızda :)
for col in cat_cols:
    cat_summary(df,col)

# Patron çıldırsın istiyorum :)

# Kategorik Değişken Analizi - Plot Görselleştirme Durumu

def cat_summary(dataframe,col_name,plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")

    if plot:
        sns.countplot(x=dataframe[col_name],data=dataframe)
        plt.show(block=True)


# Fonksiyonun içerisinde data framelerde genelde döngüler dışarıda bir noktaya yazılmaktadır. "Data Frame" ve "Değişken"
# fonksiyonunda yaptığımız gibi. Birden fazla değişkeni bu fonksiyona entegre etmek istiyorsanız ayrı bir döngü yazarsınız.

for col in cat_cols:
    cat_summary(df,col,plot=True)

# Countplot methodunu genellenebilir yaptıkları için bool kategorik değişkeni için görselleştirme vermedikleri için
# bu noktada hata almış bulunmaktayız.

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df,col,plot=True)
    else:
        cat_summary(df,col,plot=True)

# Büyük ölçekli işlerde mümkün olduğu kadar az ve takip edilebilir özellik kullanılarak ilerlemek gerekmektedir.


# Kompleks Bir Yapıda Fonksiyonu Tekrardan Yazarsak :

def cat_summary(dataframe,col_name,plot=False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("#########################################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("#########################################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


cat_summary(df,"adult_male",plot=True)


################################################
#### ANALYSIS OF NUMERICAL ANALYSIS

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()


df[["age","fare"]].describe().T

# Nümerik değişkenleri seçmek için :

num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]

num_cols = [col for col in num_cols if col not in cat_cols]
num_cols

# Veri setindeki en önemli durum; kategorik ve numerik değişkenleri doğru seçebilmektir. (Sistematik durumu yapmak ;))

# Sayısal değişkenlerin describe methodunun fonksiyonunu yazdırmak
def num_summary(dataframe,numerical_col):
     quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
     print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)


# Sayısal değişkenlerin describe methodunun fonksiyonuna görsellik katmak istersek:
def num_summary(dataframe,numerical_col,plot=False):
     quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
     print(dataframe[numerical_col].describe(quantiles).T)

     if plot:
         dataframe[numerical_col].hist()
         plt.xlabel(numerical_col)
         plt.title(numerical_col)
         plt.show(block=True)


num_summary(df,"age",plot=True)

for col in num_cols:
    num_summary(df,col,plot=True)


##############################################333
# CAPTURING VALUES AND GENERALIZING OPERATIONS

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()
df.info()


# docstring : Fonksiyona tanım yazmak için kullanılır.
def grap_col_names(dataframe,cat_th=10 , car_th = 20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe'dir.

    cat_th : int,float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri

    car_th : int,float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
        cat_cols : list
            Kategorik değişken listesi
        num_cols : list
            Numerik değişken listesi
        cat_but_car : list
            Kategorik görünümlü kardinal değişken listesi

    Notes
    -------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_car değişkeni cat_cols'un içerisindedir.
        Return olan 3 liste toplamı, toplam değişken sayısına eşittir.
    """

    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if (df[col].nunique() < 10) and df[col].dtypes in ["int64", "float64"]]
    cat_but_car = [col for col in df.columns if
                 (df[col].nunique() > 20) and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car : {len(cat_but_car)}")
    print(f"num_but_cat : {len(num_but_cat)}")

    return cat_cols,num_cols,cat_but_car



cat_cols,num_cols,cat_but_car = grap_col_names(df)

cat_cols
num_cols
cat_but_car


df["deck"]
#### KATEGORİK DEĞİŞKENLERİN ÖZETİ

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#########################################################################")


for col in cat_cols:
    cat_summary(df,col)


#### NUMERİK DEĞİŞKENLERİN ÖZETİ

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df,col,plot=True)



# bonus

df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols,num_cols,cat_but_car = grap_col_names(df)


########################################################
# ANALYSIS OF TARGET VARIABLE

# Veri setindeki hedef değişkeni, ana seti ya da odak değişkeni genellikle biliriz.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()

cat_summary(df,"survived")

# Bağımlı değişkene göre bu hedef değişkeni analiz etmemiz gerekmektedir.

# Hedef Değişken ile Kategorik Değişkenlerin Analizi

df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe,target,categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))
    print("###################################")

target_summary_with_cat(df,"survived","sex")

target_summary_with_cat(df,"survived","pclass")

for col in cat_cols:
    target_summary_with_cat(df,"survived",col)

# Bütün kategorik değişkenlerle hedef değişkenin arasındaki ilişkiyi burada görebilmekteyiz.


# Hedef Değişken ile Sayısal Değişkenlerin Analizi

df.groupby("survived")["age"].mean()
df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe,target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col:"mean"}), end="\n\n")
    print("###################################")

target_summary_with_num(df,"survived","age")

for col in num_cols:
    target_summary_with_num(df,"survived",col)


#################################
# KORELASYON ANALİZİ

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:,1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in [int,float]]

corr = df[num_cols].corr()
corr

sns.set(rc= {'figure.figsize': (12,12)})
sns.heatmap(corr,cmap="RdBu")
plt.show(block=True)
# Korelasyon : Değişkenlerin birbiriyle ilişkisi ifade eden istatistiksel bir ölçümdür. (-1:1) değerleri arasındadır.
# Yüksek korelasyona sahip değişkenlerle çalışma yapmayı genel itibariyle istemeyiz. Çünkü benzer davranışları göstereceklerdir.


# Yüksek Korelasyonlu Değişkenlerin Silinmesi

cor_matrix = df.corr().abs()

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))

upper_triangle_matrix

drop_list = [col for col in upper_triangle_matrix if any(upper_triangle_matrix[col] > 0.90 )]

drop_list

df.drop(drop_list,axis=1)


# Kaggle - Veri Seti


# Conclusion

# Her yaptığı tekrarlı işlem için fonksiyon oluşturmuş.
# Grafik yönteminden çekinmektedir.
# Az yer kaplayacak şekilde kodlarını sade ve basit bir şekilde oluşturmaktadır.


