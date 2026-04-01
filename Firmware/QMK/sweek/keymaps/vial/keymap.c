// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later
#include QMK_KEYBOARD_H

enum layers {
    L0,
    L1,
    L2,
    L3,
    L4,
    L5,
    L6
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
     /*
      * ┌───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┐
      * │ Q │ W │ E │ R │ T │       │ Y │ U │ I │ O │ P │
      * ├───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┤
      * │ A │ S │ D │ F │ G │       │ H │ J │ K │ L │ ; │
      * ├───┼───┼───┼───┼───┤       ├───┼───┼───┼───┼───┤
      * │ Z │ X │ C │ V │ B │       │ N │ M │ , │ . │ / │
      * └───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┘
      *           ┌───┐                   ┌───┐
      *           │GUI├───┐           ┌───┤Alt│
      *           └───┤Bsp├───┐   ┌───┤Ent├───┘
      *               └───┤   │   │   ├───┘
      *                   └───┘   └───┘
      */
    [L0] = LAYOUT(
        KC_Q    , KC_W      , KC_F      , KC_P           , KC_G   ,              KC_J     , KC_L      , KC_O      , KC_Y      , KC_SCLN ,
        KC_A    , LT(1,KC_R), LT(2,KC_S), LT(3,KC_T)     , KC_D   ,              KC_H     , LT(6,KC_N), LT(4,KC_E), KC_I      , KC_U    ,
        KC_Z    , KC_X      , KC_C      , KC_V           , KC_B   ,              KC_K     , KC_M      , KC_COMMA  , KC_DOT    , KC_SLSH ,
                              KC_LCTL   , LALT_T(KC_SPC) , LT(5,KC_ESC) ,        LT(5,KC_ENT)   , RALT_T(KC_BSPC) , OSM(MOD_RSFT)
    ),
    [L1] = LAYOUT(
        _______ , _______ , _______ , _______ , _______ ,             MS_WHLR  , MS_BTN1   , MS_WHLU  , MS_BTN2   , _______  ,
        _______ , _______ , MS_BTN1 , _______ , MS_BTN2 ,             MS_WHLL  , MS_LEFT   , MS_DOWN  , MS_UP     , MS_RGHT  ,
        _______ , _______ , _______ , _______ , _______ ,             _______  , MS_BTN3   , MS_WHLD  , _______   , _______  ,
                            _______ , KC_SPC  , _______ ,             _______  , _______   , _______                           
    ),
    [L2] = LAYOUT(
        _______ , KC_UP   , _______ , _______ , _______ ,             KC_PPLS   , KC_P7     , KC_P8     , KC_P9    , KC_PAST  ,
        _______ , KC_LEFT , _______ , KC_RIGHT, _______ ,             KC_PMNS   , KC_P4     , KC_P5     , KC_P6    , KC_DOT   ,
        _______ , KC_DOWN , _______ , KC_COMMA, _______ ,             KC_P0     , KC_P1     , KC_P2     , KC_P3    , KC_PSLS  ,
                            _______ , _______ , _______ ,             _______   , _______   , _______                          
    ),
    [L3] = LAYOUT(
        QK_REBOOT  , LSFT(KC_TAB)     , KC_TAB             , _______ , _______ ,             _______  , KC_F7     , KC_F8     , KC_F9     , KC_F10   ,
        LALT(KC_F4), LCTL(LSFT(KC_T)) , LSFT(KC_DEL)       , _______ , _______ ,             _______  , KC_F4     , KC_F5     , KC_F6     , KC_F11   ,
        _______    , LCTL(KC_LALT)    , LCTL(LALT(KC_DEL)) , _______ , _______ ,             _______  , KC_F1     , KC_F2     , KC_F3     , KC_F12   ,
                                                   _______ , _______ , _______ ,             _______  , _______   , _______                           
    ),
    [L4] = LAYOUT(
        KC_EXLM , KC_AT   , KC_HASH , KC_DLR  , KC_PERC ,             KC_CIRC  , KC_AMPR   , _______   , KC_GRV    , _______  ,
        KC_MINS , KC_EQL  , KC_LBRC , KC_QUOT , KC_BSLS ,             KC_ASTR  , KC_LPRN   , _______   , KC_RPRN   , _______  ,
        KC_PLUS , KC_UNDS , KC_RBRC , KC_RCBR , KC_PIPE ,             _______  , KC_NUBS   , _______   , _______   , _______  ,
                            _______ , _______ , _______ ,             KC_RCTL  , _______   , _______                           
    ),
    [L5] = LAYOUT(
        KC_CAPS , KC_HOME , KC_PGUP , KC_DEL  , KC_LSFT ,             _______  , _______   , KC_PGUP   ,  KC_HOME  ,  _______ ,
        KC_LEFT , KC_DOWN , KC_UP   , KC_RIGHT, OSM(MOD_LGUI) ,       TG(1)    , KC_BSPC   , _______   ,  _______  ,  _______ ,
        _______ , KC_END  , KC_PGDN , KC_BSPC , KC_ENT  ,             TG(6)    , _______   , KC_PGDN   ,  KC_END   ,  _______ ,
                            _______ , _______ , _______ ,             _______  , _______   , _______                           

    ),
    [L6] = LAYOUT(
        LGUI(KC_1) , LGUI(KC_2) , LGUI(KC_3)    , LGUI(KC_4)   , LGUI(KC_5)  ,           _______  , _______ , _______  , _______ , QK_REBOOT,
        LGUI(KC_H) , LGUI(KC_J) , LGUI(KC_K)    , LGUI(KC_L)   , LGUI(KC_ENT),           _______  , _______ , _______  , _______ , _______  ,
        LGUI(KC_Q) , LGUI(KC_M) , LGUI(KC_COMMA), LGUI(KC_DOT) , LGUI(KC_SPC),           _______  , _______ , _______  , _______ , _______  ,
                                  KC_LGUI       , KC_LCTL      , KC_LSFT     ,           _______  , _______ , _______                        
    )
};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [L0] = { ENCODER_CCW_CW(KC_DOWN, KC_UP  ),  ENCODER_CCW_CW(KC_LEFT, KC_RIGHT) },
    [L1] = { ENCODER_CCW_CW(UG_HUED, UG_HUEU),  ENCODER_CCW_CW(LSFT(KC_TAB), KC_TAB)  },
    [L2] = { ENCODER_CCW_CW(UG_VALD, UG_VALU),  ENCODER_CCW_CW(LCTL(MS_WHLD), LCTL(MS_WHLU))  },
    [L3] = { ENCODER_CCW_CW(UG_PREV, UG_NEXT),  ENCODER_CCW_CW(KC_VOLD, KC_VOLU) },
    [L4] = { ENCODER_CCW_CW(LSFT(KC_LEFT), LSFT(KC_RIGHT)),  ENCODER_CCW_CW(KC_RIGHT, KC_LEFT) },
    [L5] = { ENCODER_CCW_CW(UG_PREV, UG_NEXT),  ENCODER_CCW_CW(KC_DOWN, KC_UP) },
    [L6] = { ENCODER_CCW_CW(UG_PREV, UG_NEXT),  ENCODER_CCW_CW(KC_LEFT, KC_RIGHT) },
};
#endif

const rgblight_segment_t PROGMEM _L0[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_RED}
);
const rgblight_segment_t PROGMEM _L1[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_BLUE}
);
const rgblight_segment_t PROGMEM _L2[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_GREEN}
);
const rgblight_segment_t PROGMEM _L3[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_WHITE}
);
const rgblight_segment_t PROGMEM _L4[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_PURPLE}
);
const rgblight_segment_t PROGMEM _L5[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_CYAN}
);
const rgblight_segment_t PROGMEM _L6[] = RGBLIGHT_LAYER_SEGMENTS(
    {0, 1, HSV_CYAN}
);
// Now define the array of layers. Later layers take precedence
const rgblight_segment_t* const PROGMEM my_rgb_layers[] = RGBLIGHT_LAYERS_LIST(
    _L0,
    _L1,
    _L2,
    _L3,
    _L4,
    _L5,
    _L6
);

void keyboard_post_init_user(void) {
    // Enable the LED layers
    rgblight_layers = my_rgb_layers;
}

layer_state_t default_layer_state_set_user(layer_state_t state) {
    rgblight_set_layer_state(0, layer_state_cmp(state, L0));
    return state;
}

layer_state_t layer_state_set_user(layer_state_t state) {
    rgblight_set_layer_state(1, layer_state_cmp(state, L1));
    rgblight_set_layer_state(2, layer_state_cmp(state, L2));
    rgblight_set_layer_state(3, layer_state_cmp(state, L3));
    rgblight_set_layer_state(4, layer_state_cmp(state, L4));
    rgblight_set_layer_state(5, layer_state_cmp(state, L5));
    rgblight_set_layer_state(6, layer_state_cmp(state, L6));
    return state;
}
