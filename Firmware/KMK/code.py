print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner, MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Combos, Chord
from kmk.modules.holdtap import HoldTap
from kmk.modules.sticky_keys import StickyKeys
from kmk.modules.tapdance import TapDance
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.extensions.international import International
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.media_keys import MediaKeys

# side = SplitSide.LEFT
# side = SplitSide.RIGHT
from storage import getmount
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=False,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
    uart_flip=False,  # Reverses the RX and TX pins if both are provided
    use_pio=False,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

if side == SplitSide.RIGHT:
    row_pins = (board.GP3, board.GP4, board.GP5, board.GP6)
    col_pins = (board.GP29, board.GP28, board.GP27, board.GP26, board.GP15)
else:
    row_pins = (board.GP29, board.GP28, board.GP27, board.GP26)
    col_pins = (board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)

enca=board.GP10
encb=board.GP9
encs=[board.GP11]

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()
        # create and register the scanner
        self.matrix = [
            MatrixScanner(
            # required arguments:
            row_pins=row_pins,
            column_pins=col_pins,
            # columns_to_anodes=DiodeOrientation.COL2ROW,
                ),
            RotaryioEncoder(
            # require argument:
            pin_a=enca,
            pin_b=encb,
            divisor=4,
                ),
            KeysScanner(
            # require argument:
            pins=encs,
            value_when_pressed=False,
            pull=True,
                ),
        ]
        self.coord_mapping = [
                0, 1, 2, 3, 4,   27, 26, 25, 24, 23,
                5, 6, 7, 8, 9,   32, 31, 30, 29, 28,
                10,11,12,13,14,  37, 36, 35, 34, 33,
                15,16,17,18,19,  42, 41, 40, 39, 38,
                      20,21,22,  45, 44, 43 ]

keyboard = MyKeyboard() #KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

mousekeys = MouseKeys(
    max_speed = 30,
    acc_interval = 20, # Delta ms to apply acceleration
    move_step = 1
)

combos = Combos()
holdtap = HoldTap()
sticky_keys = StickyKeys(release_after=500)
caps_word = CapsWord()
tapdance = TapDance()
keyboard.modules.append(Layers())
keyboard.modules.append(combos)
keyboard.modules.append(tapdance)
keyboard.modules.append(holdtap)
keyboard.modules.append(mousekeys)
keyboard.modules.append(caps_word)
keyboard.modules.append(sticky_keys)
keyboard.extensions.append(International())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(split)

try:
    import busio
    from kmk.extensions.display import Display, TextEntry
    # For SSD1306
    from kmk.extensions.display.ssd1306 import SSD1306
    # Replace SCL and SDA according to your hardware configuration.
    i2c_bus = busio.I2C(board.GP13, board.GP12)

    driver = SSD1306(
        # Mandatory:
        i2c=i2c_bus,
        # Optional:
        device_address=0x3C,
        )
    # debug = Debug(__name__)
    display = Display(
        display=driver,
        entries=[
            TextEntry(text="Colemak", x=40, y=13, layer=0),
            TextEntry(text="Mouse", x=40, y=13, layer=1),
            TextEntry(text="Numbers", x=40, y=13,  layer=2),
            TextEntry(text="Function", x=40, y=13, layer=3),
            TextEntry(text="Symbols", x=40, y=13, layer=4),
            TextEntry(text="Extras", x=40, y=13, layer=5),
            TextEntry(text=" Sweek ", x=40, y=13, inverted=True, layer=6),
        ],
        #Optional width argument. Default is 128.
        width=128,
        height=32,
    )
    keyboard.extensions.append(display)
except:
    pass


import neopixel
pixel_pin = board.GP16
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
RED = (55, 0, 0)
GREEN = (0, 55, 0)
BLUE = (0, 0, 55)
YELLOW = (55, 55, 0)
CYAN = (0, 55, 55)
PURPLE = (55, 0, 55)
WHITE = (55, 55, 55)

def on_layer_change(self, layer):
    if layer == 0:
        pixels.fill(RED)
    elif layer == 1:
        pixels.fill(BLUE)
    elif layer == 2:
        pixels.fill(GREEN)
    elif layer == 3:
        pixels.fill(WHITE)
    elif layer == 4:
        pixels.fill(PURPLE)
    elif layer == 5:
        pixels.fill(CYAN)
    elif layer == 6:
        pixels.fill(CYAN)
    # update the LEDs manually if no animation is active:
    pixels.show()

class RGBLayers(Layers):
    def during_bootup(self, sandbox):
        layer=keyboard.active_layers[0]
        on_layer_change(self, layer)

    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        #pixels.on_layer_change(layer)
        on_layer_change(self, layer)

    def deactivate_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        layer=keyboard.active_layers[0]
        on_layer_change(self, layer)


keyboard.modules.append(RGBLayers())


SPC_ALT  = KC.HT(KC.SPC, KC.SK(KC.LALT))
DOT_APP  = KC.HT(KC.DOT, KC.APP, tap_interrupted=True)
BSPC_ALT = KC.HT(KC.BSPC, KC.RALT)

SK_LGUI = (KC.SK(KC.LGUI))
SK_LCTL = (KC.SK(KC.LCTL))
SK_CTLS = (KC.SK(KC.LCTL(KC.LSFT)))
SK_RSFT = (KC.SK(KC.RSFT))
SK_RALT = (KC.SK(KC.RALT))

DOT_COM = KC.TD(KC.DOT, KC.COMMA, tap_time=200)
CTL_GUI = KC.TD(SK_LCTL, KC.HT(SK_LGUI, SK_CTLS,), tap_time=200)
SK_SALT = KC.TD(KC.RSFT, SK_RALT, tap_time=200)

R_L1    = KC.HT(KC.R, KC.MO(1), tap_interrupted=True)
S_L2    = KC.HT(KC.S, KC.MO(2), tap_interrupted=True)
T_L3    = KC.HT(KC.T, KC.MO(3), tap_interrupted=True)
N_L5    = KC.HT(KC.N, KC.MO(5), tap_interrupted=True)
E_L4    = KC.HT(KC.E, KC.MO(4), tap_interrupted=True)
ENT_L5  = KC.HT(KC.ENT, KC.MO(5))
ESC_L5  = KC.HT(KC.ESC, KC.MO(5))

CTL_ALT = KC.LCTL(KC.LALT)

_______ = KC.TRNS
XXXXXXX = KC.NO

combos.combos = [
    Chord((KC.W, KC.F), KC.TAB),
    Chord((KC.F, KC.P), KC.CW),
    Chord((KC.O, KC.Y), KC.DEL),
    Chord((KC.O, KC.L), KC.LBRC),
    ]

keyboard.keymap =  [
    [ # 0 COLEMAK
        KC.Q    , KC.W    , KC.F    , KC.P    , KC.G   ,              KC.J     , KC.L      , KC.O      , KC.Y      , KC.SCLN ,
        KC.A    , R_L1    , S_L2    , T_L3    , KC.D   ,              KC.H     , N_L5      , E_L4      , KC.I      , KC.U    ,
        KC.Z    , KC.X    , KC.C    , KC.V    , KC.B   ,              KC.K     , KC.M      , KC.COMMA  , DOT_APP   , KC.SLSH ,
        XXXXXXX , XXXXXXX , CTL_GUI , SPC_ALT , ESC_L5 ,              ENT_L5   , BSPC_ALT  , SK_RSFT   , XXXXXXX   , XXXXXXX ,
                            KC.DOWN , KC.UP   , KC.ENT ,              KC.ENT   , KC.LEFT   , KC.RIGHT  ,
    ],
    [ # 1 Mouse
        _______ , _______ , _______ , _______ , _______ ,             _______  , KC.MB_LMB , KC.MW_UP  , KC.MB_RMB , _______  ,
        _______ , _______ , _______ , _______ , _______ ,             _______  , KC.MS_LT  , KC.MS_DN  , KC.MS_UP  , KC.MS_RT ,
        _______ , _______ , _______ , _______ , _______ ,             _______  , KC.MB_MMB , KC.MW_DN  , _______   , _______  ,
        XXXXXXX , XXXXXXX , _______ , _______ , _______ ,             _______  , _______   , _______   , XXXXXXX   , XXXXXXX  ,
                           KC.RIGHT , KC.LEFT , KC.ENT  ,             _______  , KC.LSFT(KC.TAB)   , KC.TAB,
    ],
    [ # 2 Right Numbers/Shift symbols
        _______ , _______ , _______ , _______ , _______ ,             KC.PPLS   , KC.N7     , KC.N8     , KC.N9    , KC.PAST  ,
        _______ , _______ , _______ , _______ , _______ ,             KC.PMNS   , KC.N4     , KC.N5     , KC.N6    , DOT_COM  ,
        _______ , _______ , _______ , _______ , _______ ,             KC.N0     , KC.N1     , KC.N2     , KC.N3    , KC.PSLS  ,
        XXXXXXX , XXXXXXX , _______ , _______ , _______ ,             _______   , _______   , _______   , XXXXXXX   , XXXXXXX  ,
                            _______ , _______ , _______ ,             KC.LCTL(KC.N0)        ,  KC.LCTL(KC.MW_DN) , KC.LCTL(KC.MW_UP)  , 
    ],
    [ # 3 Function keys
        KC.RLD  , KC.RESET, _______ , _______ , _______ ,             _______  , KC.F7     , KC.F8     , KC.F9     , KC.F10   ,
        _______ , _______ , CTL_ALT , _______ , _______ ,             _______  , KC.F4     , KC.F5     , KC.F6     , KC.F11   ,
        _______ , _______ , _______ , _______ , _______ ,             _______  , KC.F1     , KC.F2     , KC.F3     , KC.F12   ,
        XXXXXXX , XXXXXXX , _______ , _______ , _______ ,             _______  , _______   , _______   , XXXXXXX   , XXXXXXX  ,
                            _______ , _______ , _______ ,             KC.MPLY  , KC.VOLD   , KC.VOLU   , 
    ],
    [ # 4 Left Symbols
        KC.EXLM , KC.AT   , KC.HASH , KC.DLR  , KC.PERC ,             KC.CIRC  , KC.AMPR   , _______   , KC.GRV    , _______  ,
        KC.MINS , KC.EQL  , KC.LBRC , KC.QUOT , KC.BSLS ,             KC.ASTR  , KC.LPRN   , _______   , KC.RPRN   , _______  ,
        KC.PLUS , KC.UNDS , KC.RBRC , KC.RCBR , KC.PIPE ,             _______  , KC.NUBS   , _______   , _______   , _______  ,
        XXXXXXX , XXXXXXX , _______ , _______ , _______ ,             _______  , _______   , _______   , XXXXXXX   , XXXXXXX  ,
                            _______ , _______ , _______ ,             _______  , _______   , _______   , 
    ],
    [ # 5 Nav/extras
        _______ , KC.HOME , KC.PGUP , _______ , _______ ,             _______  , _______   , _______   ,  KC.RESET ,  KC.RLD  ,
        KC.LEFT , KC.DOWN , KC.UP   , KC.RIGHT, SK_LGUI ,             KC.TG(1) , KC.BSPC   , _______   ,  _______  ,  _______ ,
        _______ , KC.END  , KC.PGDN , KC.BSPC , KC.ENT  ,             KC.TG(6) , _______   , _______   ,  _______  ,  _______ ,
        XXXXXXX , XXXXXXX , _______ , _______ , _______ ,             _______  , _______   , _______   ,  XXXXXXX  ,  XXXXXXX ,
                            _______ , _______ , _______ ,             KC.ENT   , KC.DOWN   , KC.UP     , 
    ],
    [ # 6 Optional Layer
        KC.Q    , KC.W    , KC.F    , KC.P    , KC.G   ,              KC.J     , KC.L      , KC.O      , KC.Y      , KC.SCLN ,
        KC.A    , KC.R    , KC.S    , KC.T    , KC.D   ,              KC.H     , KC.N      , KC.E      , KC.I      , KC.U    ,
        KC.Z    , KC.X    , KC.C    , KC.V    , KC.B   ,              KC.K     , KC.M      , KC.COMMA  , DOT_APP   , KC.SLSH ,
        XXXXXXX , XXXXXXX , CTL_GUI , SPC_ALT , ESC_L5 ,              ENT_L5   , BSPC_ALT  , SK_RSFT   , XXXXXXX   , XXXXXXX ,
                            KC.DOWN , KC.UP   , KC.ENT ,              KC.ENT   , KC.LEFT   , KC.RIGHT  ,
    ],
]


if __name__ == '__main__':
    keyboard.go()
