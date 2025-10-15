# ⚔️ RPG Battle – Python Terminal Game

🎓 **Desenvolvido no âmbito do módulo de Python Avançado**  
Curso de **Programação Informática**

---

## 👥 Créditos

**Autores:** Bruno Carvalho; Fábio Silva; Marco Nunes; Miguel Nicolau  
**Formador:** Miguel Frias 
**Ano:** 2025  
**Instituição:** CENCAL - Centro de Formação Profissional Caldas da Rainha

---

## 🎮 Descrição

Bem-vindo ao **RPG Battle**, um jogo de combate por turnos em linha de comandos, desenvolvido em **Python**.  
Cria o teu herói, enfrenta inimigos aleatórios e domina as artes do combate!  
Inspirado nos clássicos RPGs de fantasia, este projecto foi criado como exercício prático de programação orientada a objectos e lógica de combate.

---

## 🧙‍♂️ Classes jogáveis

Escolhe entre 5 classes, cada uma com atributos e habilidades únicas:

| Classe | Recurso | Estilo | Descrição |
|:-------|:---------|:--------|:-----------|
| 🗡️ **Warrior** | Rage | Corpo-a-corpo | Ataques poderosos e habilidades defensivas. |
| 🔮 **Mage** | Mana | Mágico | Especialista em feitiços de fogo e controle. |
| 🕶️ **Rogue** | Energy | Furtivo | Ataques críticos e venenos paralisantes. |
| 🌿 **Druid** | Mana | Híbrido | Capaz de curar e manipular a natureza. |
| 🏹 **Hunter** | Mana | À distância | Ataques precisos e controle de campo. |

---

## ⚔️ Funcionalidades principais

- Sistema de **combate por turnos** entre jogador e inimigo.  
- Escolha de classe e **habilidades exclusivas**.  
- **IA básica** para o inimigo (decisões aleatórias com cooldowns e gestão de recursos).  
- **Sistema de cooldown** e **recuperação de recursos**.  
- **Interface de texto limpa** com logs de combate.  
- **Guia de habilidades** acessível via comando `help`.  

---

## 🧩 Estrutura do projecto

📦 RPG
├── main.py # Lógica principal do jogo
├── characters.py # Classes e atributos dos personagens
├── abilities_setup.py # Configuração das habilidades (não incluído neste exemplo)
└── README.md

---

## 🚀 Como jogar

1. Certifica-te de ter o Python 3 instalado:
```bash
   python --version
```

2. Clona o repositório e entra na pasta:
```bash
git clone https://github.com/teu-utilizador/RPG-Battle.git
cd RPG-Battle
```

3. Executa o jogo:
```bash
python main.py
```

4. Segue as instruções no ecrã:

   -Escolhe o nome do teu personagem.
   -Selecciona a tua classe.
   -Usa habilidades, gere recursos e derrota o inimigo!

🧠 Conceitos aplicados

   -Programação orientada a objectos (herança e polimorfismo)
   -Gestão de estados (HP, recursos, cooldowns)
   -Estruturas de decisão e loops
   -Modularização de código
   -Aleatoriedade e IA simples
   -Interacção via terminal

| Versão | Descrição                                                     |
| :----- | :------------------------------------------------------------ |
| `v1.0` | Versão inicial jogável com 5 classes.                         |
| `v1.1` | Ajustes de balanceamento e melhorias de interface.            |
| `v2.0` | Planeado: sistema de itens, experiência e múltiplos inimigos. |
| `v3.0` | Planeado: interface gráfica e modo história.                  |


📜 Licença

Este projecto é de uso educativo e pode ser livremente partilhado e modificado para fins de aprendizagem.
Criado com ❤️ em Python.

\----\

Dito pelo ChatGPT:
⚔️ RPG Battle – Python Terminal Game

🎓 Developed as part of the Advanced Python module
Course in Computer Programming

👥 Credits

Authors: Bruno Carvalho; Fábio Silva; Marco Nunes; Miguel Nicolau
Instructor: Miguel Frias
Year: 2025
Institution: CENCAL - Professional Training Center, Caldas da Rainha

🎮 Description

Welcome to RPG Battle, a turn-based command-line combat game developed in Python.
Create your hero, face random enemies, and master the art of battle!
Inspired by classic fantasy RPGs, this project was built as a practical exercise in object-oriented programming and combat logic.

🧙‍♂️ Playable Classes

Choose from 5 classes, each with unique attributes and abilities:

Class	Resource	Style	Description
🗡️ Warrior	Rage	Melee	Powerful attacks and defensive abilities.
🔮 Mage	Mana	Magic	Master of fire spells and control abilities.
🕶️ Rogue	Energy	Stealth	Critical strikes and paralyzing poisons.
🌿 Druid	Mana	Hybrid	Can heal and command the forces of nature.
🏹 Hunter	Mana	Ranged	Precise attacks and battlefield control.
⚔️ Main Features

Turn-based combat system between player and enemy.

Class selection with unique abilities.

Basic enemy AI (random decisions with cooldowns and resource management).

Cooldown system and resource regeneration.

Clean text-based interface with combat logs.

Ability guide accessible with the help command.

🧩 Project Structure

📦 RPG
├── main.py — Main game logic
├── characters.py — Character classes and attributes
├── abilities_setup.py — Ability configuration (not included in this example)
└── README.md

🚀 How to Play

Make sure you have Python 3 installed:

python --version


Clone the repository and open the folder:

git clone https://github.com/your-username/RPG-Battle.git
cd RPG-Battle


Run the game:

python main.py


Follow the on-screen instructions:

Choose your character’s name.

Select your class.

Use abilities, manage resources, and defeat your enemy!

🧠 Key Concepts Applied

Object-oriented programming (inheritance and polymorphism)

State management (HP, resources, cooldowns)

Decision structures and loops

Code modularization

Randomness and simple AI

Terminal-based interaction

🧭 Versions & Future Development
Version	Description
v1.0	Initial playable version with 5 classes.
v1.1	Balance adjustments and interface improvements.
v2.0	Planned: item system, experience, and multiple enemies.
v3.0	Planned: graphical interface and story mode.
📜 License

This project is for educational use and may be freely shared or modified for learning purposes.
Created with ❤️ in Python.

