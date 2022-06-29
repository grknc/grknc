# NUMPY

# WHY NUMPY ?

# Sabit tipte veri saklar. Verimlidir. Hızlı bir şekilde çalışır.
# Fonksiyonel düzeyde, yüksek düzeyde olduğu için kullanım kolaylığı sağlar.

# CREATING NUMPY ARRAYS

# ATTRITUBES OF NUMPY ARRAS

# RESHAPING

# INDEX SELECTION

# SLICING

# FANCY INDEX

# CONDITIONS ON NUMPY

# MATHEMATICAL OPERATIONS



import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
ab

#####

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

np.zeros(10, dtype=int)

# 0'dan 10'a kadar toplamda 10 rakam içeren bir array oluşturmak
np.random.randint(0, 10, size=10)

# Ortalaması 10 , standart sapması 4 olan (3,4) formatından bir array oluşturmak
np.random.normal(10, 4, (3, 4))

# Attributes of Numpy Arrays

import numpy as np

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(10, size=5)
a

a.ndim
a.shape
a.size
a.dtype

b = np.random.randint(1, 10, size=9).reshape(3, 3)

b

# Index Selection

a[::]

m = np.random.randint(10, size=(3, 5))
m

m[0, 2] = 45

m[1, 2] = 32.5

# Değerler "int" değere sahipse siz yeni atadığınız değerde "float" olarak atasanız bile değişen değer yine "int" değerinde olacaktır.

m[0:2, 0:1]

### Fancy Index

import numpy as np

v = np.arange(0, 30, 3)
v[1]
v[4]

v

# Elimizde 1'den fazla(belki yüzlerce) index olması durumunda tek tek yazmak ya da kullanmak için fancy index kullanmaktayız.

catch = [3, 5, 7]

v[catch]

# Bir liste belirlemesi yapıp bu listedeki elemanlara göre ilgili index seçimi yapabiliriz.


### Nump Koşullu İşlemler ( Conditions on Numpy)

import numpy as np

z = np.array([1, 2, 3, 4, 5])

###########
# Klasik Yöntem
###########

ab = []
for i in z:
    if i < 3:
        ab.append(i)

print(ab)
ab.clear()
ab.sort()

### With Numpy

z < 3

# Numpy da arrayler üzerinden direk koşullu ifadeleri "True,False" şeklinde görebiliyoruz.
# Bunları bir liste ya da ilerleyen süreçte data frame olarak görebilmek için mevcut data frame e index olarak girebiliriz.

z[z < 3]

z[z < 3].dtype

# Vektörel seviyede otomatik olarak "numpy" bunu yapıyor ve ilgili değerleri bize sunuyoruz.

a = np.array([2.0, 3.5, 5.5, 6.2])
a

b = np.array(["3", "1", "4", "5"])
b

np.array([s[0].astype(int) for s in b])

b == "3"

b[b != "3"]

# dtype "U1" nedir? String ifadenin numpy üzerindeki data tipi midir?


### Mathematical Operations

import numpy as np

c = np.array([5, 10, 15, 20, 25])

c / 5

# Çıktıları float olarak değil de int tam sayı değerinde göstermek için aşağıdaki yöntemi kullanırız.
(c / 5).astype(int)

(c / 4).astype(int)

(c * 5 / 10).astype(int)

(c * 5 / 10).astype(complex)

#####################################

np.sum()

"""
numpy.core.fromnumeric
@array_function_dispatch(_sum_dispatcher)
def sum (a: Union[ndarray,Iterable,int,float],
        axis : Union[None,int,Iterable,tuple[int]=None,
        dtype : Optional[object] = None,
        out : Optional[object] =None,
        keepdims : Optional[bool] = np._NoValue,
        initial: Union[int,float,complex,None] = np._NoValue,
        where: Union[ndarray,Iterable,int,float[bool],None] = np._NoValue)
"""

np.sum([0.5, 1.5])
np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
# Çıktı : 1

np.sum([[0, 1], [0, 5]])
# Çıktı : 6

np.sum([[0, 1], [0, 5]], axis=0)
# Çıktı : array([0, 6])

np.sum([[0, 1], [0, 5]], axis=1)
# Çıktı : array([1, 5])

np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)
# Çıktı : array([1., 5.])

np.ones(128, dtype=np.int8).sum(dtype=np.int8)
#Çıktı : -128

np.sum([10], initial=5)
#Çıktı : 15


np.subtract()

"""
numpy.core._multiarray_umath 
def subtract(x1: Union[Number, ndarray, Iterable],
             x2: Union[Number, ndarray, Iterable],
             *args: Any,
             **kwargs: Any) -> ndarray
             
subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
Subtract arguments, element-wise.

"""

np.subtract(1.0, 4.0)
# Çıktı : -3.0
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
np.subtract(x1, x2)
# Çıktı : array([[ 0.,  0.,  0.],
#               [ 3.,  3.,  3.],
#               [ 6.,  6.,  6.]])

x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
x1 - x2
#Çıktı : array([[0., 0., 0.],
#               [3., 3., 3.],
#               [6., 6., 6.]])

np.var()

"""
numpy.core.fromnumeric @array_function_dispatch(_var_dispatcher) def var(a: Union[ndarray, Iterable, int, float],
        axis: Union[None, int, Iterable, tuple[int]] = None,
        dtype: Optional[object] = None,
        out: Optional[ndarray] = None,
        ddof: Optional[int] = 0,
        keepdims: Optional[bool] = np._NoValue,
        *,
        where: Union[ndarray, Iterable, int, float[bool], None] = np._NoValue)
"""

a = np.array([[1, 2], [3, 4]])
np.var(a)
# Çıktı : 1.25
np.var(a, axis=0)
#Çıktı :array([1.,  1.])
np.var(a, axis=1)
#Çıktı : array([0.25,  0.25])

a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
np.var(a)
#Çıktı : 0.20250003

np.var(a, dtype=np.float64)
#Çıktı : 0.20249999932944759 # may vary
((1-0.55)**2 + (0.1-0.55)**2)/2
#Çıktı : 0.2025

a = np.array([[14, 8, 11, 10], [7, 9, 10, 11], [10, 15, 5, 10]])
np.var(a)
#Çıktı : 6.833333333333333

np.mean()

"""
numpy.core.fromnumeric @array_function_dispatch(_mean_dispatcher) def mean(a: Union[ndarray, Iterable, int, float],
         axis: Union[None, int, Iterable, tuple[int]] = None,
         dtype: Optional[object] = None,
         out: Optional[ndarray] = None,
         keepdims: Optional[bool] = np._NoValue,
         *,
         where: Union[ndarray, Iterable, int, float[bool], None] = np._NoValue)
         
"""

a = np.array([[1, 2], [3, 4]])
np.mean(a)
# Çıktı : 2.5
np.mean(a, axis=0)
#Çıktı : array([2., 3.])
np.mean(a, axis=1)
#Çıktı : array([1.5, 3.5])

#In single precision, mean can be inaccurate:
a = np.zeros((2, 512*512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1
np.mean(a)
#Çıktı : 0.54999924

#Computing the mean in float64 is more accurate:
np.mean(a, dtype=np.float64)
#Çıktı : 0.55000000074505806 # may vary


### NumPy ile İki Bilinmeyenli Denkleme Çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5,1],[1,3]])
b = np.array([12,10])

np.mean(a)
#Çıktı : 2.5
np.mean(b)
#Çıktı : 11

np.var(a)
#Çıktı : 2.75
np.var(b)
#Çıktı : 1

#İki Bilinmeyenli Denklemin Numpy üzerinde Çözümü
np.linalg.solve(a,b)
# Çıktı : array([1.85714286, 2.71428571])


