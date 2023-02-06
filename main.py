# БЛОК 1 нарисовать поле
# БЛОК 2 Опрос пользователей (расстановка символов): по очереди ставим крестики/нолики в течение 9 ходов.
# БЛОК 3 Кто выиграл? (Ничья или определение победителя)
# БЛОК 4 Обеспечение взаимодествия всех трёх блоков

if __name__ == '__main__':
    field = [['-']*3 for _ in range(3)]


    def show_playground(f):
        num = '  a b c'
        print(num)
        for row, i in zip(field, num.split()):
            print(f'{i} {" ".join(str(j) for j in row)}')


    show_playground(field)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
