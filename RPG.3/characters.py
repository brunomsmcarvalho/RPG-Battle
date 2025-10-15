# characters.py
import random

# ------------------- Classe base Character -------------------
class Character:
    def __init__(self, name, hp, attack, defense, crit_chance, crit_damage, resource_name, resource_max, resource_regen, spellPower, multiplierDamage):
        self.name = name
        self.hp_max = hp
        self.hp = hp
        self.attack = attack
        self.spellPower = spellPower
        self.multiplierDamage = multiplierDamage
        self.defense = defense
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.resource_name = resource_name
        self.resource_max = resource_max
        self.resource = resource_max
        self.resource_regen = resource_regen
        self.is_immune = False
        self.is_feared = 0
        self.abilities = []
        self.combo_points = 0
        self.next_attack_bonus = 1  # garante que sempre exista
        self.just_got_feared = False  # Nova variável para controlar fear recente
        
    def can_act(self):
        if self.is_feared > 0:
            print(f"{self.name} está com medo e não pode agir neste turno!")
            return False
        return True

    def process_fear(self):
        """Processa o efeito de fear no final do turno"""
        if self.just_got_feared:
            # No primeiro turno após receber fear, apenas marca que já foi processado
            self.just_got_feared = False
        elif self.is_feared > 0:
            # Nos turnos seguintes, decrementa o fear
            self.is_feared -= 1
            if self.is_feared == 0:
                print(f"{self.name} superou o medo!")

    def decrement_fear(self):
        """Decrementa o contador de fear no final do turno"""
        if self.is_feared > 0:
            self.is_feared -= 1
            if self.is_feared == 0:
                print(f"{self.name} superou o medo!")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def decrement_cooldowns(self):
        for ability in self.abilities:
            ability.decrement_cooldown()

    def regen_resource(self):
        self.resource += self.resource_regen
        if self.resource > self.resource_max:
            self.resource = self.resource_max
        print(f"{self.name} regenerou {self.resource_regen} {self.resource_name}. Total: {self.resource}")

    def getMultiplierOfDamage(self):
        if self.multiplierDamage == "attack":
            return self.attack*1.5
        elif self.multiplierDamage == "spellPower":
            return self.spellPower*1.5

class Warrior(Character):
    def __init__(self, namePlayer):
        super().__init__(name=namePlayer, hp=200, attack=151, defense=25, crit_chance=100, crit_damage=50, spellPower=0,
                        multiplierDamage="attack",resource_name="Rage", resource_max=100, resource_regen=5)

class Mage(Character):
    def __init__(self, namePlayer):
        super().__init__(name=namePlayer, hp=180, attack=40, defense=5, crit_chance=1, crit_damage=15, spellPower=200,
                        multiplierDamage="spellPower",resource_name="Mana", resource_max=100, resource_regen=5)

class Rogue(Character):
    def __init__(self, namePlayer):
        super().__init__(name=namePlayer, hp=200, attack=151, defense=15, crit_chance=1, crit_damage=15, spellPower=0,
                        multiplierDamage="attack",resource_name="Energy", resource_max=100, resource_regen=5)

class Druid(Character):
    def __init__(self, namePlayer):
        super().__init__(name=namePlayer, hp=200, attack=35, defense=15, crit_chance=1, crit_damage=15, spellPower=151,
                        multiplierDamage="spellPower",resource_name="Mana", resource_max=100, resource_regen=5)

class Hunter(Character):
    def __init__(self, namePlayer):
        super().__init__(name=namePlayer, hp=200, attack=151, defense=10, crit_chance=1, crit_damage=15, spellPower=0,
                        multiplierDamage="attack",resource_name="Mana", resource_max=100, resource_regen=5)