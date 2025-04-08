def log_arg_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def calculate_area(length, width):
    return length * width
calculate_area = log_arg_decorator(calculate_area)
area = calculate_area(5, 10)
print(f"Площадь прямоугольника: {area}")
