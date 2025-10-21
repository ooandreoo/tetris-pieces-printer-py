from piece.piece import Piece
from tools.piece_generator import PieceGenerator

import os
import time
import threading
import sys
import select
import termios
import tty

class Board:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.matrix = [[0 for _ in range(height)] for _ in range(width)]
        self.piece_generator = PieceGenerator(height,width)
        self.piece = None
        self.key_pressed = None
        self.running = True
        self.gravity_delay = 1
        self.gravity_increase_multiplier = 40
        self.minimum_gravity_delay = 0.3
        self.game_computing_speed = 0.2

    def add_piece(self):
        self.piece = self.piece_generator.generate_piece()

    def piece_reached_bottom(self):
        for point in self.piece.get_positions():
            if(point[1] == 0):
                return True
        return False

    def piece_reached_wall_at_left(self):
        for point in self.piece.get_positions():
            if(point[0] == 0):
                return True
        return False

    def piece_reached_wall_at_right(self):
        for point in self.piece.get_positions():
            if(point[0] == self.width-1):
                return True
        return False

    def adjust_piece_if_overboard(self):
        # we are not handling going overboard at the bottom, just sideways
        positions = self.piece.get_positions()
        positions.sort()
        right_overboard = positions.pop()[0]
        left_overboard = positions[0][0]
        if(left_overboard<0):
            for i in range(abs(left_overboard)):
                self.piece.move("right")
        elif(right_overboard>=self.width):
            for i in range(right_overboard+1-self.width):
                self.piece.move("left")
    def move_piece(self):
        if(self.key_pressed != None):
            if(self.key_pressed=="a" and not self.piece_reached_wall_at_left()):
                self.piece.move("left")
            elif(self.key_pressed=="d" and not self.piece_reached_wall_at_right()):
                self.piece.move("right")
            elif(self.key_pressed=="s"):
                self.tick()
            elif(self.key_pressed=="w"):
                self.piece.rotate("right",90)
                self.adjust_piece_if_overboard()
            self.key_pressed = None

    def start_loop(self):
        self.start_input_thread()
        self.start_gravity_thread()
        self.add_piece()
        while self.running:
            self.move_piece()
            self.draw()
            time.sleep(self.game_computing_speed)


    def tick(self):
        if(self.piece == None or self.piece_reached_bottom()):
            self.add_piece()
        else:
            self.piece.move()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def read_input(self):
        while self.running:
            self.key_pressed = self.getch()
            if(self.key_pressed == "q"):
                self.running = False

    def move_piece_down(self):
        counter = 0
        while self.running:
            counter+=1
            self.tick()
            time.sleep(self.gravity_delay)
            if(self.gravity_delay > self.minimum_gravity_delay and counter % self.gravity_increase_multiplier==0):
                self.gravity_delay -= 0.1

    def start_gravity_thread(self):
        gravity = threading.Thread(target=self.move_piece_down)
        gravity.daemon = True
        gravity.start()

    def start_input_thread(self):
        thread = threading.Thread(target=self.read_input)
        thread.daemon = True
        thread.start()

    def draw(self):
        self.clear()
        piece_positions = self.piece.get_positions()
        piece_positions.sort()

        print("(a) left     (d) right   (s) down  (w) rotate   (q) quit\r")
        print("--- START OF BOARD ---\r")
        j = self.height-1
        for _ in range(self.height):
            line = "|"
            #print(len(self.matrix))
            for i in range(self.width):
                #print(i,j)
                if(len(piece_positions)>0 and (i,j) in piece_positions):
                    line+=" #"
                else: # we still need to add a condition in case this position has 1 or 0
                    if self.matrix[i][j] == 0:
                        line+="  "
                    else:
                        line+=" #"
            j-=1
            print(line,"|\r")
        print("--- END OF BOARD ---\r")
        print("last key pressed: ",self.key_pressed,"\r")

