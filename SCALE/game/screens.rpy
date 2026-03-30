screen timeline_status():
    frame:
        xalign 1.0
        yalign 0.0
        xpadding 20
        ypadding 10
        
        vbox:
            text "Timeline Stability: [timeline_stability]%" size 18
            text "People Saved: [people_saved]" size 18
            text "Future Casualties: [future_casualties]" size 18
            if timeline_fractures > 0:
                text "Timeline Fractures: [timeline_fractures]" size 18 color "#ff4444"

screen sacrifice_choice(choice1_text, choice2_text, choice1_label, choice2_label):
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        background "#000000cc"
        
        vbox:
            spacing 30
            
            text "TEMPORAL DECISION REQUIRED" size 24 color "#ff6b6b" xalign 0.5
            text "Choose which timeline to sacrifice:" size 18 xalign 0.5
            
            hbox:
                spacing 50
                xalign 0.5
                
                textbutton choice1_text:
                    action Return(choice1_label)
                    text_size 16
                    xsize 200
                    ysize 100
                    
                textbutton choice2_text:
                    action Return(choice2_label)
                    text_size 16
                    xsize 200
                    ysize 100