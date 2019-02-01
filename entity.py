import random
import time
from gameover import *
class Entity:

    def __init__(self, name, owner = None):
        
        self.name = name
        self.owner = owner
        self.objects = {}

    def go_to(self, new_owner):
        
        if self.owner is not None:
            if self.name in self.owner.objects:          
                del self.owner.objects[self.name]
        
        new_owner.objects.update({self.name : self})
        self.owner = new_owner 

    def around(self):

        objects_around = self.owner.objects

        if "добрячок Валера" in objects_around:
            print('Ты повстречал добрячка Валеру. Он один из жильцов сей злополучной коммуналки. Он может рассказать тебе несмешной анекдот, жизненную мудрость, новости про Украину(нет) или просто уйти.')
            
            choice = input("Выбери, что ты хочешь услышать - анекдот, мудрость или ничего:").lower()
            def drinker_to_do(choice):
                if choice == "анекдот":
                    jokes = [
                                "Difference between machine learning and AI:\nIf it is written in Python, it`s probably machine learning\nIf it is written in PowerPoint, it`s probably AI",
                                "Если приговоренный к смерти чихнул, тактичный палач должен промолчать",
                                "-Давай чмокнемся\n-Давай\n-Чмо\n-Чмо"
                            ]
                    print(random.choice(jokes))
                    time.sleep(4)

                elif choice == "мудрость":
                    wisdom = [
                                "Без аргумента, ты не функция,\nбез аксиомы ты не теорема,\nа без арифметики, ты даже не ноль",
                                "Программы и церкви очень похожи. Сначала мы их строим, а потом молимся, чтобы сработало",
                                "На питоне можно написать что угодно.\nНа С++ можно написать питон"
                             ]
                    print(random.choice(wisdom))
                    time.sleep(4)
            
                else:
                    print("Ой, да иди ты к черту, добрячок Валера обиделся!")
                    time.sleep(4)
                    return choice
            drinker_to_do(choice)
            objects_around["добрячок Валера"].go_to(self)
        if "злой Петрович" in objects_around:
                print("О, нет, ты повстречал злого алкаша Петровича, который как раз искал закуску.\nТеперь его закуской станешь ты!\nПокойся с миром...")
                objects_around["злой Петрович"].go_to(self)
                time.sleep(2)
                raise GameOver()
        if "закусочка" in objects_around:
            message = "Ты нашел закусочку к водочке!"         
            if "водочка" in self.objects:
                print(message + "Теперь можешь насладиться пьянством и простимулировать гибель нескольких сот нейронов,\nхотя они тебе все равно никогда не понадобились бы.")
                raise GameOver()
            else:
                print(message + " Но водочку ты все еще не нашел, лузер.")
                objects_around["закусочка"].go_to(self)

        if "водочка" in objects_around:
            message = "Ты нашел водочку"
            if "закусочка" in self.objects:
                print(message + "Теперь можешь насладиться пьянством и простимулировать гибель нескольких сот нейронов,\nхотя они тебе все равно никогда не понадобились бы")
                raise GameOver()
            else:
                print("Ты нашел водочку. Дело за малым. Найди закуску и пьянствуй на здоровье!")
                objects_around["водочка"].go_to(self)



