from tkinter import *

root = Tk()
root.title('Мое первое GUI приложение')
root.iconbitmap('python.ico')
root.geometry('600x400+1000+200')
root.resizable(False, False)
# root.config(bg='#fff')
root['bg'] = 'white'
root.mainloop()