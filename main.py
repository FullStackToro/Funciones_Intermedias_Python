
import random
def randInt (min=0,max=100):
    num=random.random()*(max-min)+min
    num=round(num)
    print(num)


def beCheerful(name='', repeat=2):  # set defaults when declaring the parameters
    print(f"good morning {name}\n" * repeat)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  randInt(99)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
