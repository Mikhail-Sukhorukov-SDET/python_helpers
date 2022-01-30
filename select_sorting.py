from utils import random_list
from sorting import select_sorting


random_values = random_list()
print(random_values)
sorted_values = select_sorting(random_values)
print(sorted_values)

assert set(random_values) == set(sorted_values)

