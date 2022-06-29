
# Example 1

# Iterating through a string Using for Loop

ml = "machine learning"
ml_letters = []

for letter in ml:
    ml_letters.append(letter)

print(ml_letters)

# Iterating through a string Using List Comprehension

ml_letters = [letter for letter in ml]
print(ml_letters)

# Syntax of List Comprehension

[expression for item in list ]

#Example 2

## Create New Function

def new_salary(salary,rate):
    return int(salary*rate/100 + salary)

# Salaries List
salaries = [10500,24500,31500,42500,53500]

# Define New Salaries List
salaries_new = []

### For Loop and If...Else Conditions with Specified Function
for salary in salaries:
    if salary >= 30000:
        salaries_new.append(new_salary(salary,10))
    else :
        salaries_new.append(new_salary(salary,20))

# Check the Last Salaries
salaries_new


# List Comprehension

[new_salary(salary,10) if salary >=30000 else new_salary(salary,20) for salary in salaries]


# Example 3
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


#Dictionary Comprehension
{n:n ** 3 if n % 2 == 0 else n ** 2 for n in numbers}

# Example 4
import seaborn as sns
df = sns.load_dataset("penguins")
df.columns

### Kategorik değişkenlere sahip sütunların başına CAT ekledik ve tüm sütunları büyük harf yaptık.
# List Comprehension
["CAT_"+ col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]


# Traditional approach
new_columns = []
for col in df.columns:
    if df[col].dtype == "O":
       new_columns.append( "CAT_" + col.upper())
    else:
        new_columns.append(col.upper())

new_columns


# Example 5

# List Comprehension

measure_list = [col for col in df.columns if "_mm" in col ]

new_cols = [col for col in df.columns if col not in measure_list ]

new_df = df[new_cols]
print(new_df)