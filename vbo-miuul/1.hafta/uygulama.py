import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# List Comprehension Uygulamalar

# Bir Veri setindeki değişken isimlerini değiştirme

# before
#['total' ,'speeding', 'alcohol','not_distracted','no_previous','ins_premium','ins_losses','abbrev']

# after
# ['TOTAL','SPENDING','ALCOHOL','NOT_DISTRACTED','NO_PREVIOUS','INS_PREMIUM','INS_LOSSES','ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

A = []

for col in df.columns:
    A.append(col.upper())

print(A)

df =sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


##############
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
##############

[col for col in df.columns if "INS" in col]


["FLAG_"+ col for col in df.columns if "INS" in col]

["FLAG_"+ col if "INS" in col else "NO_FLAG_"+col for col in df.columns]

df.columns = ["FLAG_"+ col if "INS" in col else "NO_FLAG_"+col for col in df.columns]
df.columns

##############3

l = [2,13,18,93,22]

even_list= []
odd_list = []

for rakam in l:
    if rakam % 2== 0:
        even_list.append(rakam)
    else:
        odd_list.append(rakam)
print(even_list)

# 1'den 10'a kadar olan tek sayıların karesi, çift sayıların küpü bir sözlüğe eklenmek istemektedir.
# Key'ler Orijinal Değerler - Value'lar ise Değiştirilmiş değerler olacaktır.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 3
    else:
        new_dict[n] = n ** 2

new_dict


{n:n ** 3 if n % 2 == 0 else n ** 2 for n in numbers}