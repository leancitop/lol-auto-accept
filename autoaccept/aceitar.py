import pyautogui as pg
import time

def aceitarPartida():
    aceitar = False
    while aceitar == False:

        aceitarPng = pg.locateCenterOnScreen('E:\\PYTHON VSCODE\\workspace\\autoaccept\\aceitar.png')
        if aceitarPng != None:

            aceitar = True
            print('Partida encontrada')

            pg.click(aceitarPng)
            pg.moveTo(10, 10)

def checkSelectChamp():
    state = False
    selectPng = pg.locateCenterOnScreen('E:\\PYTHON VSCODE\\workspace\\autoaccept\\pick.png')
    if selectPng != None:
        state = True

    return state

def bucleAceitado():
    while True:
        if checkAceitado() == False:
            break


def cerrar():
    print('Entraste a select champ. Cerrando programa...')
    time.sleep(5)
    quit()

def checkAceitado():
    aceitado = True
    aceitadoPng = pg.locateCenterOnScreen('E:\\PYTHON VSCODE\\workspace\\autoaccept\\aceitado.png')
    if aceitadoPng != None:
        aceitado = True
    else: aceitado = False
    return aceitado

def main():
    while True:
        print('Buscando partida...')

        aceitarPartida()
        
        bucleAceitado()

        time.sleep(2)

        if checkSelectChamp() == True:
            cerrar()
        else: print('Partida rechazada')


    # i = 0
    #Bucle para verificar la funcion aceitado
    # while i <= 500:
    #     i +=1
    #     print('aceitado =',checkAceitado())
    #     time.sleep(0.1)

   # # Bucle para verificar la funcion select champ
    # while i <= 500:
    #     i += 1
    #     print('selectChamp =', checkSelectChamp())
    #     time.sleep(0.1)
    # bucleAceitado()

if __name__ == '__main__':
    main()