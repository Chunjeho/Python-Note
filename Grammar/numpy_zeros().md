## Why we use this?
To make **new numpy array filled with 0(integer)**.

## How to use?
Use ``` numpy.zeros((row, column)) ```

## Examples
### ex1)
[IN 01]
```
import numpt as np

a = np.zeros((4,3))
print(a)
print(a.shape)
print(a.dtype)
```
[OUT 01]
```
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
(4, 3)
float64
```

### ex2)
[IN 02]
```
import numpt as np

a = np.zeros((3, 4), dtype = 'int32')
print(a)
print(a.shape)
print(a.type)
```
[OUT 02]
```
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
(3, 4)
int32
```
