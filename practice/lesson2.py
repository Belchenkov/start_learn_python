from tkinter import *
# from tkinter import ttk

root = Tk()
root.geometry('600x400+1000+200')


def clicked():
    print('Clicked')


# btn = Button(
#     root,
#     text="Кнопка",
#     command=clicked,
#     font="Arial 17 italic"
# )
# btn = Button(
#     root,
#     text="Кнопка",
#     command=clicked,
#     font=("Comic Sans MS", 20)
# )
#
btn = Button(
    root,
    text="Кнопка",
    justify=LEFT
)
btn.configure(width=20, height=5)
btn['font'] = 'Arial 18'
btn.pack()

# btn2 = ttk.Button(root, text="Кнопка")
# btn2.pack()

root.mainloop()