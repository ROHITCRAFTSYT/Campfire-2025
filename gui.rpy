################################################################################
## Essential GUI Configuration for Temporal Guardian
################################################################################

init offset = -1

## Colors
define gui.accent_color = '#4a90e2'
define gui.idle_color = '#cccccc'
define gui.hover_color = '#66a3ff'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#8888887f'
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

## Fonts
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans-Bold.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

## Font Sizes
define gui.text_size = 22
define gui.name_text_size = 30
define gui.interface_text_size = 22
define gui.label_text_size = 24
define gui.title_text_size = 50

## Backgrounds
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## Dialogue
define gui.textbox_height = 185
define gui.textbox_yalign = 1.0
define gui.name_xpos = 240
define gui.name_ypos = 0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50
define gui.dialogue_width = 744
define gui.dialogue_text_xalign = 0.0

## Buttons
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

## Choices
define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#cccccc'
define gui.choice_button_text_hover_color = '#ffffff'
define gui.choice_button_text_insensitive_color = '#444444'

## Save slots
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 10
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_color
define config.thumbnail_width = 256
define config.thumbnail_height = 144
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

## Quick buttons
define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_color
define gui.quick_button_text_selected_color = gui.accent_color

## Navigation buttons
define gui.navigation_button_width = 250
define gui.navigation_button_borders = Borders(4, 4, 4, 4)
define gui.navigation_button_text_idle_color = gui.idle_color
define gui.navigation_button_text_hover_color = gui.hover_color
define gui.navigation_button_text_selected_color = gui.selected_color
define gui.navigation_button_text_insensitive_color = gui.insensitive_color

## Frames
define gui.frame_borders = Borders(4, 4, 4, 4)
define gui.frame_tile = False

## Bars and sliders
define gui.bar_size = 25
define gui.bar_tile = False
define gui.bar_borders = Borders(4, 4, 4, 4)

## Scrollbars  
define gui.scrollbar_size = 12
define gui.scrollbar_tile = False
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.unscrollable = "hide"

## Layout
define gui.navigation_xpos = 40
define gui.choice_spacing = 22
define gui.navigation_spacing = 4
define gui.main_menu_text_xalign = 1.0

## History
define config.history_length = 250
define gui.history_height = 140

## Language
define gui.language = "unicode"