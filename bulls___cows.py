import random

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: David Cudejko
email: david.cudejko@gmail.com
discord: #3576
"""

#Computer secret numbers

def creating_4_secret_number() -> int:
    '''
    Popis:
    Vygenerovani tajneho 4- mistniho cisla, ktere bude uzivatel hadat
    
    Priklad:
    5761
    
    Vysledek:
    [5,7,6,1]
    '''
    x = list(range(1,10))
    random.shuffle(x)
    return (x[:4])


#User choice numbers and conditions

def user_number_choice() -> str: 
    '''
    Popis:
    Vygenerovani 4-mistniho cisla uzivatelem a osetreni podminek.
    Cislo musi byt 4 mis. cislo,nesmi obsahovat 0 a byt duplicitni.
    
    Priklad:
    5314
    
    Vysledek:
    '5','3','1','4'
    '''
    while True:
        user_number = input( 'Enter a number: ')

        if len(user_number) != 4:
            print('Attention, you must enter a 4-digit number')
        elif (user_number).startswith('0'):
            print('Attention, number can\'t starts with 0 ')
        elif user_number.isdigit() != True:
            print('Attention, you must enter only number')
        elif len(user_number) > len(set(user_number)):
            print('Attention, you cant enter duplicate numbers')
        else:
            return user_number
        

# bull/bulls and cow/cows

def bulls_cows(user_n, secret_n) -> None:
    '''
    Popis:
    Vypise se pocet bull/bulls (pokud uzivatel uhodne jak cislo, tak umisteni) 
    prip. cows/cows (pokud uzivatel uhodne pouze cislo, ale ne jeho umisteni). 
    Vracene hodnoceni bere ohled na jednotne a mnozne cislo ve vystupu 
    
    Priklad:
    6328 -tajne cislo
    6382 - cislo uzivatele
    
    Vysledek:
    you have 2 bulls
    you have 2 cows
    '''
    bulls = 0
    cows = 0
    
    for i, x in zip(user_n, secret_n):
        if x in user_n:
            if x == i:
                bulls +=1
    if bulls == 1:
        print(f'you have  {bulls} bull')
    else:
        print(f'you have  {bulls} bulls')

    for i, x in zip(user_n, secret_n):
        if x in user_n:
            if x != i:
                cows +=1
    if cows == 1:
                print(f'you have {cows} cown')
    else:
                print(f'you have {cows} cows')

# Main game
def main_game() -> None:
    '''
    Popis:
    Provadi finalni hru, vypis a nastavuje pocet pokusu uzivatele na 8.
    
    Priklad:
    6328 -tajne cislo
    6382 - cislo uzivatele
    
    Vysledek:
    --- Guess: 8---
    Enter a number: 6382
    you have 2 bulls
    you have 2 cows 
    '''
    
    line = '-' * 47
    print('Hi there!', line, 
        'I\'ve generated a random 4 digit number for you.',
        'Let\'s play a bulls and cows game.', line, sep='\n')
    tries = 9
    secret_number = list(creating_4_secret_number())

    while tries > 1 :
        
        tries -= 1
        print("--- Guess: " + str(tries) + "---")
        user_number = (list(map(int,user_number_choice())))
        bulls_cows(user_number,secret_number)
        if user_number  == secret_number:
            print('---YOU WIN!---')
            quit()
        
    else:
        print(f'---you have no more attempts. You lost. GAME OVER---')
        



if __name__ == '__main__':
    main_game()






