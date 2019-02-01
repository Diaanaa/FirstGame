import tkinter as tk
from PIL import ImageTk, Image
import world
from gameover import *
import random 
import time

def show_image(path):
    image_window = tk.Tk()
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(image_window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    image_window.mainloop()

def run_game():    
    new_world = world.World()
    while True:
        try:
            turn(new_world)
        except GameOver:
            break
    show_image('C:\FirstGame\picgameover.jpg')

print("Ну привет, маленький ублюдок.")
time.sleep(2)
print("Я очень задолбался делать эту сранную игру\nпоэтому вместо того, чтобы мирно шляться по подземелью и искать дверь с ключом,\nты будешь бегать по коммуналке с соседями-алкашами и искать водяру с закуской.\nДобро пожаловать в жестокую реальность!")
time.sleep(3)

def turn(new_world):
    current_room = new_world.player.owner
    print("Ты находишься в комнате:  %i" % (current_room.number + 1))
    room_numbers = []
    if len(current_room.ways) != 0:
        where_to_go = [
        'Можешь пройти нахуй или в эти комнаты:',
        'А теперь можешь попиздохать сюда:',
        'В свободной стране - свободный выбор комнат, куда пойти:',
        ]
        message = random.choice(where_to_go)
        for room in current_room.ways:

            room_numbers.append(room.number)
            message += " %i" % (room.number + 1)

        print(message)
    
    if current_room.owner is not None:
        room_numbers.append(-1)
        print("Вернуться: 0")
    
    room_number = int(input("Выберите номер комнаты: ")) - 1
    while room_number not in room_numbers:
        print("Ну ты и тупой, хочешь биться головой об стену - бейся, но в другую комнату ты все равно не телепортируешься")
        time.sleep(1)
        room_number = int(input("Выберите номер комнаты: ")) - 1 

    print()

    new_world.play(room_number)

if __name__ == "__main__": 
    run_game()