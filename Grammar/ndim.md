## Why we use this?

To get **dimensions** of numpy array.

## How to use?

Use 
```
numpy.array().ndim
```

## Examples

[IN 01]
```
import numpy as np

a = np.array([1,2,3])
print(a.ndim)
```
[OUT 01]
```
1
```

[IN 02]
```
import numpy as np

a = np.array([1,2,3], ndmin = 2)
print(a.ndim)
```
[OUT 02]
```
2
```

[IN 02]
```
import numpy as np

a = np.array([[1,2,3],[4,5,6]], ndmin = 2)
print(a.ndim)
```
[OUT 02]
```
2
```
