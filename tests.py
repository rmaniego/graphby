from graphby import Bar

print("\n1. Basic usage")
labels = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
Bar(labels, values).plot()

print("\n2. Negative numbers")
labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values).plot()

print("\n3. Custom symbol")
labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values, bar="+").plot()

print("\n4. Expand bar graph")
labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values, limit=15).plot()

print("\n5. Customizations")
labels = ["a", "b", "c", "d"]
values = [200, -350, 20, 999]
Bar(labels, values, bar="#", limit=5).plot()