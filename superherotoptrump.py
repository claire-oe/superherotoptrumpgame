
import requests
from io import BytesIO
import random


# display on screen
print("____________________________________________________________\n")
print("                   SUPERHERO TOP TRUMPS    ")
print("_____________________________________________________________\n")
print('Welcome To The SuperHero Top Trump Game')
print('Instructions: ')
print('You will be randomly given a Superhero to compete with \nPick a powerstats to compete with')
print('The winner will be the player with best two out of three.\n')


# # score variables
# user = 0
# cpu = 0


def random_superhero():
    superhero_number = random.randint(1, 731)
    url = 'https://superheroapi.com/api/3161516373936069/{}/'.format(superhero_number)
    response = requests.get(url)
    superhero = response.json()

    return {
        'name': superhero['name'],
        'id': superhero['id'],
        'intelligence': superhero['powerstats']['intelligence'],
        'speed': superhero['powerstats']['speed'],
        'combat': superhero['powerstats']['combat'],
        'image': superhero['image'], }


def run():
    my_superhero = random_superhero()
    print('You were given {}'.format(my_superhero['name']))
    stat_choice = input('Which stat do you want to use? (intelligence, speed, combat) ')
    opponent_superhero = random_superhero()
    print('The opponent chose {}'.format(opponent_superhero['name']))
    my_stat = my_superhero[stat_choice]
    opponent_stat = opponent_superhero[stat_choice]
    user = 0
    cpu = 0
    if my_stat > opponent_stat:
        print('You Win!')
        user += 1
    elif my_stat < opponent_stat:
        print('You Lose!')
        cpu += 1
    else:
        print('Draw!')


for i in range(3):
    run()
    if cpu > user:
        print("CPU wins the match!")
    elif user > cpu:
        print("Player wins the match!")


# if cpu > user:
#     print("CPU wins the match!")
# elif user > cpu:
#     print("Player wins the match!")



