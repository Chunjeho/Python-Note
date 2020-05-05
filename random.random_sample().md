## Why we use this?
To **make a same format of numpy array filled with random number(0.xxx)**

## How to use
Use ``` numpy.random.random_sample(numpy.array().shape) ```.

## Examples
### ex1) 

[IN 01]
```
import numpy as np

a = np.zeros((3,5))
b = np.random.random_sample(a.shape)

print(b)
print(a.shape)
print(b.shape)

```
[OUT 01]
```
[[0.1092322  0.73086589 0.26442903 0.31513967 0.86726354]
 [0.86233736 0.6749824  0.18952693 0.22676598 0.97933398]
 [0.47400054 0.69452685 0.16089439 0.07260235 0.02910256]]
(3, 5)
(3, 5)
```
