###################################################
# Sorting Products
###################################################

###################################################
# Uygulama: Kurs Sıralama
###################################################

import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df= pd.read_csv('C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/product_sorting.csv')
print(df.shape)

df.head(10)

##########################3
# Sorting by Rating      #
########################

df.sort_values("rating",ascending=False).head(15)
# Out[7]:
#                                           course_name    instructor_name  purchase_count  rating  commment_count  5_point  4_point  3_point  2_point  1_point
# 0   (50+ Saat) Python A-Z™: Veri Bilimi ve Machine...  Veri Bilimi Okulu           17380 4.80000            4621     3466      924      185       46        6
# 10        İleri Düzey Excel|Dashboard|Excel İp Uçları  Veri Bilimi Okulu            9554 4.80000            2266     1654      499       91       22        0
# 19                     Alıştırmalarla SQL Öğreniyorum  Veri Bilimi Okulu            3155 4.80000             235      200       31        4        0        0
# 5                                            Course_1       Instructor_2            4601 4.80000             213      164       45        4        0        0
# 6                                            Course_2       Instructor_3            3171 4.70000             856      582      205       51        9        9
# 14                       Uçtan Uca SQL Server Eğitimi  Veri Bilimi Okulu           12893 4.70000            2425     1722      510      145       24       24
# 8            A'dan Z'ye Apache Spark (Scala & Python)  Veri Bilimi Okulu            6920 4.70000             214      154       41       13        2        4
# 13                                           Course_5       Instructor_6            6056 4.70000             144       82       46       12        1        3
# 27                                          Course_15       Instructor_1            1164 4.60000              98       65       24        6        0        3
# 1   Python: Yapay Zeka ve Veri Bilimi için Python ...  Veri Bilimi Okulu           48291 4.60000            4488     2962     1122      314       45       45
# 16                                           Course_6       Instructor_7             140 4.60000              20       10       10        0        0        0
# 4   (2020) Python ile Makine Öğrenmesi (Machine Le...  Veri Bilimi Okulu           11314 4.60000             969      717      194       38       10       10
# 3     R ile Veri Bilimi ve Machine Learning (35 Saat)  Veri Bilimi Okulu            6626 4.60000            1027      688      257       51       10       21
# 21                                          Course_10      Instructor_10             723 4.50000             130       68       47        9        3        3
# 7   Veri Bilimi için İstatistik: Python ile İstati...  Veri Bilimi Okulu             929 4.50000             126       88       26        9        0        3

##############################################
# Sorting by Comment Count or Purchase Count #
##############################################

# Sıralama yaparken kullanıcı memnuniyeti iyi olsa da
# satın alma sayısı ve rating değerini de göz ardı etmemiz gerekmektedir.

df.sort_values("purchase_count", ascending=False).head(10)


df.sort_values("commment_count", ascending=False).head(10)
# Out[13]:
#                                           course_name    instructor_name  purchase_count  rating  commment_count  5_point  4_point  3_point  2_point  1_point
# 0   (50+ Saat) Python A-Z™: Veri Bilimi ve Machine...  Veri Bilimi Okulu           17380 4.80000            4621     3466      924      185       46        6
# 1   Python: Yapay Zeka ve Veri Bilimi için Python ...  Veri Bilimi Okulu           48291 4.60000            4488     2962     1122      314       45       45
# 20                                           Course_9       Instructor_3           12946 4.50000            3371     2191      877      203       33       67
# 14                       Uçtan Uca SQL Server Eğitimi  Veri Bilimi Okulu           12893 4.70000            2425     1722      510      145       24       24
# 2            5 Saatte Veri Bilimci Olun (Valla Billa)       Instructor_1           18693 4.40000            2362     1582      567      165       24       24
# 15                      Uygulamalarla SQL Öğreniyorum  Veri Bilimi Okulu           11397 4.50000            2353     1435      705      165       24       24
# 10        İleri Düzey Excel|Dashboard|Excel İp Uçları  Veri Bilimi Okulu            9554 4.80000            2266     1654      499       91       22        0
# 3     R ile Veri Bilimi ve Machine Learning (35 Saat)  Veri Bilimi Okulu            6626 4.60000            1027      688      257       51       10       21
# 4   (2020) Python ile Makine Öğrenmesi (Machine Le...  Veri Bilimi Okulu           11314 4.60000             969      717      194       38       10       10
# 9                        Modern R Programlama Eğitimi  Veri Bilimi Okulu            6537 4.40000             901      559      252       72        9        9

##############################################
# Sorting by Rating, Comment & Purchase
##############################################

# rating, yorum ve satın alma değerlerine ilk etapta baktığımızda aynı ölçeğe
# sahip olmadıkları için bunları standartlaştırma metoduna gitmemiz gerekmektedir.
# çünkü sayıca üstün olan satın alma sayıları diğer rating ve yorum değerlerini ciddi
# oranda etkileyecektir.


df["purchase_count_scale"] = MinMaxScaler(feature_range=(1,5)).\
    fit(df[["purchase_count"]]).\
    transform(df[["purchase_count"]])


df["comment_count_scale"] = MinMaxScaler(feature_range=(1,5)).\
    fit(df[["commment_count"]]).\
    transform(df[["commment_count"]])

df.head()


# Bu değişkenler artık aynı cinse indirgendiği için bunları artık ortalamalarını alabiliriz
# ya da ağırlıklandırabiliriz.


df["comment_count_scale"] = MinMaxScaler(feature_range=(1,5)).\
    fit(df[["commment_count"]]).\
    transform(df[["commment_count"]])

# Bu üç değişkene göre hesapladığımız skor değerleri :
(df["comment_count_scale"] * 32/100 +
 df["purchase_count_scale"] * 26/100 +
  df["rating"] * 42/100)

# Bu ağırlıklara uygun olarak oluşturduğumuz fonksiyon:
def weighted_sorting_score(dataframe, w1=32, w2=26, w3=42):
    return (dataframe["comment_count_scale"] * w1 / 100 +
            dataframe["purchase_count_scale"] * w2 / 100 +
            dataframe["rating"] * w3 / 100)

df["weighted_sorting_score"] = weighted_sorting_score(df)

df.sort_values("weighted_sorting_score",ascending=False).head(15)

df[df["course_name"].str.contains("Veri Bilimi")].\
    sort_values("weighted_sorting_score",ascending=False).head(20)
# Out[28]:
#                                          course_name    instructor_name  purchase_count  rating  commment_count  5_point  4_point  3_point  2_point  1_point  purchase_count_scale  comment_count_scale  weighted_sorting_score
# 1  Python: Yapay Zeka ve Veri Bilimi için Python ...  Veri Bilimi Okulu           48291 4.60000            4488     2962     1122      314       45       45               5.00000              4.88470                 4.79510
# 0  (50+ Saat) Python A-Z™: Veri Bilimi ve Machine...  Veri Bilimi Okulu           17380 4.80000            4621     3466      924      185       46        6               2.43801              5.00000                 4.24988
# 3    R ile Veri Bilimi ve Machine Learning (35 Saat)  Veri Bilimi Okulu            6626 4.60000            1027      688      257       51       10       21               1.54669              1.88427                 2.93711
# 7  Veri Bilimi için İstatistik: Python ile İstati...  Veri Bilimi Okulu             929 4.50000             126       88       26        9        0        3               1.07451              1.10316                 2.52239


##############################################
# Bayesing Average Rating Score
##############################################

# Sorting Products with 5 Star Rated
# Sorting Products According to Distribution of 5 Star Rating

# Bayesing Average : Puan dağılımlarının üzerinden olasılıksal bir şekilde ağırlıklı ortalama
# hesabı yapar. Puanların ortalaması üzerinden bir hesaplama yapacağız.

# Bayesian Average Rating Function :
def bayesian_average_rating(n, confidence=0.95):
    if sum(n) == 0:
        return 0
    K = len(n)
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    N = sum(n)
    first_part = 0.0
    second_part = 0.0
    for k, n_k in enumerate(n):
        first_part += (k + 1) * (n[k] + 1) / (N + K)
        second_part += (k + 1) * (k + 1) * (n[k] + 1) / (N + K)
    score = first_part - z * math.sqrt((second_part - first_part * first_part) / (N + K + 1))
    return score

df["bar_sorting_score"] = df.apply(lambda x : bayesian_average_rating(x[["1_point",
                                                                         "2_point",
                                                                         "3_point",
                                                                         "4_point",
                                                                         "5_point"]]) , axis=1)


df.head()

df.sort_values("weighted_sorting_score",ascending=False).head(15)

df.sort_values("bar_sorting_score",ascending=False).head(15)
# Burada yalnızca bar score değerini "rating" lere yapmış bulunmaktayız.Burada tek
# odağa odaklanmamız gerekseydi bar score doğru sonuç verebilirdi. Fakat burada
# bizim birden fazla odaklanmaz gereken durum mevcut o sebeple

df[df["course_name"].index.isin([5, 1])].sort_values("bar_sorting_score", ascending=False)

# Out[37]:
#                                          course_name    instructor_name  purchase_count  rating  commment_count  5_point  4_point  3_point  2_point  1_point  purchase_count_scale  comment_count_scale  weighted_sorting_score  bar_sorting_score
# 5                                           Course_1       Instructor_2            4601 4.80000             213      164       45        4        0        0               1.37886              1.17859                 2.75165            4.63448
# 1  Python: Yapay Zeka ve Veri Bilimi için Python ...  Veri Bilimi Okulu           48291 4.60000            4488     2962     1122      314       45       45               5.00000              4.88470                 4.79510            4.51604

# Comment :
# Ratingler baz alındığında Course 1 için düşük yıldızlı değerlendirme neredeyse hiç
# yapılmadığı için diğer kursun önüne çıkmaktadır. Bayes Average rating bu noktada
# büyük yanılgıya düşmektedir.


####################
# Hybrid Sorting: BAR Score + Diğer Faktorler
####################


# Rating Products
# - Average
# - Time-Based Weighted Average
# - User-Based Weighted Average
# - Weighted Rating
# - Bayesian Average Rating Score

# Sorting Products
# - Sorting by Rating
# - Sorting by Comment Count or Purchase Count
# - Sorting by Rating, Comment and Purchase
# - Sorting by Bayesian Average Rating Score (Sorting Products with 5 Star Rated)
# - Hybrid Sorting: BAR Score + Diğer Faktorler


# Sektörlere göre sıralamaları belirlemek gerekir. Değişkenler kendi içerisinde değişebilir.


def hybrid_sorting_score(dataframe, bar_w=60, wss_w=40):
    bar_sorting_score = dataframe.apply(lambda x: bayesian_average_rating(x[["1_point",
                                                                     "2_point",
                                                                     "3_point",
                                                                     "4_point",
                                                                     "5_point"]]), axis=1)
    wss_score = weighted_sorting_score(dataframe)

    return bar_sorting_score*bar_w/100 + wss_score*wss_w/100


df["hybrid_sorting_score"] = hybrid_sorting_score(df)

df.sort_values("hybrid_sorting_score", ascending=False).head(20)

# Bu şekilde sıralama yaptığımızda herhangi bir kursun satın alma ve yorum sayısı düşük olmasına rağmen
# sıralamada iyi sıralarda bulunuyorsa bu kurs potansiyel vaat ediyor demektir.

# Bar score: Veri seti içerisinde yeni olsa da potansiyel vaat edenleri gösterebilmektedir.
# Bir şekilde potansiyeli yüksek fakat henüz istenilen social proof gösteremeyen kursları da
# Bar score yöntemiyle tespit edebiliriz.

df[df["course_name"].str.contains("Veri Bilimi")].\
    sort_values("hybrid_sorting_score",ascending=False).head(20)
# Out[45]:
#                                          course_name    instructor_name  purchase_count  rating  commment_count  5_point  4_point  3_point  2_point  1_point  purchase_count_scale  comment_count_scale  weighted_sorting_score  bar_sorting_score  hybrid_sorting_score
# 1  Python: Yapay Zeka ve Veri Bilimi için Python ...  Veri Bilimi Okulu           48291 4.60000            4488     2962     1122      314       45       45               5.00000              4.88470                 4.79510            4.51604               4.62766
# 0  (50+ Saat) Python A-Z™: Veri Bilimi ve Machine...  Veri Bilimi Okulu           17380 4.80000            4621     3466      924      185       46        6               2.43801              5.00000                 4.24988            4.66586               4.49947
# 3    R ile Veri Bilimi ve Machine Learning (35 Saat)  Veri Bilimi Okulu            6626 4.60000            1027      688      257       51       10       21               1.54669              1.88427                 2.93711            4.48208               3.86409
# 7  Veri Bilimi için İstatistik: Python ile İstati...  Veri Bilimi Okulu             929 4.50000             126       88       26        9        0        3               1.07451              1.10316                 2.52239            4.34219               3.61427


############################################
# Uygulama: IMDB Movie Scoring & Sorting
############################################


df= pd.read_csv('C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/movies_metadata.csv',low_memory=False)


df = df[["title","vote_average","vote_count"]]
df.head()

df.shape


########################
# Vote Average'a Göre Sıralama
########################


df.sort_values("vote_average",ascending=False).head(20)

df["vote_count"].describe([0.10, 0.25, 0.50, 0.70, 0.80, 0.90, 0.95, 0.99]).T

df[df["vote_count"] > 400].sort_values("vote_average", ascending=False).head(20)


df["vote_count_score"] = MinMaxScaler(feature_range=(1, 10)). \
    fit(df[["vote_count"]]). \
    transform(df[["vote_count"]])


########################
# vote_average * vote_count
########################

df["average_count_score"] = df["vote_average"] * df["vote_count_score"]

df.sort_values("average_count_score", ascending=False).head(20)


########################
# IMDB Weighted Rating
########################

# weighted_rating = (v/(v+M) * r) + (M/(v+M) * C)

# r = vote average
# v = vote count
# M = minimum votes required to be listed in the Top 250
# C = the mean vote across the whole report (currently 7.0)

# Film 1:
# r = 8
# M = 500
# v = 1000

# Birinci bölüm:
# (1000 / (1000+500))*8 = 5.33

# İkinci bölüm:
# 500/(1000+500) * 7 = 2.33

# Toplam = 5.33 + 2.33 = 7.66

#########################################

# Film 2:
# r = 8
# M = 500
# v = 3000

# Birinci bölüm:
# (3000 / (3000+500))*8 = 6.85

# İkinci bölüm:
# 500/(3000+500) * 7 = 1

# Toplam = 7.85

#######################################

# Bir iş yeri kendi has bir skorlama yöntemi geliştirmeli. Ağırlıklı olarak
# hesaplama yöntemi oluşturabilir.
# Bütün kitlenin ortalama sayısı, oy sayısı ve

M = 2500
C = df['vote_average'].mean()

df["vote_count"].describe().T

def weighted_rating(r, v, M, C):
    return (v / (v + M) * r) + (M / (v + M) * C)

df.sort_values("average_count_score", ascending=False).head(10)

weighted_rating(7.40000,11444.00000 ,M,C)

weighted_rating(8.10000 ,14075.00000,M,C)

df["weighted_rating"] = weighted_rating(df["vote_average"],
                                        df["vote_count"], M, C)

### Medium Function##

N = 1000
def weighted_rating_sort(r, v, N, C):
    return (v / (v + N) * r) + (N / (v + N) * C)


df["weighted_rating_sort"] = weighted_rating_sort(df["vote_average"],
                                                  df["vote_count"],N,C)


df.sort_values("average_count_score", ascending=False).head(10)

df.sort_values("weighted_rating", ascending=False).head(10)
# Out[73]:
#                                                    title  vote_average  vote_count  vote_count_score  average_count_score  weighted_rating
# 12481                                    The Dark Knight       8.30000 12269.00000           8.84519             73.41505          7.84604
# 314                             The Shawshank Redemption       8.50000  8358.00000           6.34437             53.92714          7.83648
# 2843                                          Fight Club       8.30000  9678.00000           7.18842             59.66388          7.74946
# 15480                                          Inception       8.10000 14075.00000          10.00000             81.00000          7.72567
# 292                                         Pulp Fiction       8.30000  8670.00000           6.54387             54.31414          7.69978
# 834                                        The Godfather       8.50000  6024.00000           4.85194             41.24146          7.65480
# 22879                                       Interstellar       8.10000 11187.00000           8.15332             66.04190          7.64669
# 351                                         Forrest Gump       8.20000  8147.00000           6.20945             50.91748          7.59377
# 7000       The Lord of the Rings: The Return of the King       8.10000  8226.00000           6.25996             50.70571          7.52155
# 4863   The Lord of the Rings: The Fellowship of the Ring       8.00000  8892.00000           6.68583             53.48661          7.47731


df.sort_values("weighted_rating_sort", ascending=False).head(10)
# Out[60]:
#                                                title  vote_average  vote_count  vote_count_score  average_count_score  weighted_rating_sort
# 314                         The Shawshank Redemption       8.50000  8358.00000           6.34437             53.92714               8.19205
# 12481                                The Dark Knight       8.30000 12269.00000           8.84519             73.41505               8.09789
# 834                                    The Godfather       8.50000  6024.00000           4.85194             41.24146               8.08972
# 2843                                      Fight Club       8.30000  9678.00000           7.18842             59.66388               8.04885
# 292                                     Pulp Fiction       8.30000  8670.00000           6.54387             54.31414               8.02267
# 15480                                      Inception       8.10000 14075.00000          10.00000             81.00000               7.93537
# 351                                     Forrest Gump       8.20000  8147.00000           6.20945             50.91748               7.91774
# 22879                                   Interstellar       8.10000 11187.00000           8.15332             66.04190               7.89636
# 1154                         The Empire Strikes Back       8.20000  5998.00000           4.83531             39.64955               7.83107
# 7000   The Lord of the Rings: The Return of the King       8.10000  8226.00000           6.25996             50.70571               7.83100



#######################################################################

def bayesian_average_rating(n, confidence=0.95):
    if sum(n) == 0:
        return 0
    K = len(n)
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    N = sum(n)
    first_part = 0.0
    second_part = 0.0
    for k, n_k in enumerate(n):
        first_part += (k + 1) * (n[k] + 1) / (N + K)
        second_part += (k + 1) * (k + 1) * (n[k] + 1) / (N + K)
    score = first_part - z * math.sqrt((second_part - first_part * first_part) / (N + K + 1))
    return score


bayesian_average_rating([34733, 4355, 4704, 6561, 13515, 26183, 87368, 273082, 600260, 1295351])

bayesian_average_rating([37128, 5879, 6268, 8419, 16603, 30016, 78538, 199430, 402518, 837905])

df_new = pd.read_csv("C:/Users/mgurk/PycharmProjects/pythonProject1/datasets/imdb_ratings.csv")

df_new.head()

df_new = df_new.iloc[0:, 1:]

df_new.head(20)

df_new["bar_score"] = df_new.apply(lambda x: bayesian_average_rating(x[["one", "two", "three", "four", "five",
                                                                "six", "seven", "eight", "nine", "ten"]]), axis=1)

df_new.sort_values("bar_score", ascending=False).head(20)


# Weighted Average Ratings
# IMDb publishes weighted vote averages rather than raw data averages.
# The simplest way to explain it is that although we accept and consider all votes received by users,
# not all votes have the same impact (or ‘weight’) on the final rating.

# When unusual voting activity is detected,
# an alternate weighting calculation may be applied in order to preserve the reliability of our system.
# To ensure that our rating mechanism remains effective,
# we do not disclose the exact method used to generate the rating.
