import random

def main():
    game_over = False
    selections = ['Rock', 'Paper', 'Scissors']
    print('-'*40)
    print('          Rock Paper Scissors')
    print('-'*40)

    player_name = input('Please type your name: ')
    print(f'Welcome {player_name}.  Rules of Rock Paper Scissors.  You will')
    print('select Rock, Paper or Scissors.  The computer will randomly select')
    print('from the same list.  Rock smashes Scissors, Paper covers Rock and ')
    print('Scissors cuts Paper.  If you choose the same item, it is a tie.')
    print('To win beat the computer 3 times.')
    print()

    weapons = [
        roll('Scissors', defeats='Paper', defeated_by='Rock'),
        roll('Rock', defeats='Scissors', defeated_by='Paper'),
        roll('Paper', defeats='Rock', defeated_by='Scissors'),
    ]

    contestants = {
        players(name=player_name,wins=0),
        players(name= 'Computer',wins=0),
    }


    while game_over!=True:

        player_choice = input('Type a selection (Rock, Paper or Scissors): ')
        while player_choice not in selections:
            player_choice = input('Enter Rock, Paper or Scissors: ')
        computer_choice = random.choice(weapons)
        print(f'The computer chooses {computer_choice.name}')

        if player_choice == computer_choice.defeats:
            print('The computer wins the round.')
            for i in contestants:
                if i.name == 'Computer':
                    i.wins = i.wins +1
        elif player_choice == computer_choice.defeated_by:
            print('You win the round.')
            for i in contestants:
                if i.name != 'Computer':
                    i.wins = i.wins + 1

        elif player_choice == computer_choice.name:
            print('The round is tied.')

        print()
        for i in contestants:
            if (i.wins) >= 3:                     # if one play has 3 wins, they are the winner
                print(f'{i.name} wins game!')
                game_over = True
                break
            else:                               # if a player has fewer than 3 wins print current score
                print(f'{i.name} score: {i.wins}')



class roll:
    def __init__(self, name, defeats, defeated_by):
        self.name = name
        self.defeats = defeats
        self.defeated_by = defeated_by



class players:
    def __init__(self, name, wins=0):
        self.name = name
        self.wins = wins

    def add_win(self):
        self.wins+=1




if __name__ == '__main__':
    main()

