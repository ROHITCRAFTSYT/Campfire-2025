################################################################################
## Essential Screens for Temporal Guardian
################################################################################

## Say screen - displays dialogue
screen say(who, what):
    style_prefix "say"
    
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xfill True
        ysize 200
        
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                xpos 50
                ypos -40
                text who id "who"
        
        text what id "what":
            xpos 50
            ypos 30
            xsize 1100

## Choice screen - displays menu options
screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        for i in items:
            textbutton i.caption:
                action i.action
                xsize 800
                ysize 60
                text_xalign 0.5
                text_yalign 0.5

## Quick menu - in-game controls
screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.98
            spacing 20
            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Menu") action ShowMenu('preferences')

## Main menu
screen main_menu():
    tag menu
    add gui.main_menu_background
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 500
        background Frame("gui/frame.png", 10, 10)
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            if gui.show_name:
                text "[config.name!t]":
                    xalign 0.5
                    size 40
                    color gui.accent_color
                text "[config.version]":
                    xalign 0.5
                    size 20
                    color gui.idle_color
            
            null height 20
            
            textbutton _("Start"):
                action Start()
                xalign 0.5
                xsize 300
                ysize 50
            textbutton _("Load"):
                action ShowMenu("load")
                xalign 0.5
                xsize 300
                ysize 50
            textbutton _("Preferences"):
                action ShowMenu("preferences")
                xalign 0.5
                xsize 300
                ysize 50
            textbutton _("About"):
                action ShowMenu("about")
                xalign 0.5
                xsize 300
                ysize 50
            if renpy.variant("pc"):
                textbutton _("Quit"):
                    action Quit(confirm=False)
                    xalign 0.5
                    xsize 300
                    ysize 50

## Game menu base
screen game_menu(title, scroll=None):
    tag menu
    add gui.game_menu_background
    
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
                use navigation
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            transclude
                else:
                    transclude
    
    textbutton _("Return") style "return_button" action Return()
    label title

## Navigation
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        
        if not main_menu:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Main Menu") action MainMenu()
        
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")

## Save/Load screens
screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    use game_menu(title):
        vbox:
            spacing 20
            
            # Page navigation
            hbox:
                spacing 10
                xalign 0.5
                textbutton _("<") action FilePagePrevious()
                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
            
            # Save slots
            grid 3 2:
                spacing 15
                xalign 0.5
                for i in range(6):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        xsize 250
                        ysize 180
                        
                        vbox:
                            spacing 5
                            add FileScreenshot(slot):
                                xalign 0.5
                                xsize 230
                                ysize 130
                            text FileTime(slot, empty=_("Empty Slot")):
                                xalign 0.5
                                size 14
                            text FileSaveName(slot):
                                xalign 0.5
                                size 12

## Preferences screen
screen preferences():
    tag menu
    use game_menu(_("Preferences")):
        vbox:
            spacing 30
            
            hbox:
                spacing 100
                
                vbox:
                    spacing 20
                    label _("Text Speed") text_size 20
                    bar:
                        value Preference("text speed")
                        xsize 300
                        
                    label _("Auto Speed") text_size 20  
                    bar:
                        value Preference("auto-forward time")
                        xsize 300
                
                vbox:
                    spacing 20
                    label _("Music Volume") text_size 20
                    bar:
                        value Preference("music volume")
                        xsize 300
                        
                    label _("Sound Volume") text_size 20
                    bar:
                        value Preference("sound volume")
                        xsize 300
                        
                    if config.has_voice:
                        label _("Voice Volume") text_size 20
                        bar:
                            value Preference("voice volume")
                            xsize 300
            
            hbox:
                spacing 50
                xalign 0.5
                textbutton _("Fullscreen"):
                    action Preference("display", "fullscreen")
                    xsize 150
                    ysize 40
                textbutton _("Windowed"):
                    action Preference("display", "window")
                    xsize 150
                    ysize 40

## History screen
screen history():
    tag menu
    use game_menu(_("History"), scroll="viewport"):
        for h in _history_list:
            window:
                xfill True
                ysize 100
                background None
                
                hbox:
                    spacing 20
                    if h.who:
                        text h.who:
                            style "history_name"
                            xsize 150
                            text_align 1.0
                    text h.what:
                        style "history_text"
                        xsize 800

## About screen
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]")
            if gui.about:
                text "[gui.about!t]"
            text _("Made with Ren'Py [renpy.version_only].")

## Confirm screen
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text message
            hbox:
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

## Skip indicator
screen skip_indicator():
    zorder 100
    text _("Skipping") xalign 0.98 yalign 0.02

## Notify screen
screen notify(message):
    zorder 100
    text message xalign 0.02 yalign 0.02

################################################################################
## Styles
################################################################################

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background "gui/textbox.png"

style namebox:
    xpos gui.name_xpos
    xsize gui.namebox_width
    ypos gui.name_ypos
    background "gui/namebox.png"

style say_label:
    properties gui.text_properties("name", accent=True)

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width

style choice_vbox:
    xalign 0.5
    ypos 405
    spacing gui.choice_spacing

style choice_button:
    properties gui.button_properties("choice_button")

style choice_button_text:
    properties gui.button_text_properties("choice_button")

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_vbox:
    xalign 1.0
    yalign 1.0
    xoffset -20
    yoffset -20

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style game_menu_outer_frame:
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280

style game_menu_content_frame:
    left_margin 40

style navigation_button:
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0

## Enable quick menu and other overlays
init python:
    config.overlay_screens.append("quick_menu")
    config.character_id_prefixes.append('namebox')

default quick_menu = True
define config.narrator_menu = True