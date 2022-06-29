

text = "hi my name is john and i am learning python"

text[0]
text[1]
text[2]
text[3]

a = range(len(text))

if (int(a) %2 == 0):
    print("Çift sayılar")
else:
    print("Tek sayılar")

    if (i%2 == 0):
        print(text.upper())
    else:
        print(text.lower())


def text_check(text):
    new_string = ""
    for text_index in range(len(text)):
        if text_index % 2 == 0:
            new_string+= text[text_index].upper()
        else:
            new_string += text[text_index].lower()
    print(new_string)

[text[text_index].upper() if text_index % 2 == 0 else text[text_index].lower for text_index in range(len(text))]

text_check("gurkan")

text_new = "python spyder anaconda machine learning"

range(len(text_new))

text_new.split()
text.strip()

def revise(text_new):
    new_string=""
    for textind in range(len(text_new)):
        if textind %2 == 0:
            new_string += (text_new.strip())
        else:
            new_string += (text_new.split())
    print(new_string)

revise("python spyder")



##### break-continue-while #######

salaries = [1000,2000,3000,4000,5000]

for salary in salaries:
    if salary== 3000:
        break
    print(salary)


for salary in salaries:
    if salary== 3000:
        continue
    print(salary)


#### while

number = 1

while number < 5:
    print(number)
    number +=1

######### Uygulama Mülakat Sorusu

# Amaç : Çift Sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.
# Key'ler orijinal değerler , value değerleri değiştirilmiş değerlerdir.

numbers = range(10)

new_dict = {}

for number in numbers:
    if number % 2 == 0:
        new_dict[number] = number ** 2

print(new_dict)

{number: number ** 2 for number in numbers if number % 2 == 0}

