# БЛОК 1 нарисовать поле
# БЛОК 2 Опрос пользователей (расстановка символов): по очереди ставим крестики/нолики в течение 9 ходов.
# БЛОК 3 Кто выиграл? (Ничья или определение победителя)
# БЛОК 4 Обеспечение взаимодествия всех трёх блоков

def show_playground(f):
    col_names ='  1 2 3'
    print(col_names)
    for row, i in zip(field, col_names.split()):
        print(f'{i} {" ".join(str(j) for j in row)}')

def user_input(f):
   
    while True:
        # пользователь должен ввести обязательно два числа без пробела
        coords = input('Введите координаты вашего хода в формате xy:  ')
                
        # проверка элементов - два? 
        if len(coords) != 2:
            print("Введите две координаты...")
            continue
       
        # проверка элементов строки - это числа?
        elif not(coords[0].isdigit() and coords[1].isdigit()):
            print("Введите числа...")
            continue
           
        # перевод строчных значений в численные
        # используем map для применения функции int для каждого элемента списка
    
        x,y = map(int, coords)
        
        if not((x >= 1 and x < 4) and (y >= 1 and y < 4)):
            print("Вы вышли из диапазона сетки. Введите числа от 0 до 2...")
            continue
        
        
        # проверка, что ячейка в поле f (переданный аргумент при вызове функции) не занята
        if f[x-1][y-1] != '-':
            print("Ячейка занята, попробуйте другие координаты...")
            continue
        break
    return x-1,y-1

def win_combo(f, user):
    f_list=[]
    print(f)
    
    for l in f:
        f_list+=l
    
    print(f_list)
    positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indexes = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indexes.intersection(set(p)))==3:
            return True
    return False

# TODO: спросить имена пользователей
#       спросить как они выберут, чем играть: сами договорятся или рандомно назначить игроку его символ
#       реализовать работу с возвращаемыми значениями в lets_play()
# def hello():
#     # count = 0 
#     user1 = input("Имя?...")
#     symbol1 = input("Какй символ выбираете?...")

#     user2 = input("Имя?...")
#     symbol2 = input("Какй символ выбираете?...")

#     player1 = {"name" : user1, "symbol": symbol1}
#     player2 = {"name" : user2, "symbol": symbol2}
    
#     print(player1,player2,end='\n')

#     return ....

#создание списка тирешек, выступающих в роли поля
field = [['-']*3 for _ in range(3)] 

def lets_play(field):

    # создаем переменную счётчик для отслеживания очередности хода игрока
    # и проверки окончания игры
    count = 0 
   
    while True:
    
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        show_playground(field)
        x,y = user_input(field)
        field[x][y] = user

        if count == 9:
            print("Игра окончена - ничья")
        
        if win_combo(field, user):
            show_playground(field)
            print(f"Пользователь {user} выиграл")
            break

        count += 1

lets_play(field)