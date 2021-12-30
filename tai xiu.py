import random
import math

print('+------------------------+---------------------------------------------------------+')
print('|                        |                                                         |')
print('|                        |                       FOR EDUCATIONAL ONLY - DEBUG: NO  |')
print('|                        |                                                         |')
print('|                        |                                                         |')
print('|                        |                                                         |')
print('|                        |                                                         |')
print('|                        |                  Tai Siu Python                         |')
print('|  TTTTTTTTT    sssssss  |                  Version: 1.0 (Beta 1)                  |')
print('|      T       ss        |                  All right reversed!                    |')
print('|      T       ss        |                                                         |')
print('|      T        sssssss  |                                                         |')
print('|      T      s       ss |                                                         |')
print('|      T      s       ss |                                                         |')
print('|      T      sssssssss  | LUU Y: Project danh cho muc dich hoc tap!               |')
print('|                        |        Vui long khong su dung code vao muc dich vi pham |')
print('|                        |        phap luat hay su dung vao game co bac online!    |')
print('|                        |                                                         |')
print('|                        |        Chung toi khong chiu trach nhiem ve cac hanh vi  |')
print('|                        |        vi pham phap luat cua cac ca nhan hay to chuc su |')
print('|                        |        dung trai phep ma nguon mo nay!                  |')
print('+------------------------+---------------------------------------------------------+')

question = input('Chao mung den voi game Tai siu :)) Co muon choi khong?[Co/Khong]:')

while question != 'Khong' or 'KHONG' or 'KO' or 'Ko' or 'ko' or'kO' or'K':
    if question == 'Co' or 'cO' or 'CO' or 'C':
        
        #OLD SYSTEM
        
        #die1 = random.randint(1, 6)
        #die2 = random.randint(1, 6)
        #die3 = random.randint(1, 6)
        #TX = die1 + die2 + die3

        #CURRENT SYSTEM

        #DICE RENDER PATH
        
        dice = ['one', 'two', 'three', 'four', 'five', 'six']

        
        
        def six():
            print('X X X X X X X')
            print('X           X')
            print('X 6   6   6 X')
            print('X           X')
            print('X 6   6   6 X')
            print('X           X')
            print('X 6   6   6 X')
            print('X           X')
            print('X X X X X X X')

        def five():
            print('X X X X X X X')
            print('X           X')
            print('X 5       5 X')
            print('X           X')
            print('X     5     X')
            print('X           X')
            print('X 5       5 X')
            print('X           X')
            print('X X X X X X X')

        def four():
            print('X X X X X X X')
            print('X           X')
            print('X 4       4 X')
            print('X           X')
            print('X           X')
            print('X           X')
            print('X 4       4 X')
            print('X           X')
            print('X X X X X X X')
    
        def three():
            print('X X X X X X X')
            print('X           X')
            print('X 3         X')
            print('X           X')
            print('X     3     X')
            print('X           X')
            print('X         3 X')
            print('X           X')
            print('X X X X X X X')

        def two():
            print('X X X X X X X')
            print('X           X')
            print('X           X')
            print('X           X')
            print('X 2       2 X')
            print('X           X')
            print('X           X')
            print('X           X')
            print('X X X X X X X')

        def one():
            print('X X X X X X X')
            print('X           X')
            print('X           X')
            print('X           X')
            print('X     1     X')
            print('X           X')
            print('X           X')
            print('X           X')
            print('X X X X X X X')

        #RANDOM SYSTEM
            
        dice1 = random.choice(dice)
        dice2 = random.choice(dice)
        dice3 = random.choice(dice)

        #IF ELSE RENDERING DICE + NUMBER 

        #DICE 1
        if dice1 == 'six':
            N = 6
            six()
            print()
        elif dice1 == 'five':
            N = 5
            five()
            print()
        elif dice1 == 'four':
            N = 4
            four()
            print()
        elif dice1 == 'three':
            N = 3
            three()
            print()
        elif dice1 == 'two':
            N = 2 
            two()
            print()
        else:
            N = 1
            one()
            print()

        #DICE 2    
        if dice2 == 'six':
            N1 = 6
            six()
            print()
        elif dice2 == 'five':
            N1 = 5
            five()
            print()
        elif dice2 == 'four':
            N1 = 4
            four()
            print()
        elif dice2 == 'three':
            N1 = 3
            three()
            print()
        elif dice2 == 'two':
            N1 = 2
            two()
            print()
        else:
            N1 = 1
            one()
            print()

        #DICE 3
        if dice3 == 'six':
            N2 = 6
            six()
            print()
        elif dice3 == 'five':
            N2 = 5
            five()
            print()
        elif dice3 == 'four':
            N2 = 4
            four()
            print()
        elif dice3 == 'three':
            N2 = 3
            three()
            print()
        elif dice3 == 'two':
            N2 = 2
            two()
            print()
        else:
            N2 = 1
            one()
            print()

        #CALCULATING TAI SIU    
        TX = N + N1 + N2
        if 4 <= TX <= 10:
            print('KET QUA:')
            print('Siu!')
            print()
        elif 11<= TX <= 17:
            print('KET QUA:')
            print('Tai!')
            print()
        else:
            print('Drop!')
            print()

        #QUESTION
        question = input('Co muon choi tiep khong?[Co/khong]:')
    else:
        print('Tra loi ngu! Noi lai!')
        question = input('Co muon choi khong?[Co/Khong]:')        

print('Tam biet :))!')
