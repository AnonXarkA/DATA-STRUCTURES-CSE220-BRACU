# 3

import random

 participant = [1, 2, 3, 4, 5, 6, 7]
  parti_lenght = len(participant)

   def musical_chair(list):
        while parti_lenght > 1:
            print("Player Order:", participant)
            randint = random.randint(0, 3)

            if randint == 1:
                if parti_lenght % 2 == 0:
                    delete = int(parti_lenght/2)-1
                else:
                    delete = int(parti_lenght/2)
                print(f'player{delete} is out')
                participant.pop(delete)
            participant.insert(0, participant[len(participant)-1])
            participant.pop(len(participant)-1)
        print("Winner is", participant[0])

    participant = [1, 2, 3, 4, 5, 6, 7]
    musical_chair(list)

    Player Order: [1, 2, 3, 4, 5, 6, 7]
    Player Order: [7, 1, 2, 3, 4, 5, 6]
    player3 is out
    Player Order: [6, 7, 1, 2, 4, 5]
    player3 is out
    Player Order: [5, 6, 7, 1, 4]
    Player Order: [4, 5, 6, 7, 1]
    Player Order: [1, 4, 5, 6, 7]
    Player Order: [7, 1, 4, 5, 6]
    Player Order: [6, 7, 1, 4, 5]
    player3 is out
    Player Order: [5, 6, 7, 1]
    Player Order: [1, 5, 6, 7]
    Player Order: [7, 1, 5, 6]
    Player Order: [6, 7, 1, 5]
    player3 is out
    Player Order: [1, 6, 7]
    Player Order: [7, 1, 6]
    player3 is out
