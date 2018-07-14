import Tkinter as tk

class Board(tk.Frame):
    #Pretty much stolen wholesale from a Stackoverflow answer on how to draw a chessboard with Tkinter
    def __init__(self,parent,rows,cols,size,grid,color1='white',color2='black'):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.grid = grid

        canvas_width = size*self.cols
        canvas_height = size*self.rows

        tk.Frame.__init__(self,parent)
        self.canvas = tk.Canvas(self,borderwidth=0,highlightthickness = 0,width = canvas_width,height=canvas_height,
                background = 'bisque')

        self.canvas.pack(side='top',fill='both',expand = True, padx=2,pady=2)

        self.canvas.bind('<Configure>',self.refresh)

    def refresh(self,event):
        xsize = int((event.width-1) / self.cols)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize,ysize)
        color = self.color1

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row+self.rows*col]:
                    color = self.color1
                else:
                    color = self.color2

                x1 = col*self.size
                y1 = row*self.size
                x2 = x1+self.size
                y2 = y1+self.size
                self.canvas.create_rectangle(x1,y1,x2,y2,outline='black',fill=color)


def has_repeat_digits(number):
    return len(number) != len(set(number))

def has_consecutive_repeat(number):
    for i in range(len(number)-1):
        if number[i]==number[i+1]:
            return True
    return False

def has_consec_digits(number):
    for i in range(len(number)-1):
        if int(number[i]) == int(number[i+1]) -1:
            return True
    return False


def get_num_passwords(digits,repeats_consec = False,return_list = False):
    count = 0
    if return_list: allowed = [0]*10**digits
    for i in range(10**digits):
        number = str(i).zfill(digits)
        if not has_consec_digits(number):
            if not repeats_consec:
                if not has_consecutive_repeat(number):
                    if return_list: allowed[i] = 1
                    count += 1
            else:
                if not has_repeat_digits(number):
                    if return_list: allowed[i] = 1
                    count += 1
    if return_list: return count,allowed #used for drawing the picture, returns a list saying which numbers give valid passwords
    return count 

def print_square(digits,repeats_consec = False):
    
    if digits%2 != 0: #10^n is only a square if n is even
        return ''
    rows = 10**(digits/2)
    cols = 10**(digits/2)
    board = get_num_passwords(digits,return_list = True,repeats_consec=repeats_consec)[1]
    root = tk.Tk()

    board = Board(root,rows,cols,1,board)
    board.pack(side = 'top',fill='both',expand='true',padx=4,pady=4)
    root.mainloop()


for i in range(7):
    #get a table of numbers of allowed passwords with the different rules
    num_any_repeats = get_num_passwords(i)
    num_consec_repeats = get_num_passwords(i,True)
    print '%d | %d | %d %.2f | %d %.2f' %(i,10**i,num_consec_repeats,num_consec_repeats/10.0**(i-2),num_any_repeats,num_any_repeats/10.0**(i-2))

print_square(4,False)
