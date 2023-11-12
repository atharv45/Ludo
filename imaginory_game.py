'''
Atharv phadale - Data scientist
'''


import random

xlist = [0]
zlist = [0]

def display():
    zero = 'A' if xstate[0] else '00'
    one = 'A' if xstate[1] else '01'
    two = 'A' if xstate[2] else '02'
    three = 'A' if xstate[3] else '03'
    four = 'A' if xstate[4] else 'sf'
    five = 'A' if xstate[5] else '05'
    six = 'A' if xstate[6] else '06'
    seven = 'A' if xstate[7] else '07'
    eight = 'A' if xstate[8] else '08'
    nine = 'A' if xstate[9] else '09'
    ten = 'A' if xstate[10] else '10'
    eleven = 'A' if xstate[11] else 'sf'
    twelve = 'A' if xstate[12] else '12'
    thirteen = 'A' if xstate[13] else '13'
    fourteen = 'A' if xstate[14] else '14'
    fiften = 'A' if xstate[15] else 'sf'
    sixteen = 'A' if xstate[16] else '16'
    seventeen = 'A' if xstate[17] else '17'
    eightteen = 'A' if xstate[18] else '18'
    nineteen = 'A' if xstate[19] else '19'
    twenty = 'A' if xstate[20] else '20'
    twentyone = 'A' if xstate[21] else '21'
    twentytwo = 'A' if xstate[22] else '22'
    twentythree = 'A' if xstate[23] else '23'
    twentyfour = 'A' if xstate[24] else 'wn'

    print('Play the LUDO GAME')
    print("There a TWO players in the game each controlling single piece \n"
          "The gameplay involves rolling dice to determine the moves \n"
          "and if a player is on a safe spot, they are secure,\nbut if not, they get killed "
          "and restart from the beginning")

    print(f'| {zero}    | {nine}   | {ten}   | {nineteen}   | {twenty}')
    print(f'| {one}    | {eight}   | {eleven}   | {eightteen}   | {twentyone}')
    print(f'| {two}    | {seven}   | {twelve}   | {seventeen}   | {twentytwo}')
    print(f'| {three}    | {six}   | {thirteen}   | {sixteen}   | {twentythree}')
    print(f'| {four}    | {five}   | {fourteen}   | {fiften}   | {twentyfour}')


def plot_game(xstate,zstate,xindex,zindex , turn):

    if turn == 1:
        zero = 'AA' if xstate[0] else ('BB' if zstate[0] else '00')
        one = 'AA' if xstate[1] else ('BB' if zstate[1] else '01')
        two = 'AA' if xstate[2] else ('BB' if zstate[2] else '02')
        three = 'AA' if xstate[3] else ('BB' if zstate[3] else '03')
        four = 'AA' if xstate[4] else ('BB' if zstate[4] else 'sf')
        five = 'AA' if xstate[5] else ('BB' if zstate[5] else '05')
        six = 'AA' if xstate[6] else ('BB' if zstate[6] else '06')
        seven = 'AA' if xstate[7] else ('BB' if zstate[7] else '07')
        eight = 'AA' if xstate[8] else ('BB' if zstate[8] else '08')
        nine = 'AA' if xstate[9] else ('BB' if zstate[9] else '09')
        ten = 'AA' if xstate[10] else ('BB' if zstate[10] else '10')
        eleven = 'AA' if xstate[11] else ('BB' if zstate[11] else 'sf')
        twelve = 'AA' if xstate[12] else ('BB' if zstate[12] else '12')
        thirteen = 'AA' if xstate[13] else ('BB' if zstate[13] else '13')
        fourteen = 'AA' if xstate[14] else ('BB' if zstate[14] else '14')
        fiften = 'AA' if xstate[15] else ('BB' if zstate[15] else 'sf')
        sixteen = 'AA' if xstate[16] else ('BB' if zstate[16] else '16')
        seventeen = 'AA' if xstate[17] else ('BB' if zstate[17] else '17')
        eightteen = 'AA' if xstate[18] else ('BB' if zstate[18] else '18')
        nineteen = 'AA' if xstate[19] else ('BB' if zstate[19] else '19')
        twenty = 'AA' if xstate[20] else ('BB' if zstate[20] else '20')
        twentyone = 'AA' if xstate[21] else ('BB' if zstate[21] else '21')
        twentytwo = 'AA' if xstate[22] else ('BB' if zstate[22] else '22')
        twentythree = 'AA' if xstate[23] else ('BB' if zstate[23] else '23')
        twentyfour = 'AA' if xstate[24] else ('BB' if zstate[24] else 'wn')

        print(f'| {zero}    | {nine}   | {ten}   | {nineteen}   | {twenty}')
        print(f'| {one}    | {eight}   | {eleven}   | {eightteen}   | {twentyone}')
        print(f'| {two}    | {seven}   | {twelve}   | {seventeen}   | {twentytwo}')
        print(f'| {three}    | {six}   | {thirteen}   | {sixteen}   | {twentythree}')
        print(f'| {four}    | {five}   | {fourteen}   | {fiften}   | {twentyfour}')

    else:
        zero = 'BB' if zstate[0] else ('AA' if xstate[0] else '00')
        one = 'BB' if zstate[1] else ('AA' if xstate[1] else '01')
        two = 'BB' if zstate[2] else ('AA' if xstate[2] else '02')
        three = 'BB' if zstate[3] else ('AA' if xstate[3] else '03')
        four = 'BB' if zstate[4] else ('AA' if xstate[4] else 'sf')
        five = 'BB' if zstate[5] else ('AA' if xstate[5] else '05')
        six = 'BB' if zstate[6] else ('AA' if xstate[6] else '06')
        seven = 'BB' if zstate[7] else ('AA' if xstate[7] else '07')
        eight = 'BB' if zstate[8] else ('AA' if xstate[8] else '08')
        nine = 'BB' if zstate[9] else ('AA' if xstate[9] else '09')
        ten = 'BB' if zstate[10] else ('AA' if xstate[10] else '10')
        eleven = 'BB' if zstate[11] else ('AA' if xstate[11] else 'sf')
        twelve = 'BB' if zstate[12] else ('AA' if xstate[12] else '12')
        thirteen = 'BB' if zstate[13] else ('AA' if xstate[13] else '13')
        fourteen = 'BB' if zstate[14] else ('AA' if xstate[14] else '14')
        fiften = 'BB' if zstate[15] else ('AA' if xstate[15] else 'sf')
        sixteen = 'BB' if zstate[16] else ('AA' if xstate[16] else '16')
        seventeen = 'BB' if zstate[17] else ('AA' if xstate[17] else '17')
        eightteen = 'BB' if zstate[18] else ('AA' if xstate[18] else '18')
        nineteen = 'BB' if zstate[19] else ('AA' if xstate[19] else '19')
        twenty = 'BB' if zstate[20] else ('AA' if xstate[20] else '20')
        twentyone = 'BB' if zstate[21] else ('AA' if xstate[21] else '21')
        twentytwo = 'BB' if zstate[22] else ('AA' if xstate[22] else '22')
        twentythree = 'BB' if zstate[23] else ('AA' if xstate[23] else '23')
        twentyfour = 'BB' if zstate[24] else ('AA' if xstate[24] else 'wn')

        print(f'| {zero}    | {nine}   | {ten}   | {nineteen}   | {twenty}')
        print(f'| {one}    | {eight}   | {eleven}   | {eightteen}   | {twentyone}')
        print(f'| {two}    | {seven}   | {twelve}   | {seventeen}   | {twentytwo}')
        print(f'| {three}    | {six}   | {thirteen}   | {sixteen}   | {twentythree}')
        print(f'| {four}    | {five}   | {fourteen}   | {fiften}   | {twentyfour}')

def kill(xstate, zstate, xindex , zindex,turn , xlist, zlist):

    if turn == 1:
        if xindex ==zindex:
            zstate[zindex] = 0
            zlist = [0]
            zindex = 0
        plot_game(xstate,zstate,xindex,zindex,turn)

    else:
        if zindex == xindex:
            xstate[xindex] = 0
            xlist = [0]
            xindex = 0
        plot_game(xstate, zstate, xindex, zindex, turn)

if __name__ == '__main__':
    xstate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    safe = [4,11,15]
    display()
    # xlist = [0]
    # zlist = [0]

    xfirst = 1
    zfirst = 1
    xindex = 0
    zindex = 0
    turn = 1
    while True:
        if turn == 1:
            print('-----------------------')
            print('Player A turn')
        else:
            print('-----------------------')
            print('Player B turn')
        a = (input("press 'enter' roll the dice: _"))
        anum = random.randint(1,6)
        print(f'The number is {anum}')
        print('-----------------------')

        if turn == 1:
            # print(f'player A turn')
            if xfirst == 1:
                xindex += (anum-1)
                xlist.append(xindex)
                # print('xlist',xlist)
                # print('zlist', zlist)

                xfirst = 0
                xstate[xindex] = 1
            else:
                xindex += (anum)
                xlist.append(xindex)
                # print('xlist', xlist)
                # print('zlist', zlist)
                if xindex >= 24:
                    print('Player A is winner')
                    break
                # xstate[xindex] = 1
                for i in range(len(xstate)):
                    if i == xlist[-1]:
                        # xlist = [0]
                        xstate[i] = 1
                    else:
                        xstate[i] = 0
        else:
            # print(f'player B turn')
            if zfirst == 1:
                zindex += (anum - 1)
                zlist.append(zindex)
                # print('xlist', xlist)
                # print('zlist', zlist)
                zfirst = 0
                zstate[zindex] = 1
            else:
                zindex += (anum)
                zlist.append(zindex)
                # print('xlist', xlist)
                # print('zlist', zlist)
                if zindex >= 24:
                    print('Player B is winner')
                    break
                # zstate[zindex] = 1
                for i in range(len(zstate)):
                    if i == zlist[-1]:
                        zstate[i] = 1
                        # zlist = [0]
                    else:
                        zstate[i] = 0

        kill(xstate, zstate, xindex , zindex,turn,xlist,zlist)
        xlist = [0]
        zlist = [0]

        if turn == 1:
            if xindex == zindex and xindex in safe:
                pass

            elif xindex == zindex:
                zindex = 0
        else:
            if xindex == zindex and zindex in safe:
                pass
            elif xindex == zindex:
                xindex = 0


        turn = 1 - turn













