import random  # for generating random numbers.
import sys  # for exiting the game.

def print_heap_state(heaps):
   
    print("Current heap state:")
    for i, stones in enumerate(heaps):  # Iterating over the heaps.
        print(f"Heap {i+1}: {stones} stones")  # Printing the number of stones in each heap.
    print()

def player_move(heaps):
    
    print_heap_state(heaps)  # Displaying the current state of the heaps.
    while True:
        heap_index = input("Enter the heap index (1, 2, 3, ...) or type 'q' to quit: ")  # Prompting the player to choose a heap or quit.
        if heap_index.lower() == 'q':
            print("Exiting the game. Goodbye!")
            sys.exit()
        try:
            heap_index = int(heap_index) - 1  # Converting the input to an integer and adjusting for 0-based indexing.
            if heap_index < 0 or heap_index >= len(heaps):  # Checking if the input is within the valid range of heap indices.
                print("Invalid heap index. Please try again.")
                continue
            while True:
                stones_to_remove = int(input("Enter the number of stones to remove (1, 2, 3, 4, or 5): "))
                if stones_to_remove < 1 or stones_to_remove > 5:
                    print("Invalid number of stones. Please enter 1, 2, 3, 4, or 5.")
                    continue
                if stones_to_remove > heaps[heap_index]:
                    print("You cannot remove more stones than are in the heap. Please try again.")
                    continue
                heaps[heap_index] -= stones_to_remove  # Updating the number of stones in the chosen heap.
                break
            break  # Exiting the loop once a valid move is made.
        except ValueError:
            print("Invalid input. Please enter a valid heap index or 'q' to quit.")


def ai_move(heaps):
    
    print_heap_state(heaps)  # Displaying the current state of the heaps.
    nonempty_heaps = [(i, stones) for i, stones in enumerate(heaps) if stones > 0]  # Finding the indices and number of stones in non-empty heaps.
    heap_index, stones_to_remove = random.choice(nonempty_heaps)  # Choosing a random non-empty heap and number of stones.
    max_stones_to_remove = min(stones_to_remove, 5)  # Limiting the maximum number of stones to remove to 5.
    stones_to_remove = random.randint(1, max_stones_to_remove)  # Choosing a random number of stones to remove within the limit.
    print(f"The AI removes {stones_to_remove} stones from heap {heap_index+1}")  # Informing the player about the AI's move.
    heaps[heap_index] -= stones_to_remove  # Updating the number of stones in the chosen heap.

def is_game_over(heaps):
    
    return all(stones == 0 for stones in heaps)  # Returns True if all heaps are empty, indicating the game is over.

def main():
    
    heaps = [random.randint(5, 20) for _ in range(3)]  # Initializing random heaps with random numbers of stones.
    print("Welcome to Nim Nexus!")  
    print("Nim Nexus is a two-player mathematical game where players take turns removing stones from heaps.")
    print("The player who removes the last stone wins.")
    print("In this version of Nim Nexus, you will be playing against an AI opponent.")
    print("To make a move, enter the heap index (1, 2, 3, ...) and the number of stones to remove.")
    print("Winning Strategy: XOR (exclusive OR) of the number of stones in each heap remains zero after every move.")
    print("Let's get started!")
    while not is_game_over(heaps):  # Loop until the game is over.
        player_move(heaps)  # Player's turn.
        if is_game_over(heaps):  # Checking if the game is over after the player's move.
            print("You win! Congratulations!") 
            break  
        ai_move(heaps)  # AI's turn.
        if is_game_over(heaps):  # Checking if the game is over after the AI's move.
            print("The AI wins! Better luck next time.")  # Informing the player about the AI's victory.
            break 

if __name__ == "__main__":
    main() 