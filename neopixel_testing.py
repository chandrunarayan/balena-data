import board
import neopixel
from time import sleep
pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, 
                           brightness=1, auto_write=False,
                           pixel_order=ORDER)
pixels.fill((0,0,0))
print(pixels)
pixels.show()
sleep(2)
pixels.fill((255,255,255))
print(pixels)
pixels.show()
sleep(2)

