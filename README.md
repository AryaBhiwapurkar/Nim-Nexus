# Nim-Nexus
Game Theory course project, IVth semester. 
Nim Nexus
Nim Nexus is a two-player mathematical game where players take turns removing stones from heaps. The player who removes the last stone wins. This version of Nim Nexus allows you to play against an AI opponent.

Rules
At the beginning of the game, there are three heaps of stones with random numbers of stones in each heap.
Players take turns choosing a heap and removing 1 to 5 stones from that heap.
The game continues until all the heaps are empty.
The player who removes the last stone wins the game.
Usage
Run the nim_nexus.py file.
You can follow the on-screen instructions to make your moves.
To remove stones from a heap, enter the heap index (1, 2, 3, ...) and the number of stones to remove.
The game ends when all the heaps are empty. The winner (player or AI) will be displayed.
Winning Strategy
The winning strategy for Nim Nexus is to ensure that the XOR (exclusive OR) of the number of stones in each heap remains zero after every move.
Getting Started

To start with Nim Nexus, clone this repository to your local machine and run the nim_nexus.py file.
git clone https://github.com/ChillHard/nim-nexus.git
cd nim-nexus
python nim_nexus.py

Author
Arya Mahesh Bhiwapurkar, Muskan Dewangan, Shubham Gupta, Subhali AR Otti

License
This project is licensed under the MIT License - see the LICENSE file for details.
