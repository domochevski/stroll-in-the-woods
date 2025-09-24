# TASKTODO – Infinite Text Adventure (Python, CLI)


This file tracks implementation steps, features, and polish tasks for the project. Organized roughly in day/hour blocks (32h plan). Check off as you progress.


---


## ✅ Day 1 – Foundations
- [x] Set up repo, `README.md`, `TASKTODO.md`, and project folders (`game/`, `content/`, `saves/`, `docs/`).
- [ ] Define game state structure (player, inventory, rooms, RNG seed, difficulty, etc.).
- [ ] Draft constants (HP, damage, abilities).
- [ ] Implement command loop skeleton with stubs for commands.
- [ ] Write initial room/monster/item templates in `content/`.
- [ ] Plan procedural generation rules (deterministic seed + coords).
- [ ] Decide save/load format (JSON with version + rng seed).
- [ ] Write narrative template placeholders.


## ✅ Day 2 – World & Movement
- [ ] Implement core loop with `look`, `go`, and room rendering.
- [ ] Define coordinate system and exit generation.
- [ ] Create room cache (LRU ~100 rooms).
- [ ] Add hazards & interactables (locked door, trap, container).
- [ ] Add monsters/loot placement logic (chance, scaling).
- [ ] Implement inspect, take/drop, inventory view.
- [ ] MVP Checkpoint: walk between rooms, see items, manage inv.


## ✅ Day 3 – Combat & Items
- [ ] Implement turn-based combat system (attack, use item, flee).
- [ ] Add monster AI tiers (basic + defensive behavior).
- [ ] Add simple status effects (bleed, stun, buff).
- [ ] Define consumables & equipment slots.
- [ ] Implement loot tables (weighted rarity).
- [ ] Add player progression system (XP/level or milestone buffs).
- [ ] Balance pass (TTK ~2–4 turns trash, 6–10 elites).
- [ ] Combat log polish (ASCII symbols, examine command).


## ✅ Day 4 – Saves, Narrative & Polish
- [ ] Implement save/load with multiple slots.
- [ ] Validate saves, handle versioning and corruption.
- [ ] Add preset narrative beats (contextual events).
- [ ] Add procedural text flavoring (adjectives, buffers).
- [ ] Implement help, settings (verbosity, difficulty), history.
- [ ] Testing sweep (deterministic seeds, combat math, parser errors).
- [ ] Package docs: update README, add CHANGELOG.
- [ ] Stub for AI DM (`DescribeScene(state)`).


---


## 🌟 Stretch Goals
- [ ] Quests system.
- [ ] NPC companions.
- [ ] Traveling merchant + economy.
- [ ] Boss encounters.
- [ ] ASCII map command.
- [ ] Achievements system.


---


## 🧪 Testing ToDo
- [ ] Deterministic generation reproducible with same seed.
- [ ] Save/load roundtrip works.
- [ ] Combat math: bounds checked.
- [ ] Parser handles invalid input gracefully.