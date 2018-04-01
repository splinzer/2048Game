# coding:utf-8
'''
    [
    [2,0,2,4],
    [0,0,0,2],
    [2,0,4,8],
    [0,4,0,4]
    ]
'''
from tkinter import *
from tkinter.ttk import *
from random import sample


class Matrics():
    def gameover(self, sucess=True):
        self.best_score = self.current_score
        if sucess:
            print('胜利了！')
            self.callback(sucess=True)
        else:
            print('失败了！')
            self.callback(sucess=False)

    def is_faile(self):
        can_move_horizen = self.check_moveable('Right')
        can_move_vertical = self.check_moveable('Up')
        if can_move_horizen == False and can_move_vertical == False:
            return True
        else:
            return False

    def check_moveable(self, direction='Right'):
        '''
        检测指定方向是否可以移动
        :return:
        return
        '''
        matrices = self.matrices
        if direction == 'Up' or direction == 'Down':
            matrices = list(zip(*matrices))
        for i in matrices:

            # 存在零则可以移动
            if not all(i):
                return True
            # 同行存在相同数字移动
            else:
                prev_number = 0
                for j in i:
                    if prev_number == j:
                        return True
                    else:
                        prev_number = j
        return False

    def __init__(self):
        stage = 0
        self.matrices = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
        self.current_score = 0
        self.best_score = 0
        self.random_gen(True)
        self.callback = None

    def increase_score(self, score):
        self.current_score += score

    def random_gen(self, init=False):
        '''
        随机在0位置添加一个2或4
        :return:
        '''
        m = self.matrices
        zero_list = []
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 0:
                    zero_list.append((i, j))
        zl = len(zero_list)
        if zl == 0:
            return self.matrices
        elif zl == 1:
            m[zero_list[0][0]][zero_list[0][1]] = sample([2, 4], 1)[0]
        else:
            if init:
                ran_list = sample(zero_list, 2)
            else:
                ran_list = sample(zero_list, sample([1, 2], 1)[0])

            if len(ran_list) == 1:
                m[ran_list[0][0]][ran_list[0][1]] = 4
            elif len(ran_list) == 2:

                m[ran_list[0][0]][ran_list[0][1]] = 2
                m[ran_list[1][0]][ran_list[1][1]] = 2

        #self.matrices = m
        print(self)

    def __str__(self):
        '''
        格式化打印数字方阵
        :return:返回带格式和成绩信息的数字方阵
        '''
        result = ''
        for i in self.matrices:
            result += str(i) + '\n'
        current_score = 'score:' + str(self.current_score)
        best_score = 'best:' + str(self.best_score)
        return '{0:->10s}|{1:-<10s}'.format(current_score, best_score) + '\n' + result + '-' * 20

    def on_key_press(self, direction, callback):
        self.transform(direction=direction)

    def transform(self, direction='Right'):
        '''
        将数字方阵按照指定方向处理
        :param direction:方向，有效值有right,left,up,down
        :return:返回处理后的数字方阵
        '''
        result = []
        matrices = self.matrices

        if self.check_moveable(direction):
            # 该方向可以移动

            if direction == 'Up' or direction == 'Down':
                matrices = list(zip(*self.matrices))

            for i in matrices:
                if direction == 'Left' or direction == 'Up':
                    result.append(self.__merge(i, '<'))
                if direction == 'Right' or direction == 'Down':
                    result.append(self.__merge(i, '>'))

            if direction == 'Up' or direction == 'Down':
                matrices = list(zip(*result))
                # fix for 'TypeError: 'tuple' object does not support item assignment'
                for i in range(len(matrices)):
                    matrices[i] = list(matrices[i])
                self.matrices = matrices

            else:
                self.matrices = result
            self.random_gen()
        else:
            #不能移动
            if self.is_faile():
                self.gameover(sucess=False)

    def __merge(self, ls, to='>'):
        ls = ls[:]
        result = []
        pre_number = 0
        for i in range(0, len(ls)):
            if ls[i] != 0:

                if ls[i] == pre_number:
                    result.pop()
                    newvalue = ls[i] * 2
                    result.append(newvalue)
                    if newvalue == 2048:
                        # 胜利
                        self.gameover(sucess=True)
                    self.increase_score(ls[i])  # 合并增加成绩
                    pre_number = 0
                else:
                    result.append(ls[i])
                    pre_number = ls[i]
        if to == '>':
            return (len(ls) - len(result)) * [0] + result
        elif to == '<':
            return result + (len(ls) - len(result)) * [0]
