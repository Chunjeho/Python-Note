## Why we use this?
 To get **total byte size of numpy array**.
 
## How to use it?
```
 numpy.array().nbytes
```
 
 ## How it works?
### Output 
``` itemsize * size```
 
## Examples

### ex1)
 [IN 01]
 ```
 import numpy as np
 
 a = np.array([1,2,3])
 
 print(a.dtype)
 print(a.itemsize)
 print(a.size)
 print(a.nbytes)
 ```
  [OUT 01]
 ```
int32
4
3
12
 ```
 ### ex2)
  [IN 02]
 ```
 import numpy as np
 
 a = np.array([1,2,3], dtype='int8')
 
 print(a.dtype)
 print(a.itemsize)
 print(a.size)
 print(a.nbytes)
 ```
  [OUT 02]
 ```
int8
1
3
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
 print(a.nbytes)
 ```
  [OUT 03]
 ```
float64
8
6
48
 ```

