from random import choice

def flip_a_coin():
    coin_flip = choice(["Heads", "Tails"])
    print(f"You flipped {coin_flip}.")
    if coin_flip == "Heads":
        print("You won!")
    else:
        print("You lost!")
    
def print_how_to():
    print("Heads you win\nTails you lose\n")

def main():
    print_how_to()
    for _ in range(20):
        flip_a_coin()

print("Thanks for playing the coin flipper")

main()