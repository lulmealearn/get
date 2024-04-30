import RPi.GPIO as GPIO 
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1 , 8, 5, 12, 6]
comp = 14
troyka = 13
leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def decimal_to_binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]

# снимаем показания с тройки
def adc_sar():

    result = 0

    for i in range(7, -1, -1): 
        result += 2**i
        dac_p = []
        dac_p = decimal_to_binary(result)
        GPIO.output(dac, dac_p)
        time.sleep(0.001)
        compv = GPIO.input(comp)
        if compv == GPIO.HIGH:
            result -= 2**i
    
    return result


try:
    voltage = 0
    result_experience = []
    time_start = time.time()
    count = 0
    
# зарядка конденсатора
    # GPIO.setup(troyka, GPIO.OUT, initial= GPIO.HIGH)
    GPIO.output(troyka, 1)
    while voltage < 256*0.97:
        print(f"voltage {3.3 * voltage/ 255:.4f} В")
        voltage = adc_sar()
        result_experience.append(voltage)
        time.sleep(0.005)
        count += 1
        GPIO.output(leds, decimal_to_binary(voltage))
        
# разрядка конденсатора
    GPIO.output(troyka, 0)
    # GPIO.setup(troyka, GPIO.OUT, initial= GPIO.LOW)
    while voltage> 256*0.02:
        print(f"voltage {3.3 * voltage/ 255:.4f} В")
        voltage = adc_sar()
        result_experience.append(voltage)
        time.sleep(0.005)
        count += 1
        GPIO.output(leds, voltage)
    time_experiment = time.time() - time_start

# записываем данные в файлы
    with open("data.txt", 'w') as f:
        for i in result_experience:
            f.write(str(i)+ '\n')

    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01289')
    
    y = [i/256*3.3 for i in result_experience]
    x = [i*time_experiment/count for i in range(len(result_experience))]
    pyplot.plot(x,y) 
    pyplot.show()

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()




