from buffer import *

def pvim(scr, *args):
    # -- Perform an action with Screen --
    #scr.border(0)
    #scr.addstr(5, 5, 'Hello from Curses!', curses.A_BOLD)
    #scr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)
    curses.curs_set(0)
    buff= Buffer(scr,0,0,curses.COLS,curses.LINES)
    buff.showCursor(True)
    buff.print("Hi")
    buff.cursor.x=10
    buff.print("Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    #buff.cursor.x=buff.cursor.x+10
    #buff.print("Lul")
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
        else:
            buff.print(chr(ch))
            refresh=True

        if refresh:
            buff.refresh()


if __name__=="__main__":
    curses.wrapper(pvim)
