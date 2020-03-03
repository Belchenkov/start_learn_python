from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')
root.title('Python Notepad')

main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label="File")
# main_menu.add_command(label="About")

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход")
main_menu.add_cascade(label="Файл", menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="О программе")

help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Онлайн")
help_menu_sub.add_command(label="Офлайн")

help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
main_menu.add_cascade(label="Справка", menu=help_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

t = Text(
    f_text,
    bg="#343D46",
    fg="#C6DEC1",
    padx=10, pady=10,
    wrap=WORD,
    width=30,
    insertbackground="#EDA756",
    selectbackground="#4E5A65",
    spacing3=10
)
t.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()