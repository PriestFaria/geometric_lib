# Perimeter and area formulae
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions
## Circle (circle.py)
### Description
```
import math

def area(r):
    '''Gets circle radius r and returns its area'''
    return math.pi * r * r

def perimeter(r):
    '''Gets circle radius r and returns its perimeter'''
    return 2 * math.pi * r
```
### Inputs and outputs
- area(5)
    - 78.53981633974483
- perimeter(5)
    - 31.41592653589793
## Rectangle (rectangle.py)
### Description
```
def area(a, b):
    '''Gets rectangle sides a, b and returns its area'''
    return a * b

def perimeter(a, b):
    '''Gets rectangle sides a, b and returns its perimeter'''
    return 2 * (a + b)
```
### Inputs and outputs
- area(5, 7)
    - 35
- perimeter(5, 7)
    - 24
## Square (square.py)
### Description
```
def area(a):
    '''Gets square side a and returns its area'''
    return a * a

def perimeter(a):
    '''Gets square side a and returns its perimeter'''
    return 4 * a
```
### Inputs and outputs
- area(5)
    - 25
- perimeter(5)
    - 20
## Triangle (triangle.py)
### Description
```
def area(a, h):
    '''Gets triangle side a и его высоту h and returns its area'''
    return a * h / 2

def perimeter(a, b, c):
    '''Gets triangle sides a, b, c and returns its perimeter'''
    return a + b + c
```
### Inputs and outputs
- area(5, 7)
    - 17.5
- perimeter(5, 7, 9)
    - 21

# Project history
```
* commit 9bba44c7e8f0aaa5cb22be4a0cd07940dd25ad58 (HEAD -> main, Learning_git/new_features_409317)
| Author: Пашкеев Кирилл <409317@niuitmo.ru>
| Date:   Thu Sep 21 18:46:14 2023 +0300
| 
|     Added triangle.py and fixed rectangle.py
| 
* commit 873aad601aebfe396ab9b6e0c9951d1cef4434e5
| Author: Пашкеев Кирилл <409317@niuitmo.ru>
| Date:   Thu Sep 21 18:36:49 2023 +0300
| 
|     Added rectangle.py
| 
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
| Author: smartiqa <info@smartiqa.ru>
| Date:   Thu Mar 4 14:55:29 2021 +0300
| 
|     L-03: Docs added
| 
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300
```
