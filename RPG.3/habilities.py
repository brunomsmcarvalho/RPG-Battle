import random

class Hability:
    def __init__(self, nameHability, cooldown, baseDamage, chanceCritical, costResource,
                 criticalDamage=150, isDefensive=False, isCroud=False,
                 giveImmunity=False, isHealing=False, healAmount=0, accuracy=1.0, description=""):
        self.nameHability = nameHability
        self.baseDamage = baseDamage
        self.chanceCritical = chanceCritical      # ex: 0.25 para 25%
        self.criticalDamage = criticalDamage      # ex: 150 para 150% (1.5x)
        self.costResource = costResource
        self.isDefensive = isDefensive
        self.maxCooldown = cooldown
        self.timeCooldown = 0
        self.isCroud = isCroud
        self.giveImmunity = giveImmunity
        self.isHealing = isHealing
        self.healAmount = healAmount
        self.accuracy = accuracy
        self.description = description  # Descrição da habilidade

    def is_ready(self):
        return self.timeCooldown == 0

    def put_on_cooldown(self):
        self.timeCooldown = self.maxCooldown

    def decrement_cooldown(self):
        if self.timeCooldown > 0:
            self.timeCooldown -= 1
    
    def remove_cc(self):
        """Remove efeitos de controle de multidão"""
        if self.is_feared > 0:
            self.is_feared = 0

    def critical_strike(self, damage):
        """Estilo WoW: crit_chance define probabilidade, crit_damage é multiplicador percentual"""
        isCritical = random.random() * 100
        critical_message = ""  # Mensagem vazia por padrão
    
        if isCritical < self.chanceCritical:
            critical_message = "💥 !!!CRITICAL!!!"
            damage *= (self.criticalDamage / 100)
    
        return round(damage, 1), critical_message  # Retorna tanto o dano quanto a mensagem

    def use(self, caster, target):
        if not self.is_ready():
            print(f"{self.nameHability} ainda está em cooldown por {self.timeCooldown} round(s).")
            return 0, ""

        if caster.resource < self.costResource:
            print(f"{caster.name} não tem {caster.resource_name} suficiente para usar {self.nameHability}! (Required: {self.costResource}, Available: {caster.resource})")
            return 0, ""

        # Deduzir recurso
        caster.resource -= self.costResource
        if caster.resource < 0:
            caster.resource = 0

        # Exibir descrição da habilidade
        print(f"\n{caster.name} usa {self.nameHability}! → {self.description or 'Descrição não encontrada.'}")

        if random.random() > self.accuracy:
            print(f"{caster.name} tentou usar {self.nameHability}, mas errou!")
            self.put_on_cooldown()
            return 0, ""

        # Habilidade defensiva
        if self.isDefensive and self.giveImmunity:
            caster.is_immune = True
            print(f"{caster.name} está imune ao próximo ataque!")
            self.put_on_cooldown()
            return 0, ""

        # Habilidade de cura
        if self.isHealing:
            heal = self.healAmount + (caster.attack * 0.2)
            caster.hp = min(caster.hp + heal, caster.hp_max)
            print(f"{caster.name} curou {heal:.1f} HP! HP atual: {caster.hp:.1f}")
            self.put_on_cooldown()
            return -heal, ""

        # Habilidade de controle
        if self.isCroud:
            print(f"{target.name} foi afetado por {self.nameHability} e não pode agir por 1 round!")
            target.is_feared = 1
            target.just_got_feared = True
            self.put_on_cooldown()
            return 0, ""

        # Verificar imunidade do alvo
        if target.is_immune:
            print(f"{target.name} estava protegido! Nenhum dano recebido.")
            target.is_immune = False
            self.put_on_cooldown()
            return 0, ""

        # Calcular dano com variação aleatória
        base = self.baseDamage + (caster.getMultiplierOfDamage() * 0.2) - target.defense
        if base < 0:
            base = 0
        # Adicionar variação de ±10%
        variation = random.uniform(0.9, 1.1)  # Entre 90% e 110% do dano base
        base *= variation
        damage, critical_message = self.critical_strike(base)
        target.hp = max(target.hp - damage, 0)

        print(f"{target.name} recebeu {damage:.1f} de dano! HP restante: {target.hp:.1f}")
        self.put_on_cooldown()
        return damage, critical_message
    