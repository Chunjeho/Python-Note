## Why we use this?
To **load externel file into numpy format**.

## How to use it?
Use ``` numpy.genfromtxt('filename', delimiter='something') ```

* ``` delimiter ```: can be anything, but it must distinguish each number.
  
  ex) In ``` 1,2,3,4,5 ```,  ``` delimiter=',' ```.
  
  ex) In ``` 1|2|3|4|5 ```,  ``` delimiter='|' ```.
  
## Example
### ex1)
Before coding, make *test.txt* file and make number array.
I wrote like this way.

1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
16,17,18,19,20
21,22,23,24,25
26,27,28,29,30

[IN 01]
```
import numpy as np

filedata = np.genfromtxt('test.txt', delimiter = ',')
print(filedata)
print(filedata[0, 1]
```
[OUT 01]
```
[[ 1.  2.  3.  4.  5.]
 [ 6.  7.  8.  9. 10.]
 [11. 12. 13. 14. 15.]
 [16. 17. 18. 19. 20.]
 [21. 22. 23. 24. 25.]
 [26. 27. 28. 29. 30.]]
 2.0
```
