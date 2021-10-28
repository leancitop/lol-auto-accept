import pyautogui as pg
import time

# Función búcle que busca constantemente el .png de 'partida encontrada' y al encontrarlo acepta la partida y termina el bucle.

def aceitarPartida():
    aceitar = False
    while aceitar == False:

        aceitarPng = pg.locateCenterOnScreen('E:\\PYTHON VSCODE\\workspace\\autoaccept\\aceitar.png')
        if aceitarPng != None:

            aceitar = True
            print('Partida encontrada')

            pg.click(aceitarPng)
            pg.moveTo(10, 10)

# Función boolean que devuelve 'Select Champ' = True o False

def checkSelectChamp():
    state = False
    selectPng = pg.locateCenterOnScreen('E:\\PYTHON VSCODE\\workspace\\autoaccept\\pick.png')
    if selectPng != None:
        state = True

    return state

# Función para cerrar el programa

def cerrar():
    print('Entraste a select champ. Cerrando programa...')
    time.sleep(5)
    quit()

# Función boolean que devuelve 'Pantalla de Partida Aceptada' = True o False

def checkAceitado():
    aceitado = True
    aceitadoPng = pg.locateCenterOnScreen('E:\\PYTHON VSCODE\\workspace\\autoaccept\\aceitado.png')
    if aceitadoPng != None:
        aceitado = True
    else: aceitado = False
    return aceitado

# Función búcle de checkAceitado() que rompe cuando detecta False

def bucleAceitado():
    while True:
        if checkAceitado() == False:
            break

def main():
    while True:
        print('Buscando partida...')

        aceitarPartida() # Se ejectua el bucle de aceptar partida hasta que popee o cierres el script
        
        bucleAceitado() # Una vez que acepta la partida, te aparece la pantalla de partida aceptada. Una vez que esta se va,
                        # Significa que entraste en select champ o alguien rechazó.

        time.sleep(2) # Una vez que 'Pantalla de Partida Aceptada' = False, le da un rato al programa de cargar select champ si es que
                      # la partida se aceptó.

        if checkSelectChamp() == True:  # Si entraste a select champ, el programa se cierra
            cerrar()
        else: print('Partida rechazada') # Si no entraste a select champ, se sigue ejecutando el bucle.

# La única manera de que el programa se detenga de 
# buscar partida es cerrando el script por tu cuenta
# o que entres en select champ.

if __name__ == '__main__':
    main()