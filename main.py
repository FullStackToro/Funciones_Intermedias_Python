
import random
def randInt (min=0,max=100):
    if min>max:
        return 'Error: Verificar valor mínimo y máximo.'
    elif max<0:
        return 'Error: El valor máximo no puede ser menor a cero (0).'
    else:
        num=random.random()*(max-min)+min
        num=round(num)
        return num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print(randInt())
  print('max50: ',randInt(max=50))
  print('min50: ', randInt(min=50))
  print('min50max500:', randInt(min=50,max=500))
  print('min500max50:', randInt(min=500, max=50))


