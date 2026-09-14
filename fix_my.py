"""считаем среднее"""

def calculate_average(nums):
    """функция считает среднее число."""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average

my_nums = [10, 15, 20]
result = calculate_average(my_nums)
print("The average is:", result)
