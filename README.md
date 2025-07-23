# 🧠 Nim Nexus - A Terminal-Based Strategy Game

Welcome to **Nim Nexus**, a terminal-based Python game built as a part of a Game Theory course project. This is a classic **two-player mathematical game of strategy**, where players take turns removing stones from heaps — and the one who takes the last stone wins.

> 💡 Inspired by the well-known *Nim Game* used in AI/game theory research.

---

## 🎮 Game Rules

- There are 3 heaps of stones (each initialized with a random number of stones).
- On your turn, choose a heap and remove **1 to 5 stones**.
- The AI opponent will do the same.
- The player who removes the **last stone** wins.

---

## 🧠 Strategy Behind the Game

- The **winning strategy** is based on the XOR of heap sizes.
- If the XOR of all heap sizes is 0, the current player is in a losing position.
- This version currently features a **random AI**. Future updates will include a **perfect AI** based on XOR strategy.

---

## 🛠 Tech Stack

- Python 3
- Terminal-based interface (no external dependencies)

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3 installed

### ▶️ How to Run

```bash
git clone https://github.com/yourusername/nim-nexus-game.git
cd nim-nexus-game
python nim_game.py
