import sys

print('Welcome to the UHF NEXEDGE LCN Calculator\n')

while True:
    print('\nMENU:\n')
    print('[1] LCN-to-Frequency Calculator\n')
    print('[2] Frequency-to-LCN Calculator\n')
    print('[3] Quit\n')

    while True:
        progSelection = input('Enter Your Selection: ')
        try:
            progSelection = int(progSelection)
            if (progSelection not in (1, 2, 3)):
                print('\nERROR: Invalid Menu Selection\n')
                continue
            break
        except:
            print('\nERROR: Invalid Menu Selection\n')

    
    if progSelection == 1:                 
        while True:
            while True:
                inputLcn = input('\nPlease Enter a LCN (enter 0 to return to the menu): ')
                try:
                    inputLcn = int(inputLcn)
                    if inputLcn < 0:
                        print('\nERROR: LCN must be >= 1\n')
                    break
                except:
                    print('\nERROR: Invalid input. Must be an integer.')

            if ((inputLcn > 0) and (inputLcn <= 400)):
                resultFreq = 450 + (inputLcn - 1) * 0.0125
                print('The frequency is: ',resultFreq, 'MHz\n')

            elif ((inputLcn >= 401) and (inputLcn <= 800)):
                resultFreq = 460 + (inputLcn - 401) * 0.0125
                print('The frequency is: ',resultFreq, 'MHz\n')

            elif inputLcn > 800:
                print('This LCN is used for a non-standard frequency. No frequency can be reported.\n')

            elif inputLcn == 0:
                break


    elif progSelection == 2:
        while True:
            while True:
                inputFreq = input('Please enter a frequency (enter "0" to return to the menu): ')
                try:
                    inputFreq = float(inputFreq)
                    if inputFreq < 0:
                        print('\nERROR: Invalid Frequency\n')
                        continue
                    break
                except:
                    print('\nERROR: Invalid Frequency\n')

            if (inputFreq / 0.00625).is_integer() == 0:
                print('\nInvalid Input Frequency. Please use a 6.25 KHz step.\n')

            elif ((inputFreq >= 450.0) and (inputFreq < 455.0)) and ((inputFreq / 0.00625).is_integer()):
                resultLCN = ((inputFreq - 450) / 0.0125) + 1
                print('The LCN is: ',(int)(resultLCN),'\n')

            elif ((inputFreq >= 460.0) and (inputFreq < 465.0)) and ((inputFreq / 0.00625).is_integer()):
                resultLCN = ((inputFreq - 460) / 0.0125) + 401
                print('The LCN is: ',(int)(resultLCN),'\n')

            elif inputFreq == 0: 
                break

            elif (inputFreq > 0): 
                print('This frequency uses a non-standard LCN. No LCN can be reported.\n')


    elif progSelection == 3:
        break
