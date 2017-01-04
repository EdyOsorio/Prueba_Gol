from tkinter import *
x=600
y=170
tk =Tk()
canvas = Canvas(tk, width=500 , height=500)
canvas.pack()
my_image = PhotoImage(file="balon.png")
my_image2 = PhotoImage(file='Arco.png')

canvas.create_image(350,170,anchor=NW, image=my_image)
canvas.create_image(0,100,anchor=NW, image=my_image2)


def mover(event):
    if event.keysym =='Left':
        global x
        global y
        canvas.move(1,-3,0)
        x=x-3
        print('(',x,',',y,')')
        if x<=470:
            print('...!!!GOOLL')
    else:
        global x
        global y
        x=x+3
        canvas.move(1,3,0)
        print('(',x,',',y,')')

canvas.bind_all('<KeyPress-Left>',mover)
canvas.bind_all('<KeyPress-Right>',mover)

tk.mainloop()
