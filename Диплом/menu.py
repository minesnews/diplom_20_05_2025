from tkinter import *
from tkinter import ttk
import os
import sys
import generation_content as generator
 
root = Tk()
root.title("Главное меню")
root.geometry("250x30") 
root.resizable(False, False)
root.option_add("*tearOff", FALSE)

editor = Text()
editor.pack(expand=1, fill=BOTH)

def gen():
    print(generator.cleanhtml(generator.tester))
def exit():
    root.destroy()
    
file_menu = Menu()
file_menu.add_command(label="Выйти", command=exit)
 
main_menu = Menu()
main_menu.add_cascade(label="Файл", menu=file_menu)
 
root.config(menu=main_menu)

btn = ttk.Button(editor, text="Сгенерировать тест", command=gen)
editor.window_create("1.0", window=btn)

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

root.iconbitmap(f'{script_directory}\\fipi.ico')
root.mainloop()

