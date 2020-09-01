#!/usr/bin/python3
import random
#!/usr/bin/python3
number = random.randint(-10000, 10000)
if number > 0:
    last_D = number % 10
else:
    last_D = (number % 10) * -1
if last_D > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'. format(
        number, last_D))
elif last_D == 0:
    print('Last digit of {:d} is {:d} and is 0'. format(number, last_D))
else:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(
        number, last_D))
