from bibliopixel import LEDStrip
import bibliopixel.colors as colors
from bibliopixel.animation import BaseStripAnim

import math
import time
import random

class LarsonScanner(BaseStripAnim):
    """Larson scanner (i.e. Cylon Eye or K.I.T.T.)."""

    def __init__(self, led, color, tail=2, start=0, end=-1):
        super(LarsonScanner, self).__init__(led, start, end)
        self._color = color

        self._tail = tail + 1  # makes tail math later easier
        if self._tail >= self._size / 2:
            self._tail = (self._size / 2) - 1

        self._direction = -1
        self._last = 0
        self._fadeAmt = 256 / self._tail

    def step(self, amt = 1):
        self._led.all_off()

        self._last = self._start + self._step
        self._led.set(self._last, self._color)

        for i in range(self._tail):
            self._led.set(self._last - i, colors.color_scale(self._color, 255 - (self._fadeAmt * i)))
            self._led.set(self._last + i, colors.color_scale(self._color, 255 - (self._fadeAmt * i)))

        if self._start + self._step >= self._end:
            self._direction = -self._direction
        elif self._step <= 0:
            self._direction = -self._direction

        self._step += self._direction * amt
class LarsonRainbow(LarsonScanner):
    """Larson scanner (i.e. Cylon Eye or K.I.T.T.) but Rainbow."""

    def __init__(self, led, tail=2, start=0, end=-1):
        super(LarsonRainbow, self).__init__(
            led, colors.Off, tail, start, end)

    def step(self, amt = 1):
        self._color = colors.hue_helper(0, self._size, self._step)
        self._color = colors.hue2rgb_rainbow((self._step * (256 / self._size)) % 256)

        super(LarsonRainbow, self).step(amt)
class Rainbow(BaseStripAnim):
    """Generate rainbow distributed over 256 pixels.
       If you want the full rainbow to fit in the number of pixels you
       are using, use RainbowCycle instead
    """

    def __init__(self, led, start=0, end=-1):
        super(Rainbow, self).__init__(led, start, end)

    def step(self, amt = 1):
        for i in range(self._size):
            h = (i + self._step) % 255
            self._led.set(self._start + i, colors.hue2rgb_rainbow(h))

        self._step += amt
        overflow = self._step - 256
        if overflow >= 0:
            self._step = overflow

class RainbowCycle(BaseStripAnim):
    """Generate rainbow wheel equally distributed over strip."""

    def __init__(self, led, start=0, end=-1):
        super(RainbowCycle, self).__init__(led, start, end)

    def step(self, amt = 1):
        for i in range(self._size):
            c = colors.hue_helper(i, self._size, self._step)
            self._led.set(self._start + i, c)

        self._step += amt
        overflow = self._step - 256
        if overflow >= 0:
            self._step = overflow
