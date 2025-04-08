squared_numbers = [number * number for number in range(1, 11)]
print("1.", squared_numbers)
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekday_numbers = {weekdays[i]: i + 1 for i in range(len(weekdays))}
print("2.", weekday_numbers)

usxod_tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lowercase_usxod_tags = {tag.lower() for tag in usxod_tags}
print("3.", lowercase_usxod_tags)

orig_numbers = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [number for number in orig_numbers if number % 2 == 0]
print("4.", even_numbers)

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

factorial_num = {i: factorial(i) for i in range(1, 6)}
print("5.", factorial_num)


