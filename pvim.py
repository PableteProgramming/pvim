import curses

class Cursor:
    def __init__(self,_x,_y):
        self.x=_x
        self.y=_y

class Buffer:
    def __init__(self,_instance,_x,_y,_width,_height):
        self.CShow=True
        self.instance= _instance
        self.height=_height
        self.width=_width
        self.x=_x
        self.y=_y
        self.cursor= Cursor(0,0)
        self.buff= [[]]
        for y in range(self.height):
            xr= []
            for x in range(self.width):
                xr.append(" ")
            self.buff.append(xr)

    def drawBuff(self):
        for y in range(len(self.buff)):
            for x in range(len(y)):
                self.instance.addstr(y,x,self.buff[y][x],curses.A_NORMAL)

    def showCursor(self,b):
        if b:
            #show cursor
            self.CShow=True
        else:
            #hide cursor
            self.CShow=False

    def refresh(self):
        self.instance.clear()
        self.drawBuff()
        if self.CShow:
            #print cursor:
            self.instance.addstr(self.cursor.y+self.y,self.cursor.x+self.x,"$",curses.A_BOLD)
        self.instance.refresh()

    def print(self,s):
        #print depending on cursor pos
        self.cursor.x+= len(s)
        while True:
            if self.cursor.x> self.width:
                self.cursor.x= self.cursor.x-self.width
                self.cursor.y+= 1
            else:
                break
        self.buff[self.cursor.y+self.y][self.cursor.x+self.x]= s
        

def pvim(scr, *args):
    # -- Perform an action with Screen --
    #scr.border(0)
    #scr.addstr(5, 5, 'Hello from Curses!', curses.A_BOLD)
    #scr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)
    buff= Buffer(scr,0,0,curses.COLS,curses.LINES)
    buff.showCursor(True)
    buff.print("Hi")
    #buff.cursor.x=10
    buff.print("Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    buff.cursor.x=buff.cursor.x+10
    buff.print("Lul")
    buff.refresh()
    
    while True:
        # stay in this loop till the user presses 'q'
        #scr.addstr(0,0,"lul",curses.A_BOLD)
        refresh= False
        ch = scr.getch()
        if ch == ord("w"):
            buff.cursor.y-=1
            refresh=True
        elif ch == ord("s"):
            buff.cursor.y+=1
            refresh=True
        elif ch == ord("d"):
            buff.cursor.x+=1
            refresh=True
        elif ch == ord("a"):
            buff.cursor.x-=1
            refresh=True
        elif ch == ord("q"):
            break

        if refresh:
            buff.refresh()


if __name__=="__main__":
    curses.wrapper(pvim)
