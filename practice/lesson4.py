from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

# l = Label(root, text='Текст в строке 1\nСтрока 2\nСтрока 3\nСтрока 4\nСтрока 5\nСтрока 6',
#           bg='green',
#           fg='#fff',
#           font=("Comic Sans MS", 10, "bold"),
#           justify=LEFT,
#           width=50,
#           anchor='sw'
#           )
# l.pack()


img = PhotoImage(file='python.ico')
l_logo = Label(root, image=img)
l_logo.pack()

root.mainloop()