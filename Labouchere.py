import os
x = 0
i = 'n'


print('==========\nWelcome!')


geld = int(input('==========\nAmount of money?: '))


while i == 'n':
    menu = int(input('==========\n[1] Start\n[2] Quit\n==========\n'))
    if menu == 1:
        os.system('cls')
        print('==========\nBalance:',geld,)
        winst = int(input('==========\nEstimated Profit?: '))
        doel = input('==========\nList of expense?:')
        sys = list(map(int, doel.split()))
        print('==========\n',sys)
        som = sum(sys)
        som1 = sys[0] + sys[-1]
        som2 = sys[0]
        x = 0
        while x == 0:
            #controleert of de lijst wel juist is ingevoert
            if som != winst:
                doel = input('==========\nList of expense?: ')
                sys = list(map(int, s.split()))
                print(sys)
                som = sum(sys)
            else:
                while 0 != len(sys):
                    if 1 < len(sys):
                        os.system('cls')
                        print('==========\nBalance:',geld,)
                        print('==========\nBet',sys[0] + sys[-1])
                        win = input('==========\nDid you win? y/n: ')
                        if win == 'y':
                            geld = geld + som1
                            del sys[0]
                            del sys[-1]
                        elif win == 'n':
                            geld = geld - (sys[0] + sys[-1])
                            sys.append(sys[0] + sys[-1])
                            print(sys)
                    elif 1 == len(sys):
                        os.system('cls')
                        print('==========\nBet',som2)
                        win = input('==========\nDid you win? y/n: ')
                        if win == 'y':
                            geld = geld + som2
                            del sys[0]
                        elif win == 'n':
                            geld = geld - som2
                            sys.append(sys[0])
                            print(sys)
            if 0 == len(sys):
                os.system('cls')
                print('==========\nBalance:',geld)
                print('==========\nProfit made!')
                x = 1
    elif menu == 2:
        os.system('cls')
        print('==========\nWanna quit? y/n: ')
        i = input()
        if i == 'y':
            input('==========\nPress [Enter] to quit.')
                        
