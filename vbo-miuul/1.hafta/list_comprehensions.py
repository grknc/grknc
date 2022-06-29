



salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
    return x*20/100 + x


null_list =[]

for salary in salaries:
    null_list.append(new_salary(salary))


for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

print(null_list)


[new_salary(salary * 2) if salary<3000 else new_salary(salary) for salary in salaries]

[salary*2 for salary in salaries]

[salary*2 for salary in salaries if salary <3000]

[salary*2 if salary <3000 else salary * 0 for salary in salaries]


[new_salary(salary*3) if salary <3000 else new_salary(salary * 0.2) for salary in salaries]


football_players = ["James","White","Rice","Xavi","Iniesta"]

spanish_players = ["Xavi","Iniesta"]


[players.lower() if players in spanish_players else players.upper() for players in football_players]


[players.upper() if players not in spanish_players else players.lower() for players in football_players]


#### Dict Comprehension

dictionary = {  'a':1,
                'b':2,
                'c':3,
                'd':4
}

dictionary.keys()
dictionary.values()
dictionary.items()


{k : v**2 for (k,v) in dictionary.items()}

{k.upper() : v for (k,v) in dictionary.items()}


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

#####
# Amaç key'i string , value aşağıdaki gibi bir liste olan sözlük oluşturmak
# Sadece sayısal değişkenler seçilecek.
#####

# Output
# { 'total':['mean','min','max','var'],
#   'speeding': ['mean','min','max','var'],


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O" ]
cat_cols = [col for col in df.columns if df[col].dtype == "O" ]

print(num_cols)
print(cat_cols)

soz = {}
agg_list = ["mean","min","max","sum"]

for col in num_cols:
    soz[col] = agg_list
print(soz)

{ col: agg_list for col in num_cols}


###################################
#TRAINING

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col for col in df.columns]

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# TRAINING 2
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col.upper() if "no" in col else col.upper()+"_FLAG" for col in df.columns]



#TRAINING 3

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = [col for col in df.columns if "rev" in col ]

new_cols = [col for col in df.columns if col not in og_list ]

new_df = df[new_cols]
print(new_df)