
#Создание поля игры
def show():
    print("  0 1 2 ")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
    print()

#спрашиваем координаты
def coordinates():
    while True:
        x, y = map(int,input("Ваш ход: ").split())
        if 0<=x<=2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Клетка занята")
        else:
            print("Нет таких координат")

# проверка выйграшных комбинаций
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False


# игровой цикл
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = coordinates()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break