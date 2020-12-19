"""
    (c) 2020 Rodney Maniego Jr.
    graphby
"""
import sys

class Bar:
    def __init__(self, categories, values, bar=None):
        """
            Read and prepare the JSON/Dictionary object.
            ...
            Parameters
            ---
            categories: list
                any list of string to label each corresponding values
            values: list
                any list numeric values (positive)
            bar: string
                any character to use in the bar graph for each increment
        """
        self.categories = categories
        self.limit = 10
        self.values = values
        self.normalized = normalize(self.values, self.limit)
        if len(self.categories) != len(self.values):
            print("Labels and values doesn't match in size.")
            sys.exit(0)
        self.bar = bar
        if self.bar == None or len(bar) != 1:
            self.bar = "*"

    def plot(self):
        fvalues = []
        for value in self.values:
            fvalues.append(str(value))
        max_numbers = longest(fvalues)
        max_letters = longest(self.categories)
        for label, reduced, value in zip(self.categories, self.normalized, fvalues):
            # padd labels
            limit = max_letters - len(label)
            for count in range(0, limit):
                label = f"{label} "
            # increment bars
            bar = ""
            for count in range(0, reduced):
                bar = f"{bar}{self.bar}"
            limit = self.limit - len(bar)
            for count in range(0, limit):
                bar = f"{bar} "
            # pad values
            limit = max_numbers - len(value)
            for count in range(0, limit):
                value = f" {value}"
            print(f"{label}: {bar} {value}")
            

def normalize(values, limit=10):
    rates = []
    limit = get_int(limit)
    if limit <= 0: limit = 10
    max = maximum(values)
    min = minimum(values)
    if min < 0:
        add = abs((0 - min))
        max += add
    for num in values:
        num = get_float(num)
        if min < 0:
            num += add
        rate = (num / max) * 100
        rates.append(rate)
    # normalize
    normalized = []
    sum_of_rates = maximum(rates)
    for rate in rates:
        num = round((rate / sum_of_rates) * limit)
        normalized.append(num)
    return normalized

def longest(strings):
    length = 0
    for word in strings:
        temp = len(str(word))
        if length < temp:
            length = temp
    return length
    
def maximum(numbers):
    temp = 0
    try:
        for num in numbers:
            num = get_float(num)
            if temp == 0: temp = num
            if temp < num: temp = num
    except:
        pass
    return temp

def minimum(numbers):
    temp = 0
    try:
        for num in numbers:
            num = get_float(num)
            if temp == 0: temp = num
            if temp > num: temp = num
    except:
        pass
    return temp

def get_int(string):
    try:
        return int(string)
    except:
        return 0

def get_float(string):
    try:
        return float(string)
    except:
        return 0