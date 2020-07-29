## Why we use this?
 To get **size of numpy array**.
 
## How to use it?
```
 numpy.array().size
```
 
 ## How it works?
### Output 
``` row * column ```
 
## Examples

### ex1)
 [IN 01]
 ```
 import numpy as np
 
 a = np.array([1,2,3])
 
 print(a.dtype)
 print(a.itemsize)
 print(a.size)
 ```
  [OUT 01]
 ```
int32
4
3
 ```
 ### ex2)
  [IN 02]
 ```
 import numpy as np
 
 a = np.array([1,2,3], dtype='int8')
 
 print(a.dtype)
 print(a.itemsize)
 print(a.size)
 ```
  [OUT 02]
 ```
int8
1
3
 ```
 ### ex3)
 [IN 03]
 ```
 import numpy as np
 
 a = np.array([[1.1,3.14,7.6],[3.4,5.6,7.3]])
 
 print(a.dtype)
 print(a.itemsize)
 print(a.size)
 ```
  [OUT 03]
 ```
float64
8
6
 ```

