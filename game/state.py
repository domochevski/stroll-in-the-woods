import os
import json

class GameState:
    def __init__(self):
        self.turn = 0
        self.current_room = None
        self.enemies = []
        self.map = {}

    def save(self, slot):
        # Save the game state to a file or database
        pass

    def load(self, slot):
        # Load the game state from a file or database
        pass
    def update_room(self, room):
        self.current_room = room

    def update_map(self, map_data):
        self.map = map_data

    def update_enemies(self, enemy):
        self.enemies.append(enemy)

    def update_turn(self):
        self.turn += 1

    def get_state(self):
        return {
            "current_room": self.current_room,
            "inventory": self.inventory,
            "health": self.health,
            "enemies": self.enemies
        }

class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.current_health = 100
        self.items = []
        self.attributes = {
            "strength": 10,
            "agility": 10,
            "intelligence": 10
        }
        self.level = 1
        self.experience = 0
        self.can_save = True
        self.state = GameState()

    def get_player_info(self):
        return {
            "name": self.name,
            "health": self.health,
            "items": self.items,
            "attributes": self.attributes,
            "level": self.level,
            "experience": self.experience,
            "state": self.state.get_state()
        }
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.experience = 0
        self.attributes["strength"] += 2
        self.attributes["agility"] += 2
        self.attributes["intelligence"] += 2
        self.max_health = 100 + (self.level * 10)  # Restore health on level up
        self.current_health = self.max_health

    def take_damage(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def can_save(self):
        return self.can_save

    def set_can_save(self, value):
        self.can_save = value

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        player.take_damage(self.attack_power)

class Room:
    def __init__(self, name, description, size=None, room_type=None, doors={"North": False, "East": False, "South": False, "West": False}):
        self.name = name
        self.size = size
        self.type = room_type
        self.description = description
        self.enemies = []
        self.items = []
        self.doors = doors

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def remove_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def set_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)