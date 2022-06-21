#############################
#Fonksiyon Okuryazarlığı
#############################


def calculate(x):
    print(x**2)


calculate(10)

def sum(arg1,arg2):
    """
    Sum of two numbers

    Parameters
    arg1 : int,float
    arg2 : int,float

    Returns
    int,float

    """
    print(arg1+arg2)


def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

say_hi()


def multiplication(a,b):
    c = a * b
    print(c)

multiplication(10,9)

###### Liste ve Append Fonksiyon ##########

list =[]
def add_element(a,b):
    c = a * b
    list.append(c)
    print(list)

add_element(3,2)

add_element(12,6)

########### Ön Tanımlı Argümanlar / Parametreler #############

def divide(a,b):
    print(a/b)

divide(8,3)

def divide(c,d=2):
    print(c/d)

divide(15)

##  print fonksiyonunda birçok ön tanımlı argüman bulunmaktadır.


########### Ne Zaman Fonksiyon Yazılmalıdır? ##################3

# warm , moisture , charge

""" Birbirini tekrar eden görevler olduğunda fonksiyon yazma ihtiyacı doğacaktır."""

def calculate(warm,moisture,charge):
    print((warm+moisture)/charge)

calculate(95,65,30)


###### Return : Fonksiyon çıktılarını girdi olarak kullanmak

def calculate(warm,moisture,charge):
    return (warm+moisture)/charge



def calculate(warm,moisture,charge):
    warm = warm * 2
    moisture = moisture*2
    charge = charge*2
    output= (warm + moisture)/charge

    return warm,moisture,charge,output

calculate(95,65,30)


######## Fonksiyon içerisinden fonksiyon çağırmak

def standarization(a,p):
    return a*10/100 * p * p

standarization(45,1)


def all_calculation(warm,moisture,charge,a,p):
    print(calculate(warm,moisture,charge))
    b = standarization(a,p)
    print(b*10)

all_calculation(1,3,5,9,12)


######

list_store=[1,2]

def add_element(a,b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(12,9)


#############
#KOŞULLAR
#############

number = 40

if number == 45:
    print("number is 40")

number = 45

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(15)


## elif

def number_check(number):
    if number > 20:
        print("greater than 20")
    elif number < 20:
        print("less than 20")
    else:
        print("equal to 20")

number_check(25)


##### LOOPS

# for loop

students = ["John","Mark","Philip"]

students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())


salaries = [1000,2000,3000,5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary*20/100+salary))

## Create New Function

def new_salary(salary,rate):
    return int(salary*rate/100 + salary)

# Define the List
salaries = [10500,24500,31500,42500,53500]

# For loop and Conditions with specified function
for salary in salaries:
    if salary >= 30000:
        print(new_salary(salary,10))
    else :
        print(new_salary(salary,20))

