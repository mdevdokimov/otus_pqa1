"""считаем среднее"""

def calculate_average(nums):
    """функция считает среднее число."""
    return sum(nums)/len(nums)

my_nums = [10, 15, 20]
result = calculate_average(my_nums)
print("The average is:", result)
