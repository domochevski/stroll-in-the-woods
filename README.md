# stroll-in-the-woods
# Infinite Text Adventure (CLI, Python)


An **infinite text adventure game** built in Python for the command line. Explore procedurally generated rooms, battle monsters, collect treasure, and manage your character’s abilities and inventory. Includes preset narrative beats with the option to later integrate an AI-powered Dungeon Master.


## ✨ Features (MVP)
- Procedurally generated rooms with deterministic seeding.
- Character stats: health, abilities, inventory, gold, equipment.
- Command parser with simple verbs: `go`, `look`, `take`, `drop`, `use`, `equip`, `stats`, `inv`, `save`, `load`, `quit`.
- Combat with monsters (turn-based, basic AI, loot tables).
- Multiple save slots stored as JSON.
- Narrative renderer with preset room descriptions and flavor text.


## 🚧 Planned Stretch Goals
- Quests and NPCs.
- Traveling merchants and simple economy.
- Boss rooms every N levels.
- ASCII map command.
- Optional AI-based Dungeon Master for dynamic scene descriptions.


## 📂 Project Structure
```
project_root/
├── game/ # core systems: state, parser, combat, inventory, world
├── content/ # JSON/CSV for rooms, monsters, items, adjectives, verbs
├── saves/ # save game slots (slot1.json, slot2.json, ...)
├── docs/ # design docs, planning notes
└── README.md
```


## 🎮 How to Run
```bash
python main.py
```


## 🧑‍💻 Development Roadmap
- **Day 1:** Project scaffolding, game state, command loop, content templates.
- **Day 2:** Movement system, room generation, hazards, inventory.
- **Day 3:** Combat system, monsters, loot, balancing.
- **Day 4:** Save/load, narrative integration, UX polish, AI DM stub.


## 🧪 Testing
Planned tests:
- Deterministic room generation given seeds.
- Save/load round-trip.
- Combat math within expected bounds.
- Parser recovers from invalid inputs.


## 📜 License
Unlicensed
