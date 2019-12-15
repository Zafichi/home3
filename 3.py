def foo(num):
    first_num = num
    second_num = num * 2
    third_num = num * 3
    fourth_num = num * 4
    print(first_num, '+', second_num, '-', third_num, '*', fourth_num, end=' = ')
    print(int(first_num) + int(second_num) - int(third_num) * int(fourth_num))


foo(input('Enter the number: '))
