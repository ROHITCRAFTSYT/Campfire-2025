define config.screen_width = 1920
define config.screen_height = 1080

## Transitions used between game menu screens.
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve

## Preference defaults #####################################################

## Controls the default text speed. The default, 0, is infinite, while any
## other number is the number of characters per second to type out.
default preferences.text_cps = 40

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.
default preferences.afm_time = 15

init python:

    build.directory_name = "SCALE-1.0"
    build.executable_name = "SCALE"
    build.include_update = False
    build.itch_project = "txte/temporal-guardian"

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

    