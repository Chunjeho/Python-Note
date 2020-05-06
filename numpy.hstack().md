## Why we use this?
To **stack numpy arrays horizontally**.

## How to use it?
Use ``` numpy.hstack([numpy.array(), numpy.array()]) ```

## Example
### ex1)
[IN 01]
```
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.hstack([v1, v2]))
```
[OUT 01]
```
[1 2 3 4 5 6 7 8]
```
