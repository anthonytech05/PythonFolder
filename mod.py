import getpass
from time import sleep #import specific function out from the file

from time import sleep #import either to avoid conflict etc




pass_code = getpass.getpass("Enter your 4 digit pass code")

#print(f'Revealing your pass code: {pass_code}')

for i in range(10):
    sleep(1)
print(f'{i + 1} second elapsed')
dice1, dice2, = rd(1,6), rd(1,6)
print(f'dice thrown: {dice1}, {dice2}')