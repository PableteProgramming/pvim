from buffer import *

def pvim(scr, *args):
    curses.curs_set(0)
    height, width= scr.getmaxyx() 
    #width= curses.COLS
    buff= Buffer(scr,1,1,width-1,height-1)
    buff.showCursor(True)
    buff.print("width: "+str(width)+"; height: "+str(height))
    buff.print("Hi")
    buff.print("Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    buff.refresh()
    
    while True:
        # stay in this loop till the user presses 'q'
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
