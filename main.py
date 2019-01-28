import world
import gameover

def run_game():

    new_world = world.World()

    while True:
        try:
            turn(new_world)
        except GameOver:
            break
    print('Game over')

if __name__ == "__main__": 
    run_game()