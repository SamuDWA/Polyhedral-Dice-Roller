# Polyhedral Dice Roller 🎲

An interactive command-line dice simulator built with Python tailored for RPG players and tabletop games, featuring multiple dice options and full bilingual support (English and Portuguese).

## ✨ Features

* **Bilingual Interface:** Choose between English and Portuguese at launch.
* **Comprehensive Dice Selection:** Supports standard polyhedral dice sets including D4, D6, D8, D10, D12, D20, and D010 (percentile tens dice).
* **Smart Input Handling:** Case-insensitive dice selection (accepts both 'd20' and 'D20') with error handling for invalid dice names.
* **Continuous Execution:** Roll multiple dice sequentially without needing to restart the application.

## 🚀 How it works

1. Run the script.
2. Select your preferred language (`english` or `portuguese`).
3. Choose which dice you want to roll from the available options.
4. The program generates a pseudo-random result instantly based on the chosen dice's bounds.
5. Choose whether to roll another dice or exit the program (`yes` / `sim`).

## 🛠️ Requirements

* Python 3.x installed.
* No external dependencies required (uses standard built-in `random` module).
