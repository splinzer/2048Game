from View import *
from Model import Matrics


class Game():

    def __init__(self):
        root = Tk()
        root.title('2048')
        self.stage = Stage(root)
        self.init()

        root.bind("<KeyPress>", self.keypress)
        #root.bind('<Button-1>', self.doit)
        root.mainloop()
    def keypress(self, event):
        keysym = event.keysym

        if keysym in ['Up', 'Down', 'Left', 'Right']:
            self.matrics.transform(keysym)
            print('pressed:', keysym)

            self.stage.update_cell(self.matrics.matrices)
            self.stage.set_current_score('当前成绩：' + str(self.matrics.current_score))

    def gameover(self, sucess=True):
        self.stage.set_best_score('最好成绩：' + str(self.matrics.best_score))
        self.stage.gameover(sucess)
        self.init()

    def doit(self, e):
        self.matrics.gameover(True)

    def init(self):
        self.matrics = Matrics()
        self.stage.update_cell(self.matrics.matrices)
        self.matrics.callback = self.gameover

if __name__ == "__main__":
    Game()
