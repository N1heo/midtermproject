import tkinter.messagebox
from tkinter import *
from random import choice


class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        '''
       c - canvas instance
       n - number of rows
       m - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       walls - if True matrix should have 0's surrounded by 1's (walls)
       example
       1 1 1 1
       1 0 0 1
       1 1 1 1
       '''
        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(choice([0, 0, 0, 1, 2, 3, 2, 3]))
        # Random preset

        # x,y = randint(1,39),randint(1,39)
        # for l in range(1,3):
        #     self.a[x][y] = 1
        #     self.a[x-l][y-l] = 1
        #     self.a[x-l][y] = 1
        #     self.a[x-l][y+l] = 1
        #     self.a[x][y-l] = 1
        #     self.a[x][y+l] = 1
        #     self.a[x+l][y-l] = 1
        #     self.a[x+l][y] = 1
        #     self.a[x+l][y+l] = 1
        self.__draw()

# All the methods, that take input from user:

    def left_click(self, event):
        for i in range(1, 3):
            self.a[event.x//20+1][event.y//20+1] = 1
            self.a[event.x//20+1-i][event.y//20+1-i] = 1
            self.a[event.x//20+1-i][event.y//20+1] = 1
            self.a[event.x//20+1-i][event.y//20+1+i] = 1
            self.a[event.x//20+1][event.y//20+1-i] = 1
            self.a[event.x//20+1][event.y//20+1+i] = 1
            self.a[event.x//20+1+i][event.y//20+1-i] = 1
            self.a[event.x//20+1+i][event.y//20+1] = 1
            self.a[event.x//20+1+i][event.y//20+1+i] = 1

    def right_click(self, event):
        for i in range(1, 3):
            self.a[event.x//20+1][event.y//20+1] = 2
            self.a[event.x//20+1-i][event.y//20+1-i] = 2
            self.a[event.x//20+1-i][event.y//20+1] = 2
            self.a[event.x//20+1-i][event.y//20+1+i] = 2
            self.a[event.x//20+1][event.y//20+1-i] = 2
            self.a[event.x//20+1][event.y//20+1+i] = 2
            self.a[event.x//20+1+i][event.y//20+1-i] = 2
            self.a[event.x//20+1+i][event.y//20+1] = 2
            self.a[event.x//20+1+i][event.y//20+1+i] = 2

    def middle_click(self, event):
        for i in range(1, 3):
            self.a[event.x//20+1][event.y//20+1] = 3
            self.a[event.x//20+1-i][event.y//20+1-i] = 3
            self.a[event.x//20+1-i][event.y//20+1] = 3
            self.a[event.x//20+1-i][event.y//20+1+i] = 3
            self.a[event.x//20+1][event.y//20+1-i] = 3
            self.a[event.x//20+1][event.y//20+1+i] = 3
            self.a[event.x//20+1+i][event.y//20+1-i] = 3
            self.a[event.x//20+1+i][event.y//20+1] = 3
            self.a[event.x//20+1+i][event.y//20+1+i] = 3

    def delete_click(self, event):
        for i in range(1, 3):
            self.a[event.x//20+1][event.y//20+1] = 0
            self.a[event.x//20+1-i][event.y//20+1-i] = 0
            self.a[event.x//20+1-i][event.y//20+1] = 0
            self.a[event.x//20+1-i][event.y//20+1+i] = 0
            self.a[event.x//20+1][event.y//20+1-i] = 0
            self.a[event.x//20+1][event.y//20+1+i] = 0
            self.a[event.x//20+1+i][event.y//20+1-i] = 0
            self.a[event.x//20+1+i][event.y//20+1] = 0
            self.a[event.x//20+1+i][event.y//20+1+i] = 0

    def helper(self, event):
        tkinter.messagebox.showinfo(title='Helper', message='''
        Press space to launch simulation
        Press P to pause it
        Left click - add white cells
        Right click - add viruses
        Middle click - add bacteria
        D on keyboard - delete''')

###

    def __step(self):
        # The whole magic happens here
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)

        for i in range(3, self.n - 3):
            for j in range(3, self.m - 3):
                neib_sum1 = (str(self.a[i - 1][j - 1]) + str(self.a[i - 1][j])
                             + str(self.a[i - 1][j + 1])
                             + str(self.a[i][j - 1])
                             + str(self.a[i][j + 1])
                             + str(self.a[i + 1][j - 1])
                             + str(self.a[i + 1][j])
                             + str(self.a[i + 1][j + 1]))
                neib_sum2 = (str(self.a[i - 2][j - 2]) + str(self.a[i - 2][j])
                             + str(self.a[i - 2][j + 2])
                             + str(self.a[i][j - 2])
                             + str(self.a[i][j + 2])
                             + str(self.a[i + 2][j - 2])
                             + str(self.a[i + 2][j])
                             + str(self.a[i + 2][j + 2]))
                neib_sum3 = (str(self.a[i - 3][j - 3]) + str(self.a[i - 3][j])
                             + str(self.a[i - 3][j + 3])
                             + str(self.a[i][j - 3])
                             + str(self.a[i][j + 3])
                             + str(self.a[i + 3][j - 3])
                             + str(self.a[i + 3][j])
                             + str(self.a[i + 3][j + 3]))
                neib_sum = neib_sum1 + neib_sum2 + neib_sum3
                neib_strsum = (self.a[i - 1][j - 1] + self.a[i - 1][j]
                               + self.a[i - 1][j + 1] + self.a[i][j - 1]
                               + self.a[i][j + 1] + self.a[i + 1][j - 1]
                               + self.a[i + 1][j] + self.a[i + 1][j + 1])

                if neib_strsum == 8:
                    b[i][j] = choice([2, 3])
                elif self.a[i][j] == 1:
                    if neib_sum.count('3') > 6:
                        b[i][j] = 0
                    elif neib_sum.count('2') > 6:
                        b[i][j] = 0
                    else:
                        b[i][j] = 1

                        b[i-1][j-1] = 1
                        b[i-1][j] = 1
                        b[i-1][j+1] = 1
                        b[i][j-1] = 1
                        b[i][j+1] = 1
                        b[i+1][j-1] = 1
                        b[i+1][j] = 1
                        b[i+1][j+1] = 1
                else:
                    b[i][j] = self.a[i][j]
                # elif self.a[i][j] ==2:

                # elif self.a[i][j] ==3:

        # for i in range(self.n):
        #     for j in range(self.m):
        #         print(self.a[i][j], end="")
        #     print()
        self.a = b

    # function for printing the matrix (not used)
    # def print_field(self):
    #     for i in range(self.n):
    #         for j in range(self.m):
    #             print(self.a[i][j], end="")
    #         print()

    def __draw(self):
        '''
       draw each element of matrix as a rectangle
       '''
        self.c.create_rectangle(0, 0, 600, 600, fill='grey', outline='')
        self.c.create_rectangle(40, 40, 560, 560, fill='#9a0000', outline='')
        c.create_text(300, 20, text="Cellural simulation, press H for help",
                      fill="white", font=('Helvetica 15 bold'))
        color = "white"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(3, self.n - 3):
            for j in range(3, self.m - 3):
                if (self.a[i][j] == 1):
                    color = "#d0d0d0"  # white cells
                elif (self.a[i][j] == 2):
                    color = '#09146d'  # viruses
                elif (self.a[i][j] == 3):
                    color = '#288624'  # bacteria
                else:
                    color = "#9a0000"
                self.c.create_oval((i-1) * sizen+2, (j-1) * sizem+2, (i) *
                                   sizen-2, (j) * sizem-2, fill=color,
                                   outline='', width=0.1)

        try:
            if self.running is True:
                self.__step()
        except AttributeError:
            pass
        self.c.after(500, self.__draw)

    def start(self, event):
        """Start the game."""
        self.running = True
        print('running')

    def stop(self, event):
        """Stop the game."""
        self.running = False
        print('''
        not running
        ''')


root = Tk()
root.geometry("600x600")
c = Canvas(root, width=600, height=600)

c.pack()


f = Field(c, 30, 30, 600, 600)

root.bind('<Button-1>', f.left_click)  # leftmouse
root.bind('<Button-2>', f.middle_click)  # scroll click
root.bind('<Button-3>', f.right_click)  # rightmouse
root.bind('d', f.delete_click)  # d
root.bind('h', f.helper)  # h
root.bind('<space>', f.start)  # space
root.bind('p', f.stop)  # p


root.mainloop()
