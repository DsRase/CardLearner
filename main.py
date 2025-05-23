from tkinter import *
from tkinter import ttk
from random import shuffle

class Card:
    def __init__(self, meaning, definition):
        self.meaning = meaning
        self.definition = definition
        self.current = self.meaning # by default

class Learning:
    # Format:
    # Meaning<>Value\n
    path = "learning.txt"
    def __init__(self):
        self.tasks = self.get_tasks()
        shuffle(self.tasks)

    def get_tasks(self):
        result = []
        with open(self.path, mode='r', encoding='utf-8') as f:
            for line in f:
                meaning = list(line.split('<>')[0].strip())
                definition = list(line.split('<>')[1].strip())

                if len(meaning) > 40:
                    for i in range(40, len(meaning)-1, 40):
                        meaning.insert(i, '\n')

                if len(definition) > 40:
                    for i in range(40, len(definition)-1, 40):
                        definition.insert(i, '\n')

                meaning = "".join(meaning)
                definition = "".join(definition)

                result.append(Card(meaning, definition))
        return result

    def restart(self):
        print("Restarting tasks")
        self.tasks = self.get_tasks()

    @staticmethod
    def add_new_word(meaning, definition):
        with open(Learning.path, mode='a', encoding='utf-8') as f:
            f.write(f"{meaning}<>{definition}\n")

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Quizlet на минималках и на ткинтере")
        self.resizable(False, False)

        self.mode = 0 # 0 - meaning <> value ; 1 - value <> meaning

        self.current_card = None
        self.card_frame = ttk.Frame(self).pack()
        self.current_btn = ttk.Button(self.card_frame, text="Нажми - похуй го некст", width=50, command=self.flip_card)

        self.show_menu()

    # 0 - word
    # 1 - definition
    def change_mode(self):
        if self.mode: self.mode = 0
        else: self.mode = 1

    def show_menu(self):
        ttk.Button(self, text="Сменить режим", width=50, command=self.change_mode).pack()
        self.show_new_card()
        self.current_btn.pack()
        frame = ttk.Frame(self).pack()
        ttk.Button(frame, text="Перезапуск", width=25, command=learner.restart).pack(side='left')
        ttk.Button(frame, text="Похуй, го некст", width=25, command=self.show_new_card).pack(side='right')

    def flip_card(self):
        if self.mode:
            self.current_btn["text"] = self.current_card.definition if self.current_card.definition != self.current_btn["text"] else self.current_card.meaning
        else:
            self.current_btn["text"] = self.current_card.meaning if self.current_card.meaning != self.current_btn[
                "text"] else self.current_card.definition
    # show new card for learning
    def show_new_card(self):
        if not learner.tasks: learner.restart()
        card = learner.tasks.pop()
        self.current_card = card

        self.flip_card()

        # text = card.meaning if not self.mode else card.definition
        # btn = ttk.Button(self.card_frame, text=text, width=50, command=lambda: self.flip_card(btn, card))

if __name__ == "__main__":
    learner = Learning()

    root = Window()
    root.mainloop()