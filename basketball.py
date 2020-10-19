#baskethree=None
#keeps score
# 2 pointer 2 points
# 3 pointer 3 points
# if wrong key is hit keep asking for the right key
#10 points win
import random
from datetime import datetime, timedelta

print("Tim's BasketBall game")

user_score = []
cpu_score = []




def two_pointer(two, cpu_two):
    two_result = two
    cpu_result = cpu_two
    if two == 2:
        if random.random() <= .10:
            user_score.append(two_result)
            return print("You where fouled and made two free throws")
        elif random.random() <= .45:
            user_score.append(two_result)
            return print('You scored two points')
        if random.random() <= .10:
            cpu_score.append(cpu_result)
            return print("Cpu was fouled and made two free throws")
        elif random.random() <= .45:
            cpu_score.append(cpu_result)
            return print('Other team scored 2 points')
        elif random.random() <=.70:
            return print('Other team missed')
        elif random.random() <=.70:
            return print('You missed')
        else:
            print("Ball out of bounds")

def three_pointer(three, cpu_three):
    three_result = three
    cpu_three_result = cpu_three
    if three == 3:
        if random.random() <= .05:
            user_score.append(three_result)
            return print('You where fouled and made 3 free throws')
        elif random.random() <= .3:
            user_score.append(three_result)
            return print('you scored a three pointer')

        elif random.random() <= .05:
            cpu_score.append(cpu_three_result)
            return print('Cpu was fouled and made 3 free throws')
        elif random.random() <= .30:
            cpu_score.append(cpu_three_result)
            print('Cpu scored a three')
        elif random.random() <= .70:
            return print('You missed')
        elif random.random() <= .70:
            print("Cpu missed")
        else:
            return print("Ball out of bounds")




end_time = datetime.now() + timedelta(seconds = 45)# gives 45 seconds to play

while datetime.now() < end_time:
    user_input = input('To shoot a two pointer hit 2, for a three pointer hit 3 or q to quit\n')

    if user_input == 'q':
        player_sum = sum(user_score)
        cpu_sum = sum(cpu_score)
        print(f'Your score is {player_sum} and cpu score is {cpu_sum} game was not finished')
        break
    if user_input == '2':
        two_pointer(2,2)

        player_sum = sum(user_score)
        cpu_sum = sum(cpu_score)

        print(f'Player score is: {player_sum}\nCpu score is: {cpu_sum}')

    elif user_input == '3':
        three_pointer(3,3)

        player_sum = sum(user_score)
        cpu_sum = sum(cpu_score)
        print(f'User score is: {player_sum}\nCpu score is: {cpu_sum}')


    else:
        print('try again')
        continue

print(f'Final score is Player: {player_sum} Cpu is: {cpu_sum}')
