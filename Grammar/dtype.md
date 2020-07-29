## Why we use this?
 To get **data type** of numpy array.
 
## How to use it?
```
 numpy.array().dtype
```
 
## Examples

### ex1)
 [IN 01]
 ```
 import numpy as np
 
 a = np.array([1,2,3])
 print(a.dtype)
 ```
  [OUT 01]
 ```
int32
 ```
 ### ex2)
  [IN 02]
 ```
 import numpy as np
 
 a = np.array([1,2,3], dtype='int8')
 print(a.dtype)
 ```
  [OUT 02]
 ```
int8
 ```
 ### ex3)
 [IN 03]
 ```
 import numpy as np
 
 a = np.array([1.1,3.14,7.6])
 print(a.dtype)
 ```
  [OUT 03]
 ```
float64
 ```

