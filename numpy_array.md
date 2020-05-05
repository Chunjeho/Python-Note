## Why we use this?

To make **numpy array** in our code.

## How to do that?
Use
```
numpy.array()
```
## Examples
[IN 01] 
```
import numpy as np

a = np.array([1,2,3])
print(a)
```
[OUT 01]
```
[1,2,3]
```
[IN 02]
```
import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a)
```
[OUT 02]
```
[[1,2,3]
 [4,5,6]]
```

## At a glance
\* : essential

```
numpy.array(*object, dtype=None, ndmin=0 ...)
```
* object: array that anything you want.

  ex) [1, 2, 3], [1.0, 2.0, 3.0], [[10, 40, 50], [90, 50, 40]]
  
* dtype: data type. (quite a different from python data type, it's more simple than that)

  ex) dtype='int8', dtype='int16', dtype='int32', dtype='float16' ... (The number after the data type represents the bits that you'll goona use.) 

* ndim: Same as asking "How many dimensions you want?". 

For other parameters visit: https://numpy.org/doc/stable/reference/generated/numpy.array.html?highlight=array#numpy.array
