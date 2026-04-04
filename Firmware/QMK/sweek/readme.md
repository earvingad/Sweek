# sweek

![sweek](https://raw.githubusercontent.com/earvingad/Sweek/refs/heads/main/src/sweek.jpeg)

Sweek is a Ferris/sweep inspired, 36 keys split keyboard with encoders and OLED screens (although I have not configured OLED screens for QMK).

* Keyboard Maintainer: [earvingad](https://github.com/earvingad)
* Hardware Supported: [sweek](https://github.com/earvingad/sweek)

Compile with vial support and flash with EE_HANDS

    make sweek:vial:uf2-split-left

And then righ side:

    make sweek:vial:uf2-split-right

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Physical reset button**: Press quickly twice the reset button from the RP2040-zero.
* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
