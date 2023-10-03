# Формулы периметра и площади фигур
## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = ah / 2

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c

# Функции
## Круг (circle.py)
### Описание функции
```
import math

def area(r):
    '''Принимает радиус круга r, возвращает его площадь'''
    return math.pi * r * r

def perimeter(r):
    '''Принимает радиус круга r, возвращает длину его окружности'''
    return 2 * math.pi * r
```
### Входные и выходные данные
- area(5)
    - 78.53981633974483
- perimeter(5)
    - 31.41592653589793
## Прямоугольник (rectangle.py)
### Описание функции
```
def area(a, b):
    '''Принимает стороны прямоугольника a и b, возвращает его площадь'''
    return a * b

def perimeter(a, b):
    '''Принимает стороны прямоугольника a и b, возвращает его периметр'''
    return 2 * (a + b)
```
### Входные и выходные данные
- area(5, 7)
    - 35
- perimeter(5, 7)
    - 24
## Квадрат (square.py)
### Описание функции
```
def area(a):
    '''Принимает сторону квадрата a, возвращает его площадь'''
    return a * a

def perimeter(a):
    '''Принимает сторону квадрата a, возвращает его периметр'''
    return 4 * a
```
### Входные и выходные данные
- area(5)
    - 25
- perimeter(5)
    - 20
## Треугольник (triangle.py)
### Описание функции
```
def area(a, h):
    '''Принимает сторону треугольника a и его высоту h, возвращает его площадь'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает стороны треугольника a, b, c, возвращает его периметр'''
    return a + b + c
```
### Входные и выходные данные
- area(5, 7)
    - 17.5
- perimeter(5, 7, 9)
    - 21

# История проекта
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
