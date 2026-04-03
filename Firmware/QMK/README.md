# Flash
Here you will find precompiled uf2 files that also work with vial.

1. Download the `sweek-vial-left/right.uf2`
2. Put you rp2040 in boot mode and copy/paste the corresponding `sweek-vial-left/right.uf2` to each half.
3. Edit the keymap to your needs with vial.

If you want to compile yourself, you can download the source files from the sweek folder, edit them to your taste and compile/flash it with `make sweek:vial:uf2-split-left` and `make sweek:vial:uf2-split-right` for each half.


## QMK-github actions
Alternatively, you can compile the code using github actions:

1. Clone [this repo](https://github.com/earvingad/qmk-firmware-builder)
2. Edit the config to your taste, commit your changes and the github action will compile the firmware.
3. Flash both sides with the `sweek-vial.uf2` master by default is Right side. Change it in the `config.h` if you  prefer left. 
