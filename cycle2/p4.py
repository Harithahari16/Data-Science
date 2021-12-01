import numpy as np

a = np.arange(1, 11, 1)
print(a)
first_element = a[:4]
print("first 4 elements:")
print(first_element)
last_element = a[5:]
print("last 6 elements:")
print(last_element)
element = a[1:7]
print("elements from index 2 to 7:")
print(element)