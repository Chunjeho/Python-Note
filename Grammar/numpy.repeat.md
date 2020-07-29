## Why we use this?
To make **numpy matrix with repetitive items more fast**.

## How to use?
Use ``` numpy.repeat(numpy.array(), times, axis=*) ```

## How it works?
It depends on ``` axis ``` and given ``` numpy.array() ```.

``` numpy.array().ndim = n```: output **n dimension array**

``` axis=0 ```: repeating each element by vertical direction

``` axis=1 ```: repeating each element by horizontal direction

## Examples 

### ex1)
[IN 01]
```
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.repeat(arr1, 3, axis = 0)

print(arr2.ndim)
print(arr2)
```
[OUT 01]
```
1
[1 1 1 2 2 2 3 3 3]
```
### ex2)
[IN 02]

```
import numpy as np

arr1 = np.array([[1,2,3]])
arr2 = np.repeat(arr1, 3, axis = 0)

print(arr2.ndim)
print(arr2)
```

[OUT 02]

```
2
[[1 2 3]
 [1 2 3]
 [1 2 3]]
```

### ex3)
[IN 03]

```
import numpy as np

arr1 = np.array([[1,2,3]])
arr2 = np.repeat(arr1, 3, axis = 1)

print(arr2.ndim)
print(arr2)
```

[OUT 03]

```
2
[[1 1 1 2 2 2 3 3 3]]
```
