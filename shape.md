## Why we use this?

To get a shape of the numpy array.

## How to use it?
Use 
```
numpy.array().shape
```

## How it works?
If dimension = 1, output is ```(row,)```.

Else if dimension > 1, output is ```(column, row)```.

## Examples

**[IN 01]**
```
import numpy as np

a = np.array([1.0, 3.0, 6.0])
print(a.shape)
```
**[OUT 01]**
```
(3,) 
```

**[IN 02]**
```
import numpy as np

a = np.array([[1.0, 3.0, 6.0], [6.1, 5.4, 7.3]])
print(a.shape)
```
**[OUT 02]**
```
(2,3) 
```
