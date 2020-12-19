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
values = [1, 2, 3, 4]
Bar(labels, values).plot()
---

a: **         1
b: *****      2
c: ********   3
d: ********** 4
```

**3. Negative numbers**
```python
from graphby import Bar

labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values).plot()
---

a: ****        200
b:            -350
c: ***          20
d: **********  999
```

**4. Custom symbol**
```python
from graphby import Bar

labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values, bar="+").plot()
---

a: ++++        200
b:            -350
c: +++          20
d: ++++++++++  999
```


**5. Expand graph**
```python
from graphby import Bar

labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values, limit=15).plot()
---

a: ******           200
b:                 -350
c: ****              20
d: ***************  999
```


**6. Customizations**
```python
from graphby import Bar

labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values, bar="#", limit=5).plot()
---

a: ##     200
b:       -350
c: #       20
d: #####  999
```

