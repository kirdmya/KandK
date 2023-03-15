from random import shuffle

def return_number():
    numbers = list(map(str, range(0, 10)))
    shuffle(numbers)
    return "".join(numbers[0:3])


def begin():
    priv = input('Введите имя')
    print('Привет', priv, 'Вы попали на игру "Угадай число". Вам необходимо угадать трехзначное число.')
    print('Компьютер загадал')
    number = input()




if __name__ == "__main__":
    begin()
