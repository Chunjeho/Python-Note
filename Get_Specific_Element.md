## How to get specific element in numpy array?
Use 
```[row, column]```

**Row**: 
![Row](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Matrix_Rows.svg/1024px-Matrix_Rows.svg.png)

**Column**:
![Column](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Matrix_Columns.svg/1024px-Matrix_Columns.svg.png)

*Index in python always starts with 0. You need to count 0,1,2,3...; not 1,2,3,4...
## How it works?

If you write ``` a = np.array([[1,2,3],[4,5,6]]) ``` then, 2x3 matrix is created.
```
   0 1 2
0 [1,2,3]
1 [4,5,6]
```

[IN]: ``` print(a[0,0]) ```

[OUT]: ``` 1 ```

[IN]: ``` print(a[0,1]) ```

[OUT]: ``` 2 ```

[IN]: ``` print(a[0,2]) ```

[OUT]: ``` 3 ```

[IN]: ``` print(a[1,0]) ```

[OUT]: ``` 4 ```

[IN]: ``` print(a[1,1]) ```

[OUT]: ``` 5 ```

[IN]: ``` print(a[1,2]) ```

[OUT]: ``` 6 ```

## Examples

### ex1)
[IN 01]
```
import numpy as np

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a[0,0])
```
[OUT 01]
```
1
```

### ex2)
[IN 02]
```
import numpy as np

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a[1,4])
```
[OUT 02]
```
10
```
