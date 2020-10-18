from deck import Deck 
from player import Player

def play():

    player_one = Player("1")
    player_two = Player("2")

    new_deck = Deck()
    new_deck.shuffle()
    deal_carts_count = int(len(new_deck.all_cards)/2)

    for _ in range(deal_carts_count):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
        
    game_on = True

    round_count = 1
    while game_on:
        
        print(f"Round {round_count}")
        
        # Check to see if a player is out of cards:
        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break
            
        if len(player_two.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break
        
        # Otherwise, the game is still on!
        
        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
        
        at_war = True

        while at_war:

            print("Player {}: {}\t Player {}: {}".format(player_one.name, player_one_cards[-1],
                                        player_two.name, player_two_cards[-1]))
            if player_one_cards[-1].value > player_two_cards[-1].value:

                # Player One gets the cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                print("Player {} got the cart".format(player_one.name))
                
                # No Longer at "war" , time for next round
                at_war = False
            
            # Player Two Has higher Card
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # Player Two gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                print("Player {} got the cart".format(player_two.name))
                
                # No Longer at "war" , time for next round
                at_war = False

            else:
                print('WAR!')
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.
                
                # First check to see if player has enough cards
                
                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins! Player One Loses!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins! Player One Loses!")
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for _ in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

            print("Player {} and Player {}.\n".format(player_one, player_two))
            # In case of deadlock pattern for players hands
            if not round_count % 200:
                player_one.shuffle()
                player_two.shuffle()
                
            round_count += 1
            

if __name__ == "__main__":
    play()