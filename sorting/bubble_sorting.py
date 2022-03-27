from utils.utils import random_list
from sorting import bubble_sorting


random_values = random_list()
print(random_values)
sorted_values = bubble_sorting(random_values)
print(sorted_values)

assert set(random_values) == set(sorted_values)
