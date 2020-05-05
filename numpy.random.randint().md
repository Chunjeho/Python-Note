## Why we use this?
To **make numpy array filled with random number(integer).**

## How to use?
Use ``` numpy.random.randint(max, size=(row, column)) ```

## Example
### ex1)
[IN 01]
```
import numpy as np

a = np.random.randint(100, size=(3,4))

print(a)
print(a.shape)
print(a.dtype)
```
[OUT 01]
```
[[32 57 79 45]
 [19 76 45 43]
 [45 70 75 58]]
(3, 4)
int32
```
