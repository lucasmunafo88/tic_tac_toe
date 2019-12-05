# Tic_tac_toe  
## :no_entry:Version necesaria de python  
- [x] python >= 3.5
## :unlock:Como instalar todas las dependencias  
```
pipenv install
```
#### En caso de que no tengas pipenv instalado
```
sudo apt install pipenv
```
## :thumbsup:Como ejecutar Tic-Tac-Toe  
```
pipenv run python main.py
```
## Desarrollo
Lo desafiante de desarrollar el tic-tac-toe fue más que nada pensar la lógica de los posibles movimientos y como verificar la victoria. Si bien podría haberlo pensado como una lista de tuplas que contenga todos los movimientos posibles como coordenadas y que se limite a verificar esos valores, me pareció más interesante y desafiante examinar el tablero en si. Lo mismo para evaluar cual seria el mejor movimiento posible. Para ello me base en el principio anterior pero pensando en que tenia que contar cuantos símbolos iguales había, y si contenía un espacio vacío en una línea.

Utilice exactamente la misma lógica para el test que comprueba que la pc realice movimientos forzados y creo que eso fue como lo más desafiante del desarrollo.

A lo largo del proyecto se me ocurrieron varias formas de realizar el juego, una de ellas es la que mencione al principio. Otra forma que se me ocurrió fue trabajando con una lista, entre otras.
