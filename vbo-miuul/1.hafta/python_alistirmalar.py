###################################
## Görev 1
###################################

x= 8
type(x)

y=3.2
type(y)

z =8j+18
type(z)

a = "Hello World"
type(a)

b= True
type(b)

c = 23 < 22
type(c)

l = [1,2,3,4]
type(l)

d = {"Name":"Jake",
     "Age": 27,
     "Address":"Downtown" }
type(d)

t = ("Machine Learning","Data Science")
type(t)

s = {"Python","Machine Learning","Data Science"}
type(s)


####################################
### GÖREV 2
################################
text = "The goal is to turn data into information, and information into insight."

text1 = text.replace(","," ")
text2 = text1.replace("."," ")
text3 = text2.upper()
text3.split()

###############################
# GÖREV 3
###############################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

##### Adım 1
len(lst)

##### Adım 2
lst [0]
lst [10]

##### Adım 3
lst[0:4]

#### Adım 4
lst.pop(8)
lst

#### Adım 5
lst.append("X")
lst

#### Adım 6
lst.insert(8,"N")
lst

#### Bonus
dir(list)

lst.remove("X")
lst

###############################
# GÖREV 4
###############################

dict = {'Christian': ["America",18],
         'Daisy': ["England",12],
         'Antoino':["Spain",22],
         'Dante': ["Italy",25]}

# Adım 1
dict.keys()

# Adım 2
dict.values()

# Adım 3
dict['Daisy'][1] = 13
dict['Daisy']

# Adım 4
dict['Ahmet']= ["Turkey",24]
dict

# Adım 5

dict.pop('Antoino')
dict

###############################
# GÖREV 5
###############################

l = [2,13,18,93,22]

even_list= []
odd_list = []

for rakam in l:
    if rakam % 2== 0:
        even_list.append(rakam)
    else:
        odd_list.append(rakam)
print(even_list)

###############################
# GÖREV 6
###############################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

####List Comprehension

# Öncelikle for döngüsü içerisinde if else yapısını kullanırım.
# Nümerik değişkenler için sütun string değerini büyütüp "NUM" stringi eklerim.
# Kategorik değişken için ise yalnızca sütun string değerini büyütürüm.(upper)

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]



###############################
# GÖREV 7
###############################


### FLAG EKLEME

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col.upper() if "no" in col else col.upper()+"_FLAG" for col in df.columns]

###############################
# GÖREV 8
###############################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


og_list = [col for col in df.columns if "rev" in col ]
new_cols = [col for col in df.columns if col not in og_list ]

new_df = df[new_cols]
print(new_df)