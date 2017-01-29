from gpiozero import LED, Button
from signal import pause
from time import sleep

try:
    led1 = LED(int(input('led1:')))
    led2 = LED(int(input('led2: ')))
    button = Button(2)
    led1.on()
    led2.off()
    print('on, off')
    mode = True

    while True:
        button.wait_for_press()
        if mode == True:
            led1.off()
            led2.on()
            print('off, on')
            mode = False
        elif mode == False:
            led1.on()
            led2.off()
            print('on, off')
            mode = True
        sleep(0.25)
except:
    print('error: invalid input')
