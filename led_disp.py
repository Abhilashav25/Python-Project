from machine import Pin
import utime

row_pins = [15, 2, 18, 4, 16, 17, 5]
col_pins = [19, 21, 22, 23, 14]

row_pins = [Pin(pin, Pin.OUT) for pin in row_pins]
col_pins = [Pin(pin, Pin.OUT) for pin in col_pins]

def clear_display(row_pins, col_pins):
    for row_pin in row_pins:
        row_pin.value(0)  # Set to LOW for common cathode
    for col_pin in col_pins:
        col_pin.value(1)  # Set to HIGH to turn off all columns

def pattern_matrix(num1=[], row_pins=[], col_pins=[]):
    for i in range(5):
        cp = col_pins[i]
        for j in range(7):
            rp = row_pins[j]
            num = num1[j][i]  # Corrected indexing
            if num == 1:
                cp.off()
                rp.on()
            else:
                cp.on()
                rp.off()
            utime.sleep_us(200)
            clear_display(row_pins, col_pins)
#         utime.sleep_ms(1)

num1 = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]
    ]
num2 = [
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1]
    ]
num3 = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

num4 = [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]

num5 = [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ]

num6 = [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ]

num7 = [
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ]

num8 = [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ]

num9 = [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ]

num0 = [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ]
while True:
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num1,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num2,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num3,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num4,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num5,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num6,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num7,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num8,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num9,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)
    for i in range(50):
        clear_display(row_pins, col_pins)
        pattern_matrix(num0,row_pins=row_pins, col_pins=col_pins)
        utime.sleep_us(1)
    utime.sleep(1)