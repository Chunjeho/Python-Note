## Why we use this?
 To get **item's size of bytes** in numpy array.
 
## How to use it?
```
 numpy.array().itemsize
```
 
 ## How it works?
 ### Bit and Byte
 ```8 bits``` : ```1 byte```
 
 ```16 bits``` : ```2 bytes```
 
 ```32 bits``` : ```4 bytes```
 
 ```64 bits``` : ```8 bytes```
### Output 
``` size of bytes ```
 
## Examples

### ex1)
 [IN 01]
 ```
 import numpy as np
 
 a = np.array([1,2,3])
 
 print(a.dtype)
 print(a.itemsize)
 ```
  [OUT 01]
 ```
int32
4
 ```
 ### ex2)
  [IN 02]
 ```
 import numpy as np
 
 a = np.array([1,2,3], dtype='int8')
 
 print(a.dtype)
 print(a.itemsize)
 ```
  [OUT 02]
 ```
int8
1
 ```
 ### ex3)
 [IN 03]
 ```
 import numpy as np
 
 a = np.array([1.1,3.14,7.6])
 
 print(a.dtype)
 print(a.itemsize)
 ```
  [OUT 03]
 ```
float64
8
 ```

