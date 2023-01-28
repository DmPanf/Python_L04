"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
# Программа "Личный счет"
yes_no = True
user_bank = 0.
user_purchase = {}


def choice_menu():  # menu
    global yes_no
    my_menu = {'1': 'пополнение счета', '2': 'покупка', '3': 'история покупок', '4': 'баланс', '5': 'средний чек', '0': 'выход'}
    print('.' * 21)
    for key, val in my_menu.items():
        print(f'{key}. {val}')
    print('.' * 21)
    to_do = input('Выберите пункт меню: ')
    return yes_no, to_do


def bank_account():  # 1. пополнение счета
    global user_bank
    try:
        new_sum = float(input('Введите сумму для пополнения счета: '))
        if new_sum >= 10:
            user_bank += new_sum
        else:
            print('Сумма должна быть не менее 10 ..\n')
    except:
        print('Ошибка ввода суммы!')


def make_purchase():  # 2. покупка
    global user_bank
    global user_purchase
    try:
        purchase_sum = float(input('Ввведите сумму покупки: '))
        if purchase_sum < 10:
            print('Стоимость покупки не может быть менее 10 ..')
        elif purchase_sum <= user_bank:
            user_bank -= purchase_sum
            purchase = input('Введите название покупки: ')
            user_purchase[purchase] = purchase_sum
        else:
            print('Денег не хватает!')
    except:
        print('Ошибка ввода суммы!')


def user_histroy():  # 3. история покупок
    if len(user_purchase) > 0:
        for key, val in user_purchase.items():
            print(f' - Стоимость {key} = {val}')
        print('Сделано покупок: ', len(user_purchase))
        average_check()
        bank_balance()
        print()
    else:
        print('Еще не было покупок!')


def bank_balance():  # 4. баланс
    print('💰 Остаток на счету:', user_bank)


def average_check():  # 5. средний чек
    if len(user_purchase) > 0:
        print('🛒🛒🛒📝📝📝📝Средний чек = ', round(sum(user_purchase.values()) / len(user_purchase), 1))
    else:
        print('Еще не было покупок!')


while yes_no:
    yes_no, choice = choice_menu()
    if choice == '1':
        bank_account()
    elif choice == '2':
        make_purchase()
    elif choice == '3':
        user_histroy()
    elif choice == '4':
        bank_balance()
    elif choice == '5':
        average_check()
    elif choice == '0':
        yes_no = False
    else:
        print('Неверный пункт меню\n')
