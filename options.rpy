################################################################################
## Essential Options for Temporal Guardian
################################################################################

## Game Info
define config.name = _("Temporal Guardian")
define config.version = "1.0"
define build.name = "TemporalGuardian"

define gui.show_name = True
define gui.about = _("A visual novel about moral choices across time.")

## Audio
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve

## Window
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Defaults
default preferences.text_cps = 40
default preferences.afm_time = 15

## Save directory
define config.save_directory = "TemporalGuardian-1672093210"

## Build configuration
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)

## Developer options
define config.developer = True
define config.rollback_enabled = True
define config.rollback_length = 128

## Console
init python:
    config.console = True