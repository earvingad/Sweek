# Intructions for KMK

1. [Install Circuitpython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) to your RP2040-zero and then [KMK](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/Getting_Started.md#tldr-quick-start-guide). 
2. Rename the drives as `SWEEKL` and `SWEEKR`, respectively. Follow [this guide](https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy) to learn how to do it.
3. Follow the [Preparation guide for Display in KMK](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/Display.md#preparation) for the required libraries for the SSD1306 oled display.
4. Download the `neopixel.py` or `neopixel.mpy` from [here](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/releases) and place it inside the `lib` folder of each RP2040-zero.
5. Copy the `code.py` to each RP2040-zero. It will automatically detect which half is which.

Enjoy!
