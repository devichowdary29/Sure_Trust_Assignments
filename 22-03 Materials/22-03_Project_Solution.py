import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def choose_move(self):
        valid_moves = ["rock", "paper", "scissors"]
        while True:
            move = input(f"{self.name}, enter your move (rock, paper, scissors): ").strip().lower()
            if move in valid_moves:
                return move
            print("Invalid move. Please choose rock, paper, or scissors.")
class Computer(Player):
    def choose_move(self):
        return random.choice(["rock", "paper", "scissors"])
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

class Game:
    def __init__(self):
        self.player = Player("Alice")
        self.computer = Computer("AI")

    def play_round(self):
        player_move = self.player.choose_move()
        computer_move = self.computer.choose_move()
        print(f"Computer chose: {computer_move}")
        print(determine_winner(player_move, computer_move))

    def play_game(self):
        rounds = 3
        for _ in range(rounds):
            self.play_round()
        print("Game Over!")

# Run the game
game = Game()
game.play_game()
