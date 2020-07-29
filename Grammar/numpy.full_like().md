## Why we use this?
To **copy and paste same format of numpy array, which is filled with given number**.

## How to use?
Use ``` numpy.full_like(numpy.array(), number) ```

## Examples
### ex1)
[IN 01]
```
import numpy as np

a = np.zeros((3,4), dtype = 'int32')
b = np.full_like(a, 7)

print(a)
print(b)
print(b.shape)
print(a.shape)
print(b.dtype)
print(a.dtype)
```
[OUT 01]
```
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
[[7 7 7 7]
 [7 7 7 7]
 [7 7 7 7]]
(3, 4)
(3, 4)
int32
int32
```

### ex2)
[IN 02]
```
import numpy as np

a = np.zeros((3,4))
b = np.full_like(a, 7.2)

print(a)
print(b)
print(b.shape)
print(a.shape)
print(b.dtype)
print(a.dtype)
```
[OUT 02]
```
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
[[7.2 7.2 7.2 7.2]
 [7.2 7.2 7.2 7.2]
 [7.2 7.2 7.2 7.2]]
(3, 4)
(3, 4)
float64
float64
```
