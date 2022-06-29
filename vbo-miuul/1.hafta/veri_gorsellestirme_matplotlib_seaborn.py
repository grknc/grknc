##          VERİ GÖRSELLEŞTİRME - MATPLOTLIB & SEABORN

#           MATPLOTLIB
#   * Low-level(Düşük Seviye) bir görselleştirme aracıdır.
#   * Seaborn kütüphanesine kıyasla daha fazla çaba ile veri görselleştirme yapabilirsiniz.
#   * Grafik biçimlendirme


# ! Veri görselleştirme geniş bir konu olup buradaki görselleştirme araçlarına hakim olmak en önemli durumdur.
# ! Hangi değişken için hangi görselleştirme tekniğini uygulamalıyım?

#   Kategorik değişkenler için sütun grafik ( countplot, barplot gibi)
#   Sayısal değişkenler için değişkenin dağılımı yani hist , boxplot


import matplotlib.pyplot as plt
#   Power BI , Tableau gibi araçlar veri görselleştirme için daha uygundur.
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")

df.head()

df.info()


df["sex"].value_counts().plot(kind='bar')
plt.show(block= True)




###     SAYISAL DEĞİŞKEN GÖRSELLEŞTİRME

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

df= sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show(block=True)

plt.boxplot(df["fare"])
plt.show(block=True)

# Bu iki grafik istatistiksel grafiklerdir. Bir veriyi tanırken asıl amacımız dağılım yapılarını gözlemlemektir.
# Hist Sayısal değişken ve kutu grafik, bize hem sayısal değişkenin aralıklarında hangi frekanslarda gözlemler
# veri setinin içindeki bu değişkenin keni içindeki dağılım bilgisini verir.


##  W    MATPLOTLIB'IN OZELLIKLERI

# PLOT
import numpy as np

x = np.array([1,8])
y = np.array([0,150])

plt.plot(x,y)
plt.show(block=True)


plt.plot(x,y,'o')
plt.show(block=True)

# MARKER

y = np.array([13,28,11,100])

plt.plot(y,marker='o')
plt.show(block=True)


markers = ['o','*','.',',','x'+'X'+'s']

# LINE

y = np.array([13,28,11,1088])
plt.plot(y,linestyle = "dotted")
plt.show(block = True)



y = np.array([13,28,11,1088])
plt.plot(y,linestyle = "dotted")
plt.show(block = True)

# MULTIPLE LINES

x = np.array(
)

# BAŞLIK

plt.title("Ana Başlık")


plt.x
plt.ylabel

# PLOT 1
z = np.array([2,10])

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot (1,2,1)
plt.title("Weird")
plt.plot(x,y)


x = np.array([8,8,9,9,10,10,11,11,12,12])
y = np.array([24,25,26,27,28,29,30,31,32,33])
plt.subplot (1,2,2)
plt.title("4")
plt.plot(x,y)
plt.show(block=True)


###     SEABORN

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")
df.head()


df["sex"].value_counts()

sns.countplot(x= df["sex"],data=df)
plt.show(block=True)


### SAYISAL DEĞİŞKENLER İÇİN

sns.boxplot(x=df["total_bill"])
plt.show(block=True)