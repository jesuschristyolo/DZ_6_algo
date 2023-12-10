
def creating_list():
    first_num, last_num = map(int, input("Введите первое и последнее значение формируемого списка: \n").split())
    return_list = [i for i in range(first_num, last_num + 1)]
    print("Сформированный список:\n", return_list)
    return return_list



def binary_search(enter_list: list, search_num: int):
    mid_value = enter_list[len(enter_list)//2]
    if mid_value == search_num:
        return enter_list.index(mid_value)
    else:
        exit_list = enter_list
        while mid_value != search_num:
            if search_num > mid_value:
                right_list = exit_list[len(exit_list) // 2:]
                mid_value = right_list[len(right_list) // 2]
                exit_list = right_list

            elif search_num < mid_value:
                left_list = exit_list[:len(exit_list) // 2]
                mid_value = left_list[len(left_list) // 2]
                exit_list = left_list

            if mid_value == search_num:
                return f"Индекс вашего числа: {enter_list.index(mid_value)}"
            if len(exit_list) == 1:
                return f"-1(мы не нашли ваше число)"

try:
    sorted_list = creating_list()
except:
    print('нужно было вводить цыферки')

try:
    print(binary_search(sorted_list, int(input("Введите искомое число\n"))))
except ValueError:
    print('Нужно было ввести 1 цифру')



























