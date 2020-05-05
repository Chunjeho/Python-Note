## Why we use this?
To get row or column a littke bit fancy.

## How does it works?
Use ``` [row, start:end:step] ```, if you want certain elements in its row.

Or use ``` [start:end:step, column] ```, if you want certain elements in its column.

**Range is start(start index) <= x < end(end index)**
## Examples
### ex1)
[IN 01]
```
import numpy as np

a = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(a[0, 0:5:1])
```
[OUT 01]
```
[1 2 3 4 5]
```

### ex2)
[IN 02]
```
import numpy as np

a = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(a[0, 0:5:2])
```
[OUT 02]
```
[1 3 5]
```


### ex3)
[IN 03]
```
import numpy as np

a = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a[0:4:1, 0])
```
[OUT 03]
```
[1 3 5 7]
```

### ex4)
[IN 04]
```
import numpy as np

a = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a[0:4:2, 0])
```
[OUT 04]
```
[1 5]
```
