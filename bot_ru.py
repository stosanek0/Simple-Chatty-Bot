def greet(bot_name, birth_year):
    print('Привет, меня зовут ' + bot_name + '.')
    print('Я был создан в ' + birth_year + '.')


def remind_name():
    print('Пожалуйста, напомни мне свое имя.')
    name = input()
    print('Какое у тебя отличное имя, ' + name + '!')


def guess_age():
    print('Дай угадать твой возраст.')
    print('Введите остаток от деления вашего возраста на 3, 5 и 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Ваш возраст " + str(age) + "; это хорошее время, чтобы начать программировать!")


def count():
    print('Теперь я докажу вам, что могу считать до любого числа, которое вы хотите.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Давайте проверим ваши знания в области программирования.")
    print("Почему мы используем функцию?")
    print("1. Повторить высказывание несколько раз.")
    print("2. Разложить программу на несколько небольших подпрограмм.")
    print("3. Определить время выполнения программы.")
    print("4. Прервать выполнение программы.")
    otvet = int(input())
    while otvet != 0 and otvet < 5:
        if otvet in(1, 3, 4):
          print("Пожалуйста, попробуйте еще раз.")
          otvet = int(input())
        else:
          print('Completed, have a nice day!')
          break


def end():
    print('Готово, хорошего дня!')


greet('БотАник.', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
