from time import sleep
from characters import Warrior, Mage, Rogue, Druid, Hunter
import random
import os
from abilities_setup import add_abilities

# ------------------- Funções auxiliares -------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_class(name):
    classes = {
        "1": Warrior, 
        "2": Mage, 
        "3": Rogue, 
        "4": Druid, 
        "5": Hunter,
    }

    while True:
        print()
        print("╔══════════════════════════════════════╗")
        print("║       👤 SELECIONE SUA CLASSE        ║")
        print("╠══════════════════════════════════════╣")
        print("║                                      ║")
        print("║   1. 🗡️  - WARRIOR                    ║")
        print("║   2. 🔮 - MAGE                       ║")
        print("║   3. 🗡️  - ROGUE                      ║")
        print("║   4. ⛪ - DRUID                      ║")
        print("║   5. 🏹 - HUNTER                     ║")
        print("║                                      ║")
        print("╚══════════════════════════════════════╝")
        print()
        print("\033[95mDigite 'help' para consultar as habilidades.\n\033[0m")
        choice = input("👤 = ").lower().strip()
        if choice == "help":
            show_help()
            clear_screen()
            continue
        if choice in classes:
            return classes[choice](name)
        print("Escolha inválida!")

def choose_player_ability(player):
    print(f"\n{player.name}, escolha sua habilidade:")
    print("0. Passar a vez")
    for idx, ability in enumerate(player.abilities):
        status = f"(CD: {ability.timeCooldown})" if ability.timeCooldown > 0 else ""
        print(f"{idx+1}. {ability.nameHability} {status}  - Cost: {ability.costResource} {player.resource_name}")

    while True:
        choice = input("\nNúmero da habilidade: ").lower().strip()
        if choice == "help":
            show_help()
            continue
        if choice == "0":
            print(f"{player.name} decidiu passar a vez.")
            return None
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(player.abilities):
                ability = player.abilities[choice]
                if player.resource < ability.costResource:
                    print(f"Você não tem {player.resource_name} suficiente para usar {ability.nameHability}!")
                    continue
                return ability
        except ValueError:
            pass
        print("Escolha inválida! Digite o número ou 'help'.")

def get_cooldowns(character, max_abilities=5):
    cds = [ab.timeCooldown for ab in character.abilities]
    cds += [0] * (max_abilities - len(cds))
    return cds

def choose_enemy_ability(enemy):
    """Escolhe uma habilidade pronta do inimigo ou passa a vez."""
    ready_abilities = [a for a in enemy.abilities if a.is_ready() and a.costResource <= enemy.resource]
    offensive_abilities = [a for a in ready_abilities if not a.isDefensive and not a.isCroud and not a.isHealing]
    if ready_abilities and random.random() < 0.2:
        print(f"{enemy.name} decidiu passar a vez!")
        return None
    if offensive_abilities:
        return random.choice(offensive_abilities)  # Prioriza ofensivas
    elif ready_abilities:
        return random.choice(ready_abilities)
    print(f"{enemy.name} não tem habilidades prontas e passa a vez.")
    return None

def random_enemy():
    """Cria um inimigo aleatório (classe + nome)."""
    enemy_names = ["Merlin", "Sylvanas", "Ragnaros", "Illidan", "Jaina"]
    enemy_classes = [Warrior, Mage, Rogue, Druid, Hunter]
    idx = random.randrange(len(enemy_classes))
    name = random.choice(enemy_names)
    return enemy_classes[idx](name)

# ------------------- GUIA DE HABILIDADES -------------------
def show_help():
    clear_screen()
    print("╔══════════════════════════════╗")
    print("║     📜 GUIA DE HABILIDADES   ║")
    print("╚══════════════════════════════╝\n")
    classes = [Warrior, Mage, Rogue, Druid, Hunter]
    for cls in classes:
        # Criar um personagem temporário para acessar as habilidades
        temp_char = cls("Temp")
        add_abilities(temp_char)
        print(f"\n🧭 {cls.__name__.upper()}")
        print("-" * (len(cls.__name__) + 5))
        for ability in temp_char.abilities:
            tipo = "Ofensiva"
            if ability.isDefensive:
                tipo = "Defensiva"
            elif ability.isCroud:
                tipo = "Controle"
            elif ability.isHealing:
                tipo = "Cura"
            print(f"• {ability.nameHability} [{tipo}]")
            print(f"   Cooldown: {ability.maxCooldown} rounds | Custo: {ability.costResource}")
            print(f"   → {ability.description}\n")
    input("\nPressione ENTER para voltar ao jogo...")

# ------------------- Sistema principal -------------------
combat_log = []
clear_screen()
print("╔══════════════════════════════╗")
print("║   🎮 DUNGEONS OF PYTHON 🎮   ║")
print("╚══════════════════════════════╝")
print()

player1 = choose_class(input("╔════════════════════════════════════╗\n"
                             "║     👤 NOME DO PERSONAGEM          ║\n"
                             "╚════════════════════════════════════╝\n"
                             "👤 = "))

enemy = random_enemy()
add_abilities(player1)
add_abilities(enemy)

round_number = 1
while player1.hp > 0 and enemy.hp > 0:
    clear_screen()
    print("=" * 50)
    print(f"RONDA {round_number}")
    print("=" * 50)
    print(f"{player1.name} HP: {player1.hp:.1f}/{player1.hp_max} | {player1.resource_name}: {player1.resource}/{player1.resource_max}")
    print(f"{enemy.name} ({enemy.__class__.__name__}) HP: {enemy.hp:.1f}/{enemy.hp_max} | {enemy.resource_name}: {enemy.resource}/{enemy.resource_max}")
    print("\n")

    # Log do round anterior
    if combat_log:
        for entry in combat_log:
            print(entry)
        print("\n")
        combat_log.clear()
        

    # Turno do player1
    if player1.can_act():
        ability = choose_player_ability(player1)
        if ability is None:
            combat_log.append(f"{player1.name} passou a vez.")
        else:
            damage, critical_message = ability.use(player1, enemy)
            if damage > 0:
                combat_log.append(f"{player1.name} usou {ability.nameHability}!")
                if critical_message != None:  # Se houve crítico, adiciona ao log
                    combat_log.append(critical_message)
                combat_log.append(f"{enemy.name} recebeu {damage:.1f} de dano! HP restante: {enemy.hp:.1f}")
            else:
                combat_log.append(f"{player1.name} usou {ability.nameHability}!")
    else:
        combat_log.append(f"{player1.name} está com medo e não pode atacar!")

    # Turno do inimigo 
    if enemy.can_act():
        ability = choose_enemy_ability(enemy)
        if ability:
            damage, critical_message = ability.use(enemy, player1)
            if damage > 0:
                combat_log.append(f"{enemy.name} usou {ability.nameHability}!")
                if critical_message != None:  # Se houve crítico, adiciona ao log
                    combat_log.append(critical_message)
                combat_log.append(f"{player1.name} recebeu {damage:.1f} de dano! HP restante: {player1.hp:.1f}")
            else:
                combat_log.append(f"{enemy.name} usou {ability.nameHability}!")
        else:
            combat_log.append(f"{enemy.name} passou a vez.")
    else:
        combat_log.append(f"{enemy.name} está com medo e não pode atacar!")
   
    # Decrementa o fear de ambos os personagens no final da ronda
    player1.decrement_fear()
    enemy.decrement_fear()

    # Atualização de cooldowns e recursos
    for char in [player1, enemy]:
        char.decrement_cooldowns()
        char.regen_resource()
        if char.resource < 0:
            char.resource = 0
        combat_log.append(f"{char.name} agora tem {char.resource}/{char.resource_max} {char.resource_name}.")

    round_number += 1

# Resultado final
print("=" * 50)
if player1.hp <= 0 and enemy.hp <= 0:
    print("\nAmbos caíram em combate! É um empate!")
elif player1.hp <= 0:
    print(f"\n{player1.name} foi derrotado!")
else:
    print(f"\n{enemy.name} foi derrotado!")
print("=" * 50)