# SCALE — Temporal Guardian

A choice-driven visual novel built with the **Ren'Py** engine. You play as a Temporal Guardian tasked with preventing timeline collapse — but every life you save in the present creates catastrophic ripples in the future.

---

## Story

You are a Temporal Guardian. Reality is fracturing. A series of incidents unfolds before you, each one a direct conflict between personal compassion and utilitarian necessity:

- Save a child from a truck — prevent a future peace negotiator (+2,847 deaths)
- Save a mother from a burning building — prevent a climate scientist (+50,000 casualties)
- Save a scientist from an explosion — erase a breakthrough energy technology
- Prevent a construction accident — fracture the timeline further

Every choice is tracked. Your cumulative decisions lead to one of **5 possible endings**.

---

## Endings

| Ending | Condition |
|--------|-----------|
| **Shattered Time** | Save everyone — reality fractures into a multiverse |
| **Price of Compassion** | Save most — condemn millions in future wars and plagues |
| **Infinite Possibilities** | Accept the chaos — timelines split, free will prevails |
| **The Reset** | Undo all interventions — natural timeline preserved |
| **Eternal Guardian** | Self-sacrifice — the Guardian becomes one with time itself |

---

## Tech Stack

| Component | Details |
|-----------|---------|
| Engine | [Ren'Py](https://www.renpy.org/) (Python-based visual novel framework) |
| Language | Ren'Py Script (.rpy) + embedded Python |
| Resolution | 1920 × 1080 |
| Platforms | Windows, macOS, Linux |
| Audio | MP3 / OGG (voice acting for all characters) |
| Images | PNG / JPG sprites and backgrounds |

---

## Project Structure

```
ren-scaler/
├── SCALE/                     # Main game source
│   ├── game/
│   │   ├── script.rpy         # Core narrative, dialogue, and game logic
│   │   ├── screens.rpy        # UI screens (timeline status, choice modals)
│   │   ├── gui.rpy            # Color themes and UI styling
│   │   ├── options.rpy        # Game settings and build config
│   │   ├── images/            # Character sprites and background scenes
│   │   ├── audio/             # Voice acting (guardian, child, mother, scientist, worker)
│   │   ├── gui/               # GUI asset theme (buttons, bars, dialogs, menus)
│   │   └── tl/                # Localization / translation files
│   └── project.json           # Ren'Py build manifest
└── SCALE-1.0-dists/           # Pre-built platform distributions
    ├── SCALE-1.0-pc.zip
    ├── SCALE-1.0-mac.zip
    └── SCALE-1.0-win.zip
```

---

## Characters

- **Temporal Guardian** — The player character; the last line of defense for timeline integrity
- **Child** — A young life in immediate danger
- **Mother** — A parent whose fate ties to a critical future scientist
- **Scientist** — A researcher on the verge of a world-changing breakthrough
- **Worker** — A laborer caught in a construction site accident

---

## Running the Game

### Play from a Distribution (Recommended)

1. Download the zip for your platform from `SCALE-1.0-dists/`
2. Extract and run the `SCALE` executable

### Run from Source

1. Install the [Ren'Py SDK](https://www.renpy.org/latest.html)
2. Open the Ren'Py launcher and point it to the `SCALE/` directory
3. Click **Launch Project**

---

## Building

Open the Ren'Py launcher with the `SCALE/` project selected, then use **Build Distributions**. Outputs go to `SCALE-1.0-dists/` for Windows, macOS, and Linux.

---

## License

All rights reserved. Game assets, narrative, and code are the property of their respective creators.
