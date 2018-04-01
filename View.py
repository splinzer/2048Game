from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class Stage():
    def set_current_score(self, newvalue):
        self.current_score.set(newvalue)

    def set_best_score(self, newvalue):
        print(newvalue)
        self.best_score.set(newvalue)

    def gameover(self, sucess=True):
        if sucess:
            message = '胜利～～～是否再来一把？'
        else:
            message = '游戏结束，是否再来一把？'
        oncemore = messagebox.askyesno(parent=self.root, title=message, message=message, type=messagebox.YESNO,
                         icon=messagebox.QUESTION)
        if not oncemore:
            self.root.quit()
        return oncemore

    def __init__(self, parent):

        

        head = Frame(parent, width=400, height=50)
        head_style = Style()
        head_style.configure('heads.TFrame', borderwidth=4, background='#c0c0c0', relief='solid')
        head.configure(style='heads.TFrame')
        head.pack()
        # self.matrices = Matrics(self)
        # self.matrices.callback = self.update_cell
        self.root = parent
        self.current_score = StringVar()
        self.best_score = StringVar()
        self.current_score.set('当前成绩：--')
        self.best_score.set('最好成绩：--')

        current_score_label = Label(head, textvariable=self.current_score)
        current_score_label.grid(column=0, row=0, ipadx=10)

        best_score_label = Label(head, textvariable=self.best_score)
        best_score_label.grid(column=2, row=0, ipadx=10)

        frame = Frame(parent, width=420, height=420)
        frame_style = Style()
        frame_style.configure('body.TFrame', borderwidth=10, bordercolor='#eee4da', relief='solid')
        frame.configure(style='body.TFrame')
        frame.pack_propagate(False)
        frame.pack()

        self.canvas = Canvas(frame, width=400, height=400, background='#bbada0')
        self.canvas.place(x=10, y=10)
        # 间隔8px，方块宽度90
        space = 8
        cell_width = 90

        for i in range(4):
            for j in range(4):
                r_x1 = (j + 1) * space + j * cell_width
                r_y1 = (i + 1) * space + i * cell_width
                r_x2 = (j + 1) * space + (j + 1) * cell_width
                r_y2 = (i + 1) * space + (i + 1) * cell_width
                t_x1 = r_x1 + cell_width / 2
                t_y1 = r_y1 + cell_width / 2
                index = str(i) + str(j)
                r_tag = 'r' + index
                t_tag = 't' + index
                self.canvas.create_rectangle(r_x1, r_y1, r_x2, r_y2, fill='#eee4da', width=0, tag=r_tag)
                self.canvas.create_text(t_x1, t_y1, text='0', font=('arial', 20), fill='green', tag=t_tag)

        # def hiddenit(event):
        #
        #     w = event.widget
        #     id = w.find_closest(event.x,event.y)
        #     w.itemconfigure(id,state=HIDDEN)
        #     if canvas.itemcget('r00', 'state') != HIDDEN:
        #         canvas.itemconfig('r00',state=HIDDEN)
        #         canvas.itemconfig('t00', state=HIDDEN)
        #     else:
        #         canvas.itemconfig('r00', state=NORMAL)
        #         canvas.itemconfig('t00', state=NORMAL)
        #     self.canvas.itemconfig('t13', state=HIDDEN)
        #     print(1)
        #
        # self.canvas.bind("<Button-1>", hiddenit)

    def update_cell(self, m):
        for i in range(len(m)):
            for j in range(len(m[i])):
                r_tag = 'r' + str(i) + str(j)
                t_tag = 't' + str(i) + str(j)
                if m[i][j] == 0:
                    self.canvas.itemconfig(r_tag, state=HIDDEN)
                    self.canvas.itemconfig(t_tag, state=HIDDEN)
                else:
                    self.canvas.itemconfig(r_tag, state=NORMAL)
                    self.canvas.itemconfig(t_tag, state=NORMAL)
                    self.canvas.itemconfig(t_tag, text=m[i][j])
