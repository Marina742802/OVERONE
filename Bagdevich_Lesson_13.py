#1. Напишите функцию, которая принимает на вход два аргумента и возвращает их сумму.
def fun_sum(a, b):
    return a + b

#2. Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение.
inp_lst = [1, 5, 6, 3, 8]
sum_lst = sum(inp_lst)
lst_avg = sum_lst/len(inp_lst)
print(lst_avg)

#3. Напишите функцию, которая принимает на вход число и возвращает True,
# если оно четное, и False, если оно нечетное.
def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n = int(input("Введите число:"))
if (check(n) == True):
      print(True)
else:
      print(False)


#4. Напишите функцию, которая принимает на вход список и возвращает новый список,
# содержащий только уникальные элементы из исходного списка.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([8,2,3,3,6,3,4,5,5]))


#5. Решите задачу с использованием вложенной функции is_square.
# Предположим, у нас есть список чисел и мы хотим найти все числа,
# которые являются квадратами других чисел в этом списке.
# Шаблон кода (ориентировачный):
# def find_square_numbers(numbers):
#     def is_square(number):
#         return '...'
#
#     return '...'
def find_square_numbers(numbers):
    def is_square(number):
        return numbers * numbers

    return is_square(numbers)

print(find_square_numbers)