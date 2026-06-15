# GlosCol-IoT-Project
# 🔐 The Hackbox

> *A physical puzzle box that challenges visitors to "hack" their way in through a series of logic and code challenges built for festivals, maker fairs, and tech events.*

---

## What Is It?

The Hackbox is a locked wooden or plastic box with a screen, some LEDs, and a secret inside. A sign on the front dares you:

**"This box contains a prize / secret message / trophy. Can you hack your way in?"**

Visitors work through **three sequential puzzle stages**. Solving each one triggers a satisfying LED flash and unlocks the next. Complete all three and a physical latch releases and the box clicks open. Your time is logged on a leaderboard.

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

