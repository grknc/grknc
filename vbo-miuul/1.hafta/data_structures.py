###############################
# DATA STRUCTURES

##############################

# Integer

x = 50

type(x)

y = 0.3
type(y)

#Boolean
True
False

#Liste

x = ["btc","eth","xrp"]
type(x)

#Sözlük

y = {"name":"Yigithan","Age":4}
type(y)

#Tuple

z = ("python","R","AI")
type(z)


####string methods

dir(str)
type(len)

len("gurkan")

name = "gurkan"


###upper & lower methos

"gurkan".upper()
"GURKAN".lower()

#### replace : karakter değiştirir

hello = "Welcome AI "

hello.replace("W","m")


#### split : böler

"Welcome AI".split()

###sprit

"Welcome".strip("W")

#### capitalize : ilk harfi büyür

"yigithan".capitalize()


### List

# Değiştirilebilir
# Sıralıdır
# Kapsayıcıdır.

notes = [0,1,2,3]
type(notes)

ng = ["s","e","k","a",4,True,[3,6,9]]

len(ng)

ng[5]
ng[6][0]

ng[0]="m"
ng

# List methods

dir(ng)

#append : eleman ekleme

ng.append("case")


# insert : index eklemek

ng.insert(0,"s")
ng

# dictionary

# değiştirilebilir.
# sırasız
# kapsaıcı

# key -value

dictionary = {"REG": "Regression",
              "lOG": "Logistic"}

dictionary = {"RMD": ["REAL", 14],
               "LIV" : ["LIVERPOOL", 7]}

dictionary["RMD"]

# key sorgulama

"RMD" in dictionary

dir(dict)

#key e göre value ya erişmek

dictionary.get("LIV")

#### Value Değiştirmek

dictionary["LIV"]= ["LIVERPOOL",6]

# Tüm keylere erişmek

dictionary.keys()

# Tüm values erişmek
dictionary.values()

# Tüm çiftleri tuple halinde listeye çevirme

dictionary.items()

# key value değerini update etmek

dictionary.update({"RMD":"REAL MADRID"})

# Yeni Key-Value Eklemek

dictionary.update({"JUV":"JUVENTUS"})

dictionary


# Tuple (Demet)

# Değiştirilemez
# Sıralıdır
# Kapsayıcıdır.

t = ("jason","statham",35,15)

t[0]="gg"

# Set
print("a","b",sep=".")
print("a","b")


def calculate():
    print()
# Değiştirilebilir
# Sırasız ve Eşsizdir.
# Kapsayıcıdır.

## difference - iki kümenin farkı

set1 = set()

text = "The goal is to turn data into information, and information into insight."

text.upper()

text.replace(","," ")
text.replace("."," ")

"The goal is to turn data into information, and information into insight.".split()