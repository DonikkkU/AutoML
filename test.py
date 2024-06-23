def summa_n():
    N = int(input("Введите число: "))
    
    # Вычисление суммы чисел от 1 до N
    total_sum = sum(range(1, N + 1))
    
    # Вывод результата
    print(f"Я знаю, что сумма чисел от 1 до {N} равна {total_sum}")

# Вызов функции для проверки
# summa_n()

def input_num(num:int) -> int:
    num = int(input())
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        print('zero')
    def positive(num:int) -> int:
        print('positive')
    
    def negative(num:int) -> int:
        print('negative')

def calculator(num1:int, num2:int, target:str):
    num1 = input('введите число')
    num2 = input('введите число')
    target = input(' действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру:')
    if target == 'сумма':
        summ()
    elif target == 'минимальную цифру':
        min_num()
    else:
        max_num()

    def min_num(num1, num2):
        print(min(num1, num2))

    def max_num(num1, num2):
        print(max(num1, num2))  
    def summ(num1, num2):
        sum(num1, num2)

calculator(12, 25)