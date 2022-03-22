print('Задание 1')

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print('Задание 2-3')

input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length_of_list:int = len(input_list)
store_id = id(input_list)

for i in input_list:

    elem = input_list.pop(0)

    if elem.isdigit():
        input_list.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        input_list.append(f'"+{int(elem):02d}"')
    else:
        input_list.append(elem)

print(' '.join(input_list))

print('Задание 4')

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй','директор аэлита']
answer = {}

for string in my_list:
    correct_name = string.split()[-1].capitalize()
    print(f"Привет, {correct_name}!")

print('Задание 5')

list = [57.8, 46.51, 97, 76.05, 13.11, 87.93, 27, 97.09, 0.16, 42,96.64, 34.17, 97.45, 40.62, 84.94, 7, 52.23, 93.74, 89, 3.93]

store_id = id(list)

end_word:str = ", "

for i, num in enumerate(list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

print(f"{'':-^100}")

list.sort()
print(list)

print(f"{'':-^100}")

copy_of_list = list.copy()
copy_of_list.sort(reverse=True)

print(copy_of_list)

print(f"{'':-^100}")

print("ТОП 5 САМЫХ ДОРОГИХ ТОВАРОВ", list[-6:-1])