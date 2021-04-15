# БСБО-05-19 Савранский Сергей

class Interpreter:

    def __init__(self, c):
        self.arr = [0] * 30000
        self.ptr = 0
        self.commands = c

    def val_plus(self):
        self.arr[self.ptr] = 0 if self.arr[self.ptr] == 255 else self.arr[self.ptr] + 1

    def val_minus(self):
        self.arr[self.ptr] = 255 if self.arr[self.ptr] == 0 else self.arr[self.ptr] - 1

    def move_right(self):
        self.ptr = 0 if self.ptr + 1 == len(self.arr) else self.ptr + 1

    def move_left(self):
        self.ptr = len(self.arr) - 1 if self.ptr - 1 < 0 else self.ptr - 1

    def val_print(self):
        print(self.arr[self.ptr])

    def run(self):
        in_cycle = False
        actions = {
            '+': self.val_plus,
            '-': self.val_minus,
            '<': self.move_left,
            '>': self.move_right,
            '.': self.val_print
        }

        for c in self.commands:
            if c == '[':
                in_cycle = True
            elif c == ']':
                in_cycle = False
            elif in_cycle:
                while self.arr[self.ptr] != 0:
                    actions.get(c)()
            else:
                actions.get(c)()


commands = input('Commands >> ')
interpreter = Interpreter(commands)
interpreter.run()
