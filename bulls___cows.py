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
    

#Main game
def main_game() -> None:
    '''
    Popis:
    Porovnani cisla uzivatele s tajnym cislem. Pocet hadani je 9.
    Porovnavaji se hodnoty - cows a hodnoty+indexy - bulls.
    
    Priklad:
    5761 vs 5314
    
    Vysledek:
    you have  1 bull
    you have 2 cows 
    '''
    line = '-' * 47
    print('Hi there!', line, 
        'I\'ve generated a random 4 digit number for you.',
        'Let\'s play a bulls and cows game.', line, sep='\n')
    tries = 9
    secret_number = list(creating_4_secret_number())
    print(secret_number)
    
    while tries > 1 :
        bulls = 0
        cows = 0
        tries -= 1
        print("--- Guess: " + str(tries) + "---")
        user_number = (list(map(int,user_number_choice())))
        #bull/bulls
        for i in range(len(user_number)):
            
            if user_number[i] == secret_number[i]:
                bulls +=1
        if bulls == 1:
            print(f'you have  {bulls} bull')
        else:
            print(f'you have  {bulls} bulls')
        #cown/cowns
        for i in user_number:
            
            if i in secret_number:
                cows += 1        
        if cows == 1:
            print(f'you have {cows} cown')
        else:
            print(f'you have {cows} cows')
        #user win        
        if user_number  == secret_number:
            print('---YOU WIN!---')
            quit()       
    else:
        print(f'---you have no more attempts. You lost. GAME OVER---')



if __name__ == '__main__':
    main_game()






