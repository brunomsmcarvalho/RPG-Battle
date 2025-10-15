from habilities import Hability
from characters import Warrior, Mage, Rogue, Druid, Hunter

def add_abilities(character):
    critDamag = character.crit_damage

    if isinstance(character, Warrior):
        abilities = [
            Hability("Quick Strike", 1, 4, 35, 10, accuracy=0.95, criticalDamage=critDamag,
                     description="Um ataque rápido corpo a corpo que causa 4 + Attack - Defense de dano. Chance de crítico: 10%."),
            Hability("Powerful Charge", 3, 6, 35, 25, accuracy=0.9, criticalDamage=critDamag,
                     description="Avança contra o inimigo causando 6 + Attack - Defense de dano. Chance de crítico: 15%."),
            Hability("Battle Cry", 5, 0, 0, 20, isDefensive=True, giveImmunity=True, criticalDamage=critDamag,
                     description="Grito de guerra que concede imunidade a controle por 1 round."),
            Hability("Iron Wall", 6, 0, 0, 25, isDefensive=True, giveImmunity=True, criticalDamage=critDamag,
                     description="Bloqueia completamente o próximo ataque recebido."),
            Hability("Warrior's Fear", 6, 0, 0, 25, isCroud=True, criticalDamage=critDamag,
                     description="Intimida o inimigo, fazendo-o perder o próximo turno.")
        ]
    elif isinstance(character, Mage):
        abilities = [
            Hability("Fireball", 1, 5, 35, 20, accuracy=0.9, criticalDamage=critDamag,
                     description="Lança uma bola de fogo que causa 5 + Attack - Defense de dano. Chance de crítico: 15%."),
            Hability("Arcane Explosion", 4, 7, 35, 35, accuracy=0.85, criticalDamage=critDamag,
                     description="Explosão arcana que causa 7 + Attack - Defense de dano. Chance de crítico: 25%."),
            Hability("Arcane Focus", 5, 0, 0, 30, criticalDamage=critDamag,
                     description="Aumenta o dano do próximo ataque em 20%."),
            Hability("Magic Shield", 6, 0, 0, 25, isDefensive=True, giveImmunity=True, criticalDamage=critDamag,
                     description="Cria um escudo que anula o próximo ataque recebido."),
            Hability("Arcane Paralysis", 6, 0, 0, 25, isCroud=True, criticalDamage=critDamag,
                     description="Paralisa o inimigo, impedindo-o de agir por 1 round.")
        ]
    elif isinstance(character, Rogue):
        abilities = [
            Hability("Stab", 1, 5, 35, 10, accuracy=0.95, criticalDamage=critDamag,
                     description="Golpe rápido que causa 5 + Attack - Defense de dano. Chance de crítico: 20%."),
            Hability("Surprise Attack", 3, 7, 35, 25, accuracy=0.9, criticalDamage=critDamag,
                     description="Ataque sorrateiro que causa 7 + Attack - Defense de dano. Chance de crítico: 25%."),
            Hability("Frenzy", 5, 0, 0, 20, criticalDamage=critDamag,
                     description="Aumenta o dano dos próximos dois ataques em 10%."),
            Hability("Agile Dodge", 5, 0, 0, 10, isDefensive=True, giveImmunity=True, criticalDamage=critDamag,
                     description="Esquiva o próximo ataque, tornando-se imune por 1 round."),
            Hability("Paralyzing Poison", 6, 0, 0, 20, isCroud=True, criticalDamage=critDamag,
                     description="Envenena o inimigo, impedindo-o de agir por 1 round.")
        ]
    elif isinstance(character, Druid):
        abilities = [
            Hability("Nature's Claws", 1, 4, 35, 10, accuracy=0.9, criticalDamage=critDamag,
                     description="Golpe natural que causa 4 + Attack - Defense de dano. Chance de crítico: 15%."),
            Hability("Wild Roar", 3, 6, 35, 20, accuracy=0.85, criticalDamage=critDamag,
                     description="Um rugido que causa 6 + Attack - Defense de dano."),
            Hability("Nature's Blessing", 5, 0, 0, 25, isHealing=True, healAmount=25, criticalDamage=critDamag,
                     description="Cura 25 + (Attack × 0.2) de HP."),
            Hability("Natural Barrier", 6, 0, 0, 25, isDefensive=True, giveImmunity=True, criticalDamage=critDamag,
                     description="Cria uma barreira natural que absorve o próximo ataque."),
            Hability("Forest Fear", 6, 0, 0, 25, isCroud=True,
                     description="Raízes prendem o inimigo, impedindo-o de agir por 1 round.")
        ]
    elif isinstance(character, Hunter):
        abilities = [
            Hability("Quick Shot", 1, 3, 35, 10, accuracy=0.95, criticalDamage=critDamag,
                     description="Dispara uma flecha rápida que causa 3 + Attack - Defense de dano."),
            Hability("Precise Shot", 3, 6, 35, 15, accuracy=0.9, criticalDamage=critDamag,
                     description="Disparo preciso que causa 6 + Attack - Defense de dano. Chance de crítico: 20%."),
            Hability("Hunter's Focus", 4, 0, 0, 15, criticalDamage=critDamag,
                     description="Aumenta a chance de crítico do próximo ataque em 15%."),
            Hability("Hideout", 5, 0, 0, 20, isDefensive=True, giveImmunity=True, criticalDamage=critDamag,
                     description="Esconde-se e evita o próximo ataque recebido."),
            Hability("Stunning Shot", 6, 0, 0, 20, isCroud=True, criticalDamage=critDamag,
                     description="Disparo que atordoa o inimigo por 1 round.")
        ]
    character.abilities.extend(abilities)
    return character