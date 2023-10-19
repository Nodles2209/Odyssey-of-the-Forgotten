from time import sleep

#Colors = {'blue':'\033[94m', 'yellow':'\033[93m', 'green':'\033[92m', 'red':'\033[91m', 'lightblue':'\033[36m', 'flush':'\033[5m'}

testkeyword = {'YOU ':'92', ' CANNOT ':'91', ' GO ':'94', ' THERE ':'93', ' !!!!!!':'36'}

def textout_normal(tin, color):
    print('\033[' + str(color) + 'm', end='')
    for element in tin:
        sleep(0.1)
        print(element, end='', flush=True)

def textout_keyword(keywords):
    for element in keywords:
        print('\033[' + str(keywords[element]) + 'm', end='')
        for e in element:
            sleep(0.1)
            print(e, end='', flush=True)

print('\033[94mtestkeyword: ')
textout_keyword(testkeyword)

print('\n\033[94mnormal output in green: ')
textout_normal('YOU CANNNOT GO THERE !!!!!!', '92')
print('\n')
