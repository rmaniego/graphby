# graphby
Generate simple visualizations on terminal.

## Import
**graphby** can now be used on your Python projects through PyPi by running pip command on a Python-ready environment.
`pip import --upgrade graphby`

## Usage
**1. Import package**
```python
from graphby import Bar
```

**2. Basic usage**
```python
from graphby import Bar

labels = ["a", "b", "c", "d"]
values = [200, 350, 20, 999]
Bar(labels, values).plot()
---

a: *          200
b: **         350
c:            20
d: ******     999
```

**3. Change bar character**
```python
from graphby import Bar

labels = ["a", "b", "c", "d"]
values = [200, 350, 20, 999]
Bar(labels, values, bar="+").plot()
```
