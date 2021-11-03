import curses
import time
import threading
from cursor import *

class Buffer:
    def __init__(self,_instance,_x,_y,_width,_height):
        #self.running=True
        self.CShow=True
        self.instance= _instance
        self.height=_height
        self.width=_width
        self.x=_x
        self.y=_y
        self.cursor= Cursor(0,0)
        self.buff= []
        for y in range(self.height):
            xr= []
            for x in range(self.width):
                xr.append(" ")
            self.buff.append(xr)
        #blinking= threading.Thread(target=self.CursorBlink)
        #blinking.start()
    
    '''not working yet'''
    def CursorBlink(self):
        on=True
        while self.running:
            if on:
                #off
                #draw the current char at this buffer position
                self.instance.addstr(self.cursor.y,self.cursor.x,self.buff[self.cursor.y][self.cursor.x],curses.A_NORMAL)
                on=False
            else:
                #on
                #draw the cursor
                self.instance.addstr(self.cursor.y,self.cursor,x,"$",curses.A_BOLD)
                on=True
            self.instance.refresh()
            time.sleep(1)
    ''' ---------------'''

    def UpdateCursor(self):
        if self.cursor.x>= self.width:
            self.cursor.x= self.width-1
        if self.cursor.x < 0:
            self.cursor.x=0
        if self.cursor.y >= self.height:
            self.cursor.y=self.height-1
        if self.cursor.y <0 :
            self.cursor.y=0


    def drawBuff(self):
        for y in range(len(self.buff)):
            for x in range(len(self.buff[y])):
                try:
                    self.instance.addstr(self.y+y,self.x+x,self.buff[y][x],curses.A_NORMAL)
                except curses.error:
                    pass

    def showCursor(self,b):
        if b:
            #show cursor
            self.CShow=True
        else:
            #hide cursor
            self.CShow=False

    def refresh(self):
        self.UpdateCursor()
        self.instance.clear()
        self.drawBuff()
        if self.CShow:
            #print cursor:
            self.instance.addstr(self.cursor.y+self.y,self.cursor.x+self.x,"$",curses.A_BOLD)
        self.instance.refresh()

    def print(self,s):
        #print depending on cursor pos
        for c in s:
            self.printCh(c)
        self.UpdateCursor()

    def printCh(self,c):
        self.buff[self.cursor.y][self.cursor.x]=c
        self.cursor.x+=1
        if self.cursor.x >= self.width:
            self.cursor.x=0
            self.cursor.y+=1
            
