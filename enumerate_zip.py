"""
Compare values from three lists using zip() and enumerate().

For each iteration, print the tuple and identify its largest
and smallest values.
"""

first = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
second = [100, -100, 10, -10, 1, -1, 0.1, -0.1, 0.01, -0.01]
third = [5, 4, 3, 2, 1, 0, 0, 1, 2, 3]

for iteration, (a, b, c) in enumerate(zip(first, second, third), start=1):
    values = (a, b, c)
    print(values)
    print(f"Iteration {iteration}: largest = {max(values)}")
    print(f"Iteration {iteration}: smallest = {min(values)}")
