# Game title and version
define config.name = "Temporal Guardian"
define config.version = "1.0"

# Image definitions for characters (supports both PNG and JPG)
image guardian = ConditionSwitch(
    "renpy.loadable('images/guardian.png')", "images/guardian.png",
    "renpy.loadable('images/guardian.jpg')", "images/guardian.jpg",
    "renpy.loadable('guardian.png')", "guardian.png",
    "renpy.loadable('guardian.jpg')", "guardian.jpg",
    True, "guardian.png")

image child = ConditionSwitch(
    "renpy.loadable('images/child.png')", "images/child.png",
    "renpy.loadable('images/child.jpg')", "images/child.jpg",
    "renpy.loadable('child.png')", "child.png",
    "renpy.loadable('child.jpg')", "child.jpg",
    True, "child.png")

image mother = ConditionSwitch(
    "renpy.loadable('images/mother.png')", "images/mother.png",
    "renpy.loadable('images/mother.jpg')", "images/mother.jpg",
    "renpy.loadable('mother.png')", "mother.png",
    "renpy.loadable('mother.jpg')", "mother.jpg",
    True, "mother.png")

image scientist = ConditionSwitch(
    "renpy.loadable('images/scientist.png')", "images/scientist.png",
    "renpy.loadable('images/scientist.jpg')", "images/scientist.jpg",
    "renpy.loadable('scientist.png')", "scientist.png",
    "renpy.loadable('scientist.jpg')", "scientist.jpg",
    True, "scientist.png")

image worker = ConditionSwitch(
    "renpy.loadable('images/worker.png')", "images/worker.png",
    "renpy.loadable('images/worker.jpg')", "images/worker.jpg",
    "renpy.loadable('worker.png')", "worker.png",
    "renpy.loadable('worker.jpg')", "worker.jpg",
    True, "worker.png")

# Background images (supports both PNG and JPG)
image bg_void = ConditionSwitch(
    "renpy.loadable('images/bg_void.png')", "images/bg_void.png",
    "renpy.loadable('images/bg_void.jpg')", "images/bg_void.jpg",
    "renpy.loadable('bg_void.png')", "bg_void.png",
    "renpy.loadable('bg_void.jpg')", "bg_void.jpg",
    True, "#000000")

image bg_city_present = ConditionSwitch(
    "renpy.loadable('images/bg_city_present.png')", "images/bg_city_present.png",
    "renpy.loadable('images/bg_city_present.jpg')", "images/bg_city_present.jpg",
    "renpy.loadable('bg_city_present.png')", "bg_city_present.png",
    "renpy.loadable('bg_city_present.jpg')", "bg_city_present.jpg",
    True, "#2c3e50")

image bg_street = ConditionSwitch(
    "renpy.loadable('images/bg_street.png')", "images/bg_street.png",
    "renpy.loadable('images/bg_street.jpg')", "images/bg_street.jpg",
    "renpy.loadable('bg_street.png')", "bg_street.png",
    "renpy.loadable('bg_street.jpg')", "bg_street.jpg",
    True, "#34495e")

image bg_burning_building = ConditionSwitch(
    "renpy.loadable('images/bg_burning_building.png')", "images/bg_burning_building.png",
    "renpy.loadable('images/bg_burning_building.jpg')", "images/bg_burning_building.jpg",
    "renpy.loadable('bg_burning_building.png')", "bg_burning_building.png",
    "renpy.loadable('bg_burning_building.jpg')", "bg_burning_building.jpg",
    True, "#e74c3c")

image bg_laboratory = ConditionSwitch(
    "renpy.loadable('images/bg_laboratory.png')", "images/bg_laboratory.png",
    "renpy.loadable('images/bg_laboratory.jpg')", "images/bg_laboratory.jpg",
    "renpy.loadable('bg_laboratory.png')", "bg_laboratory.png",
    "renpy.loadable('bg_laboratory.jpg')", "bg_laboratory.jpg",
    True, "#9b59b6")

image bg_construction_site = ConditionSwitch(
    "renpy.loadable('images/bg_construction_site.png')", "images/bg_construction_site.png",
    "renpy.loadable('images/bg_construction_site.jpg')", "images/bg_construction_site.jpg",
    "renpy.loadable('bg_construction_site.png')", "bg_construction_site.png",
    "renpy.loadable('bg_construction_site.jpg')", "bg_construction_site.jpg",
    True, "#2ecc71")

image bg_temporal_nexus = ConditionSwitch(
    "renpy.loadable('images/bg_temporal_nexus.png')", "images/bg_temporal_nexus.png",
    "renpy.loadable('images/bg_temporal_nexus.jpg')", "images/bg_temporal_nexus.jpg",
    "renpy.loadable('bg_temporal_nexus.png')", "bg_temporal_nexus.png",
    "renpy.loadable('bg_temporal_nexus.jpg')", "bg_temporal_nexus.jpg",
    True, "#4a90e2")

image bg_fractured_reality = ConditionSwitch(
    "renpy.loadable('images/bg_fractured_reality.png')", "images/bg_fractured_reality.png",
    "renpy.loadable('images/bg_fractured_reality.jpg')", "images/bg_fractured_reality.jpg",
    "renpy.loadable('bg_fractured_reality.png')", "bg_fractured_reality.png",
    "renpy.loadable('bg_fractured_reality.jpg')", "bg_fractured_reality.jpg",
    True, "#ff6b6b")

image bg_dark_future = ConditionSwitch(
    "renpy.loadable('images/bg_dark_future.png')", "images/bg_dark_future.png",
    "renpy.loadable('images/bg_dark_future.jpg')", "images/bg_dark_future.jpg",
    "renpy.loadable('bg_dark_future.png')", "bg_dark_future.png",
    "renpy.loadable('bg_dark_future.jpg')", "bg_dark_future.jpg",
    True, "#8b0000")

image bg_multiverse = ConditionSwitch(
    "renpy.loadable('images/bg_multiverse.png')", "images/bg_multiverse.png",
    "renpy.loadable('images/bg_multiverse.jpg')", "images/bg_multiverse.jpg",
    "renpy.loadable('bg_multiverse.png')", "bg_multiverse.png",
    "renpy.loadable('bg_multiverse.jpg')", "bg_multiverse.jpg",
    True, "#663399")

image bg_eternal_watch = ConditionSwitch(
    "renpy.loadable('images/bg_eternal_watch.png')", "images/bg_eternal_watch.png",
    "renpy.loadable('images/bg_eternal_watch.jpg')", "images/bg_eternal_watch.jpg",
    "renpy.loadable('bg_eternal_watch.png')", "bg_eternal_watch.png",
    "renpy.loadable('bg_eternal_watch.jpg')", "bg_eternal_watch.jpg",
    True, "#1e3a8a")

# Placeholder images (fallback solid colors if no images found)
image placeholder_character = Solid("#ffffff")
image placeholder_bg = Solid("#000000")

# Characters
define narrator = Character(None, kind=nvl)
define guardian = Character("Guardian", color="#4a90e2")
define system = Character("Temporal System", color="#ff6b6b", what_prefix="> ", what_suffix=" <")
define child = Character("Lost Child", color="#f39c12")
define mother = Character("Sarah Chen", color="#e74c3c")
define scientist = Character("Dr. Martinez", color="#9b59b6")
define worker = Character("Construction Worker", color="#2ecc71")

# Variables to track timeline states and consequences
default timeline_stability = 100
default people_saved = 0
default future_casualties = 0
default timeline_fractures = 0

# Flags for specific choices
default saved_child = False
default saved_mother = False
default saved_scientist = False
default prevented_accident = False

# Future consequence flags
default child_timeline_broken = False
default mother_timeline_broken = False
default scientist_timeline_broken = False
default accident_timeline_broken = False

# ====== SCREENS ======

screen timeline_status():
    frame:
        xalign 1.0
        yalign 0.0
        xpadding 20
        ypadding 10
        
        vbox:
            text "Timeline Stability: [timeline_stability]%%" size 18
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

# ====== MAIN STORY ======

label start:
    show screen timeline_status
    
    scene bg_void
    with fade
    
    system "TEMPORAL GUARDIAN UNIT ACTIVATED"
    system "Timeline stability: 100%%"
    system "Mission: Prevent catastrophic timeline collapse"
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice1.mp3"):
        voice "audio/guardian/voice1.mp3"
    guardian "Another day, another timeline to protect."
    hide guardian
    
    narrator "You are the Temporal Guardian, tasked with maintaining the stability of reality itself. But every life you save creates ripples through time..."
    
    narrator "Your temporal sensors detect multiple crisis points occurring simultaneously across the timeline."
    
    scene bg_city_present
    with dissolve
    
    system "ALERT: Four critical incidents detected"
    system "WARNING: Intervention will cause temporal fractures"
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice2.mp3"):
        voice "audio/guardian/voice2.mp3"
    guardian "Four emergencies, but I can only prevent the worst outcomes by sacrificing others..."
    hide guardian
    
    jump incident_selection

label incident_selection:
    
    narrator "Your temporal display shows four simultaneous crises. You must address each in sequence and decide whether to intervene."
    
    jump child_incident

# ====== INCIDENT: CHILD ======
label child_incident:
    scene bg_street
    with dissolve
    
    narrator "You see a young girl chasing a ball into a busy street. A truck is speeding toward him."
    
    show child at center
    with dissolve
    if renpy.loadable("audio/child/voice1.mp3"):
        voice "audio/child/voice1.mp3"
    child "My ball! I need my ball!"
    hide child
    
    narrator "You could easily save him, but your temporal calculations show the consequences..."
    
    system "TEMPORAL ANALYSIS:"
    system "Saving child will prevent him from becoming a renowned peace negotiator"
    system "Future war casualties: +2,847 deaths in 2089"
    system "Alternative: Let natural timeline proceed"
    
    call screen sacrifice_choice("Save the child now", "Let fate decide", "save_child", "sacrifice_child")
    
    if _return == "save_child":
        $ saved_child = True
        $ people_saved += 1
        $ future_casualties += 2847
        $ timeline_fractures += 1
        $ timeline_stability -= 15
        $ child_timeline_broken = True
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice3.omp3gg"):
            voice "audio/guardian/voice3.mp3"
        guardian "I can't let a child die, no matter the cost."
        hide guardian
        
        narrator "You freeze time and pull the child to safety. The truck passes harmlessly."
        
        show child at center
        with dissolve
        if renpy.loadable("audio/child/voice2.mp3"):
            voice "audio/child/voice2.mp3"
        child "Thank you, mister! You saved me!"
        hide child
        
        system "TIMELINE ALTERED"
        system "Immediate result: 1 life saved"
        system "Future consequence: Peace treaty of 2089 will fail"
        system "Timeline stability decreased"
        
    else:
        $ timeline_stability += 5
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice4.mp3"):
            voice "audio/guardian/voice4.mp3"
        guardian "The greater good... it has to matter more than one life."
        hide guardian
        
        narrator "You watch helplessly as the inevitable unfolds. The child's sacrifice will save thousands in the future."
        
        system "NATURAL TIMELINE PRESERVED"
        system "Future peace negotiations remain intact"
        
    jump mother_incident

# ====== INCIDENT: MOTHER ======
label mother_incident:
    scene bg_burning_building
    with dissolve
    
    narrator "Sarah Chen, a single mother, is trapped on the third floor of a burning apartment building."
    
    show mother at center
    with dissolve
    if renpy.loadable("audio/mother/voice1.mp3"):
        voice "audio/mother/voice1.mp3"
    mother "Help! Please, someone help me! I have a daughter!"
    hide mother
    
    system "TEMPORAL ANALYSIS:"
    system "Subject will die in 3 minutes without intervention"
    system "Saving her prevents her daughter from becoming a climate scientist"
    system "Environmental disaster in 2078: +50,000 casualties"
    system "Alternative: Allow natural timeline"
    
    call screen sacrifice_choice("Save Sarah Chen", "Preserve timeline", "save_mother", "sacrifice_mother")
    
    if _return == "save_mother":
        $ saved_mother = True
        $ people_saved += 1
        $ future_casualties += 50000
        $ timeline_fractures += 1
        $ timeline_stability -= 20
        $ mother_timeline_broken = True
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice5.mp3"):
            voice "audio/guardian/voice5.mp3"
        guardian "A mother's life... I have to try."
        hide guardian
        
        narrator "You manipulate the building's structure, creating an escape route through time and space."
        
        show mother at center
        with dissolve
        if renpy.loadable("audio/mother/voice2.mp3"):
            voice "audio/mother/voice2.mp3"
        mother "I don't understand how, but thank you! I need to find my daughter!"
        hide mother
        
        system "TIMELINE COMPROMISED"
        system "Climate research program derailed"
        system "Environmental protections will fail in 2078"
        
    else:
        $ timeline_stability += 10
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice6.mp3"):
            voice "audio/guardian/voice6.mp3"
        guardian "Her daughter will save more lives than I'm taking today."
        hide guardian
        
        narrator "You turn away as the flames claim another victim for the greater timeline."
        
        system "TIMELINE PRESERVED"
        system "Future environmental research secured"
        
    jump scientist_incident

# ====== INCIDENT: SCIENTIST ======
label scientist_incident:
    scene bg_laboratory
    with dissolve
    
    narrator "Dr. Martinez is about to accidentally trigger a chemical explosion in her research facility."
    
    show scientist at center
    with dissolve
    if renpy.loadable("audio/scientist/voice1.mp3"):
        voice "audio/scientist/voice1.mp3"
    scientist "Just one more calculation... this formula could change everything!"
    hide scientist
    
    system "TEMPORAL ANALYSIS:"
    system "Explosion will kill Dr. Martinez and destroy 20 years of research"
    system "However: Her research leads to biological weapons in 2095"
    system "Preventing explosion causes global pandemic: +500,000 deaths"
    system "Alternative: Allow natural timeline"
    
    call screen sacrifice_choice("Prevent the explosion", "Let research be destroyed", "save_scientist", "sacrifice_scientist")
    
    if _return == "save_scientist":
        $ saved_scientist = True
        $ people_saved += 1
        $ future_casualties += 500000
        $ timeline_fractures += 1
        $ timeline_stability -= 25
        $ scientist_timeline_broken = True
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice7.mp3"):
            voice "audio/guardian/voice7.mp3"
        guardian "Scientific knowledge is too valuable to lose."
        hide guardian
        
        narrator "You subtly adjust the chemical mixture, preventing the explosive reaction."
        
        show scientist at center
        with dissolve
        if renpy.loadable("audio/scientist/voice2.mp3"):
            voice "audio/scientist/voice2.mp3"
        scientist "Strange... my calculations were off. But now I can continue my research!"
        hide scientist
        
        system "CATASTROPHIC TIMELINE BREACH"
        system "Biological weapons research preserved"
        system "Global pandemic probability: 89%%"
        
    else:
        $ timeline_stability += 15
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice8.mp3"):
            voice "audio/guardian/voice8.mp3"
        guardian "Some knowledge is too dangerous to preserve."
        hide guardian
        
        narrator "The explosion destroys decades of research, but humanity's future is safer."
        
        system "DANGEROUS RESEARCH ELIMINATED"
        system "Pandemic timeline prevented"
        
    jump construction_incident

# ====== INCIDENT: CONSTRUCTION ======
label construction_incident:
    scene bg_construction_site
    with dissolve
    
    narrator "A construction crane is about to collapse, threatening to kill five workers below."
    
    show worker at center
    with dissolve
    if renpy.loadable("audio/worker/voice1.mp3"):
        voice "audio/worker/voice1.mp3"
    worker "Hey, did you hear that creaking sound?"
    hide worker
    
    system "TEMPORAL ANALYSIS:"
    system "5 workers will die without intervention"
    system "However: One worker's son becomes a dictator in 2087"
    system "Authoritarian regime casualties: +1,000,000 deaths"
    system "Alternative: Allow natural timeline"
    
    call screen sacrifice_choice("Save the workers", "Preserve timeline", "prevent_accident", "allow_accident")
    
    if _return == "prevent_accident":
        $ prevented_accident = True
        $ people_saved += 5
        $ future_casualties += 1000000
        $ timeline_fractures += 2
        $ timeline_stability -= 30
        $ accident_timeline_broken = True
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice9.mp3"):
            voice "audio/guardian/voice9.mp3"
        guardian "Five lives... I can't let them die."
        hide guardian
        
        narrator "You reinforce the crane's structure through temporal manipulation."
        
        show worker at center
        with dissolve
        if renpy.loadable("audio/worker/voice2.mp3"):
            voice "audio/worker/voice2.mp3"
        worker "Whew! That was close. Thanks to whoever's watching over us!"
        hide worker
        
        system "MAJOR TIMELINE DISRUPTION"
        system "Future dictator's lineage preserved"
        system "Democratic institutions will collapse in 2087"
        
    else:
        $ timeline_stability += 20
        
        show guardian at center
        with dissolve
        if renpy.loadable("audio/guardian/voice10.mp3"):
            voice "audio/guardian/voice10.mp3"
        guardian "The hardest choices require the strongest wills."
        hide guardian
        
        narrator "Five good people die today so that millions might live free tomorrow."
        
        system "AUTHORITARIAN TIMELINE PREVENTED"
        system "Democratic future secured"
        
    jump next_incident

label next_incident:
    if people_saved == 0:
        jump ending_purist
    elif timeline_fractures >= 3:
        jump ending_chaos
    elif future_casualties >= 1000000:
        jump ending_catastrophe
    else:
        jump final_choice

# ====== FINAL CHOICE ======
label final_choice:
    scene bg_temporal_nexus
    with dissolve
    
    system "TEMPORAL CONVERGENCE POINT REACHED"
    system "Final stabilization required"
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice11.mp3"):
        voice "audio/guardian/voice11.mp3"
    guardian "I've made my choices, but I can see the timeline fracturing. There's one last decision to make."
    hide guardian
    
    narrator "Your actions have created temporal instabilities. You have one final choice to make as the Guardian."
    
    system "OPTION 1: Accept timeline fractures - embrace chaos but preserve free will"
    system "OPTION 2: Reset timeline - undo all changes, return to natural flow"
    system "OPTION 3: Sacrifice yourself - become part of the timeline to stabilize it"
    
    menu:
        "Embrace the chaos - let the fractured timeline stand":
            jump ending_chaos_accepted
            
        "Reset everything - undo all my interventions":
            jump ending_reset
            
        "Sacrifice myself to stabilize the timeline":
            jump ending_sacrifice

# ====== ENDINGS ======

label ending_purist:
    hide screen timeline_status
    scene bg_temporal_nexus
    with dissolve
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice12.mp3"):
        voice "audio/guardian/voice12.mp3"
    guardian "I saved no one today, but the timeline remains intact."
    hide guardian
    
    system "MISSION STATUS: SUCCESSFUL"
    system "Timeline stability: [timeline_stability]%%"
    system "Future casualties prevented: [future_casualties * -1]"
    
    narrator "You chose the path of ultimate sacrifice - allowing tragedy to unfold to prevent greater catastrophes."
    
    narrator "The timeline flows as it should. Millions live because of the few who died."
    
    narrator "You are the perfect Guardian, but the weight of inaction haunts you across all timelines."
    
    centered "{color=#4a90e2}ENDING: THE PERFECT GUARDIAN{/color}"
    centered "You preserved the timeline at the cost of your humanity."
    
    return

label ending_chaos:
    hide screen timeline_status
    scene bg_fractured_reality
    with dissolve
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice13.mp3"):
        voice "audio/guardian/voice13.mp3"
    guardian "I tried to save everyone, but I've broken everything."
    hide guardian
    
    system "CRITICAL ERROR: TIMELINE COLLAPSE IMMINENT"
    system "Fractures detected: [timeline_fractures]"
    system "Reality stability: [timeline_stability]%%"
    
    narrator "Your interventions have shattered the timeline into countless fragments."
    
    narrator "In trying to save everyone, you've doomed everyone to an uncertain existence across infinite realities."
    
    narrator "Some timelines flourish, others burn, but none follow the natural order."
    
    centered "{color=#ff6b6b}ENDING: SHATTERED TIME{/color}"
    centered "Your compassion broke reality itself."
    
    return

label ending_catastrophe:
    hide screen timeline_status
    scene bg_dark_future
    with dissolve
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice14.mp3"):
        voice "audio/guardian/voice14.mp3"
    guardian "I saved lives today, but at what cost?"
    hide guardian
    
    system "TEMPORAL ANALYSIS COMPLETE"
    system "Future casualties: [future_casualties]"
    system "Timeline stability: [timeline_stability]%%"
    
    narrator "Your choices saved [people_saved] people in the present, but condemned millions in the future."
    
    narrator "Wars rage, plagues spread, and tyrants rise because of your interventions."
    
    narrator "The faces of those you saved smile at you from across time, unaware of the price paid for their lives."
    
    centered "{color=#f39c12}ENDING: THE PRICE OF COMPASSION{/color}"
    centered "You chose the present over the future."
    
    return

label ending_chaos_accepted:
    hide screen timeline_status
    scene bg_multiverse
    with dissolve
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice15.mp3"):
        voice "audio/guardian/voice15.mp3"
    guardian "Let the timeline fracture. At least everyone gets a chance to live."
    hide guardian
    
    system "TIMELINE FRACTURES ACCEPTED"
    system "Multiverse stabilization initiated"
    
    narrator "Reality splits into infinite possibilities. In some timelines, your saved individuals become heroes. In others, villains."
    
    narrator "You've given up control for the chance that free will might find a better way."
    
    narrator "The future is uncertain, but at least it exists in all its chaotic potential."
    
    centered "{color=#9b59b6}ENDING: INFINITE POSSIBILITIES{/color}"
    centered "You chose chaos over certainty."
    
    return

label ending_reset:
    hide screen timeline_status
    scene bg_void
    with dissolve
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice16.mp3"):
        voice "audio/guardian/voice16.mp3"
    guardian "I'll undo it all. Let fate decide who lives and dies."
    hide guardian
    
    system "INITIATING TEMPORAL RESET"
    system "All interventions being reversed"
    
    narrator "Time flows backward as you undo every choice, every intervention."
    
    narrator "The child falls to the truck. The mother burns. The scientist explodes. The workers are crushed."
    
    narrator "But the timeline heals. The future unfolds as it should have."
    
    narrator "You remember everything, but history remembers nothing of your choices."
    
    centered "{color=#2ecc71}ENDING: THE RESET{/color}"
    centered "You chose to let fate decide."
    
    return

label ending_sacrifice:
    hide screen timeline_status
    scene bg_eternal_watch
    with dissolve
    
    show guardian at center
    with dissolve
    if renpy.loadable("audio/guardian/voice17.mp3"):
        voice "audio/guardian/voice17.mp3"
    guardian "If my existence can stabilize the timeline, then so be it."
    hide guardian
    
    system "GUARDIAN INTEGRATION PROTOCOL INITIATED"
    system "Becoming one with the temporal flow"
    
    narrator "You dissolve into the timeline itself, becoming part of the fabric of reality."
    
    narrator "Your consciousness spreads across all moments, stabilizing the fractures you created."
    
    narrator "Those you saved live on, their future consequences balanced by your eternal vigilance."
    
    narrator "You are no longer the Guardian of time - you ARE time itself."
    
    centered "{color=#4a90e2}ENDING: ETERNAL GUARDIAN{/color}"
    centered "You became the sacrifice the timeline needed."
    
    return