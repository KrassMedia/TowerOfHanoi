"""Ханойские башни
Головоломка с перемещением дисков."""

from copy import copy
import sys
import os


TOTAL_DISK = 5  # Кол-во дисков в игре

SOLVED_TOWER = list(range(TOTAL_DISK, 0, -1))  # Создаём список - пример собранной башни


def get_player_move(towers):
    """Запрашиваем ход пользователя, возвращаем имена башен, откуда и куда перекладывать диск"""
    while True:
        print('Введите буквы башен для переноса диска.')
        print('Пример: AB - Переносит диск с башни A на B.')

        response = input('> ').upper().strip()

        if response == 'QUIT':
            sys.exit()

        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Введите одно из AB, AC, BA, BC, CA или CB')
            continue

        from_tower, to_tower = response[0], response[1]

        if not len(towers[from_tower]):  # Выбрана пустая башня для забора диска
            print('Нельзя переложить диски из пустой башни!')
            continue
        elif not len(towers[to_tower]):  # Выбрана пустая башня для укладки диска
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:  # Большой диск кладётся на малый
            print('Нельзя перекладывать большие диски на маленькие!')
            continue
        else:  # Любой иной, допустимый ход
            return from_tower, to_tower


def display_disk(width):
    """Выводим диск нужной ширины, 0 = отсутствие диска"""

    empty_spase = ' ' * (TOTAL_DISK - width)

    if not width:
        print(f'{empty_spase}||{empty_spase}', end='')
    else:
        disk = '#' * width
        num_label = str(width).rjust(2, '_')
        print(f'{empty_spase}{disk}{num_label}{disk}{empty_spase}', end='')


def display_towers(towers):
    """Выводим башни с дисками на дисплей"""

    for level in range(TOTAL_DISK, -1, -1):  # Перебираем уровни башен
        for tower in (towers['A'], towers['B'], towers['C']):  # Перебираем башни
            if level >= len(tower):  # Если диски в башне на текущем уровне отсутствуют
                display_disk(0)  # Выводим пустой стержень
            else:  # Если диск в башне, на текущем уровне присутствует
                display_disk(tower[level])  # Выводим имеющийся на текущем уровне диск
        print()

    empty_spase = ' ' * TOTAL_DISK
    print(f'{empty_spase} A{empty_spase * 2} B{empty_spase * 2} C')


def main():
    towers = {'A': copy(SOLVED_TOWER), 'B': [], 'C': []}

    while True:  # Основной цикл
        # Выводим правила игры
        print('''Правила игры:
    Задача состоит в том, чтобы перенести пирамиду
    из колец за наименьшее число ходов на другой стержень.
    За один раз разрешается переносить только одно кольцо,
    причём нельзя класть большее кольцо на меньшее.\n''')

        # Выводим башни на дисплей
        display_towers(towers)

        # Запрашиваем ход игрока
        from_tower, to_tower = get_player_move(towers)

        # Перемещаем диск
        towers[to_tower].append(towers[from_tower].pop())

        # Проверяем, решена ли головоломка
        if SOLVED_TOWER in (towers['B'], towers['C']):
            display_towers(towers)  # Выводим башни на дисплей
            input('''Поздравляю, Вы прошли головоломку!
            Для продолжения нажмите любую клавишу...''')
            sys.exit()

        # Отчищаем экран перед выводом нового этапа игры
        os.system('cls||clear')


if __name__ == '__main__':
    main()
