import random

def black_jack():
    print("\n🎲 Welcome to Black Jack!")
    print("Goal: Get as close to 21 as possible without going over.\n")

    while True:
        # Create and shuffle deck
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
                 'Jack', 'Queen', 'King', 'Ace']
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)

        # Deal initial hands
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Function to calculate hand value
        def calculate_hand_value(hand):
            value = 0
            aces = 0

            for rank, suit in hand:
                if rank in ['Jack', 'Queen', 'King']:
                    value += 10
                elif rank == 'Ace':
                    aces += 1
                    value += 11
                else:
                    value += int(rank)

            # Adjust for Aces if over 21
            while value > 21 and aces:
                value -= 10
                aces -= 1

            return value

        # Function to display hand nicely
        def display_hand(hand):
            return ', '.join([f"{rank} of {suit}" for rank, suit in hand])

        # --------------------
        # Player Turn
        # --------------------
        while True:
            player_value = calculate_hand_value(player_hand)

            print(f"\nYour hand: {display_hand(player_hand)} (Value: {player_value})")
            print(f"Dealer's visible card: {dealer_hand[0][0]} of {dealer_hand[0][1]}")

            if player_value > 21:
                print("❌ You went over 21! You lose.")
                break

            if player_value == 21:
                print("🎉 Black Jack! Let's see what the dealer has...")
                break

            action = input("Do you want to hit or stand? (h/s): ").lower()

            if action == 'h':
                if not deck:
                    print("Reshuffling deck...")
                    deck = [(rank, suit) for suit in suits for rank in ranks]
                    random.shuffle(deck)
                player_hand.append(deck.pop())
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        player_value = calculate_hand_value(player_hand)

        # --------------------
        # Dealer Turn
        # --------------------
        if player_value <= 21:
            print(f"\nDealer's hand: {display_hand(dealer_hand)} "
                  f"(Value: {calculate_hand_value(dealer_hand)})")

            while calculate_hand_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                print(f"Dealer's hand: {display_hand(dealer_hand)} "
                      f"(Value: {calculate_hand_value(dealer_hand)})")

            dealer_value = calculate_hand_value(dealer_hand)

            # --------------------
            # Determine Winner
            # --------------------
            if dealer_value > 21:
                print("🎉 Dealer busts! You win!")
            elif dealer_value > player_value:
                print("❌ Dealer wins!")
            elif dealer_value < player_value:
                print("🎉 You win!")
            else:
                print("🤝 It's a tie!")

        # --------------------
        # Replay Option
        # --------------------
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye 👋")
            break


# Run the game
black_jack()
