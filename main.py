__time__ = '2021/8/1'
__author__ = 'ZhiYong Sun'


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sudoku import Ui_Form
import matplotlib.pyplot as plt
import os
import csv


class game(QMainWindow, Ui_Form):
    def __init__(self):
        super(game, self).__init__()
        self.setupUi(self)
        self.path = self.getRealPath()   # exe执行时解压后的资源路径

    def load_problem(self):    # 加载问题数据 curr = self.curr
        with open(file=self.path + r'./ziyuan/problem.txt', mode='r', encoding='utf-8') as fr:
            data = list(csv.reader(fr))
        curr = int(data[0][0])
        if curr >= len(data):
            QMessageBox.information(self, "通关证明", "恭喜玲兰姐姐完美通关！请点击获取福利~", QMessageBox.Yes)
            self.show_pic()
            curr = len(data) - 1
        prob = [[data[curr][i * 9 + j] for j in range(9)] for i in range(9)]
        self.count.setText(str(curr))
        return prob

    def show_pic(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        img = plt.imread(self.path + r'./ziyuan/fuli.jpg')
        plt.figure("通关福利")  # 图像窗口名称
        plt.imshow(img)
        plt.axis('off')  # 关掉坐标轴为 off
        plt.title('情 人 节 快 乐 之 湿 身 诱 惑')  # 图像题目
        plt.show()

    def isvalid(self, board):  # 判定数独是否有效
        size = len(board)
        rows, cols, subs = [set() for _ in range(size)], [set() for _ in range(size)], [set() for _ in range(size)]

        for i in range(size):
            for j in range(size):
                num = board[i][j]
                if num <= 0 or num > 9:
                    return False
                if 0 < num <= 9:
                    sub_index = 3 * (i // 3) + j // 3
                    if num in rows[i] or num in cols[j] or num in subs[sub_index]:
                        return False

                    rows[i].add(num)
                    cols[j].add(num)
                    subs[sub_index].add(num)

        return True

    def getRealPath(self):
        # 获取exe解压目录的绝对路径
        p = os.path.realpath(sys.path[0])
        p = p.replace(r'\base_library.zip', '')
        return p

    def reset(self):
        prob = self.load_problem()
        for i in range(9):
            for j in range(9):
                self.table.setItem(i, j, QTableWidgetItem(prob[i][j]))    # 设置数字
                self.table.item(i, j).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置居中显示
                if prob[i][j] != '0':
                    self.table.item(i, j).setFlags(Qt.ItemIsEditable)   # 设置初始不为0的数字不可编辑
                    self.table.item(i, j).setBackground(QBrush(QColor(0, 225, 0)))

    def read_table(self):
        board = []   # 读取table中的数据
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(int(self.table.item(i, j).text()))
            board.append(tmp)
        return board

    def submit(self):
        board = self.read_table()
        if self.isvalid(board):
            QMessageBox.information(self, "提交结果", "玲兰姐姐太棒了~", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "提交结果", "玲兰姐姐再看看~", QMessageBox.Yes)

    def next_(self):   # 将关卡数字 + 1，然后执行重置模块
        board = self.read_table()
        if not self.isvalid(board):
            QMessageBox.critical(self, "过关失败", "当前结果有问题，无法进入下一关~", QMessageBox.Yes)
        else:
            with open(file=self.path + r'./ziyuan/problem.txt', mode='r') as fr:
                data = list(csv.reader(fr))
            data[0][0] = str(int(data[0][0]) + 1)
            with open(file=self.path + r'./ziyuan/problem.txt', mode='w', newline='') as fw:
                f_csv = csv.writer(fw)
                f_csv.writerows(data)
            self.reset()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = game()   # 创建窗体对象
    MainWindow.show()   # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程