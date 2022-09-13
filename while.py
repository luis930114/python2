# -*- coding: utf-8 -*-

import random

def run():
    number_fount = False
    random_number = random.randint(0,20)

    while not number_fount:
        number = int(raw_input('Intenta un numero: '))
        print(random_number)

        if number == random_number :
            print('Felicidades. Encontraste el numero')
            number_fount = True
        elif number > random_number :
            print('el numero es mas pequeño')
        else:
            print('el numero es mas grande')

if __name__ == '__main__':
    run()
