# GlosCol-IoT-Project
# 🔐 The Hackbox

> *A physical puzzle box that challenges visitors to "hack" their way in through a series of logic and code challenges — built for festivals, maker fairs, and tech events.*

---

## What Is It?

The Hackbox is a locked wooden or plastic box with a screen, some LEDs, and a secret inside. A sign on the front dares you:

**"This box contains a prize / secret message / trophy. Can you hack your way in?"**

Visitors work through **three sequential puzzle stages**. Solving each one triggers a satisfying LED flash and unlocks the next. Complete all three and a physical latch releases — the box clicks open. Your time is logged on a leaderboard.

Designed for solo players or pairs. No experience required, but a curious mind helps.

---

## How It Works

### The Three Stages

Each stage is a self-contained hacking-themed puzzle. Examples include:

- **Stage 1 — Decode:** Decipher a message encoded in binary, hex, or Caesar cipher
- **Stage 2 — Crack:** Brute-force a short PIN by following logical clues
- **Stage 3 — Exploit:** Spot a deliberate "vulnerability" in a fake login screen and bypass it

Stages are designed to be approachable but not trivial — expected completion time is **3–10 minutes** for a motivated pair.

### Feedback & Flow

| Event | Response |
|---|---|
| Correct answer | Green LED flash, short success tone, next stage loads |
| Wrong answer | Red LED flash, short buzz, try again |
| All three solved | All LEDs flash, relay triggers, latch releases |
| Box opens | Completion time is saved to the leaderboard |

---

## Hardware

| Component | Purpose |
|---|---|
| Raspberry Pi (3B+ or 4) | Main controller — runs all game logic |
| Small touchscreen or monitor | Displays puzzles and UI |
| RGB LEDs | Stage feedback (green = correct, red = wrong) |
| Piezo buzzer | Audio feedback |
| Relay module | Controls the physical latch |
| Electric door latch / solenoid | The actual locking mechanism |
| Wooden or plastic enclosure | The box itself |
| USB keyboard (optional) | For typed puzzle answers |
| Power supply | Powers Pi, screen, relay, and latch |

### Wiring Overview

```
Raspberry Pi GPIO
├── GPIO 17 → LED (Stage 1)
├── GPIO 18 → LED (Stage 2)
├── GPIO 27 → LED (Stage 3)
├── GPIO 22 → Piezo buzzer
└── GPIO 23 → Relay IN → Solenoid latch
```

Exact pin assignments are configurable in `config.py`.

---

## Software

### Stack

- **Python 3** — game logic and GPIO control
- **Pygame** or **Tkinter** — UI rendering on the screen
- **SQLite** — leaderboard storage
- **RPi.GPIO** — hardware control

### Project Structure

```
hackbox/
├── main.py              # Entry point — runs the game loop
├── config.py            # Pin assignments, timing, difficulty settings
├── stages/
│   ├── stage1.py        # Puzzle logic for Stage 1
│   ├── stage2.py        # Puzzle logic for Stage 2
│   └── stage3.py        # Puzzle logic for Stage 3
├── hardware/
│   ├── leds.py          # LED control helpers
│   ├── buzzer.py        # Buzzer patterns
│   └── latch.py         # Relay / latch control
├── leaderboard/
│   ├── leaderboard.py   # Read/write completion times
│   └── scores.db        # SQLite database (auto-created)
├── ui/
│   ├── screen.py        # Display manager
│   └── assets/          # Fonts, images, sound effects
├── tests/
│   └── test_stages.py   # Unit tests for puzzle logic
├── requirements.txt
└── README.md
```

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/hackbox.git
cd hackbox

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

> Requires a Raspberry Pi with GPIO access. Run as root or add your user to the `gpio` group.

### Configuration

Edit `config.py` to adjust:

```python
# GPIO pins
LED_PINS = [17, 18, 27]
BUZZER_PIN = 22
LATCH_PIN = 23

# Timing
LATCH_OPEN_DURATION = 5      # seconds the latch stays open
SUCCESS_FLASH_DURATION = 0.5 # seconds per LED flash

# Gameplay
MAX_ATTEMPTS_PER_STAGE = None  # Set an integer to limit attempts
SHOW_HINTS = True
```

---

## The Leaderboard

Completion times are saved automatically when the box opens. The leaderboard screen displays the top 10 times and can be shown on a secondary monitor or printed at the end of an event.

```
🏆 HACKBOX LEADERBOARD

1. Alice & Bob     —  2:34
2. Mystery Hacker  —  3:11
3. Team Sudo       —  4:02
...
```

Reset between events with:

```bash
python leaderboard/leaderboard.py --reset
```

---

## Designing Your Own Stages

Stages are modular. Each stage file exposes a simple interface:

```python
class Stage:
    def render(self, screen) -> None: ...   # Draw the puzzle UI
    def check(self, answer: str) -> bool:   # Return True if correct
        ...
```

Drop a new file into `stages/` and register it in `main.py`. See `stages/stage1.py` for a worked example.

---

## Event Tips

- **Playtesting:** Run the box with a few volunteers before the event and tune difficulty so most teams can complete it in under 10 minutes.
- **Reset:** The game resets automatically after the box is opened and closed again. No manual intervention needed between players.
- **Power:** Use a proper UPS or battery pack — losing power mid-puzzle is frustrating. A Pi powers on cleanly and resumes the game on boot.
- **Supervision:** Leaving the box unattended is fine, but having someone nearby to help confused visitors dramatically improves the experience.
- **Prize ideas:** USB drives with a fun message, a folded-up certificate, a small trophy, or a QR code to a secret page.

---

## Contributing

Pull requests welcome! Ideas that would make great contributions:

- New puzzle stages (steganography, Morse code, logic gates...)
- A web-based leaderboard dashboard
- Sound effect packs
- 3D-printable enclosure designs
- Network multiplayer / race mode

Please open an issue first to discuss larger changes.

---

## Licence

MIT — hack freely.

---

*Built with curiosity, a soldering iron, and entirely too much coffee.*
