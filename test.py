import tkinter as tk
import ttkbootstrap as tkb
from tkinter import *

root = tkb.Window(title='Pokédex', resizable=(tkb.NO, tkb.NO))
root.geometry("350x440+1000+150") #temporary

sv_pokemon_description = tkb.StringVar(value="Il a une étrange graine plantée sur son dos. Elle grandit avec lui depuis la naissance.")
sv_pokemon_description_p1 = tkb.StringVar(value="")
sv_pokemon_description_p2 = tkb.StringVar(value="")
desc_list = [sv_pokemon_description.get()]
desc_split = []
buffer_p1 = []
buffer_p2 = []
n_char = 0
p1 = ""
p2 = str("")
icn_previous = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/previous.png')
icn_next = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/next.png')
current_page = 1


def process_desc():  # 1 row = 23 chars -> 3 rows = 69 chars
    global desc_list, desc_split, buffer_p1, buffer_p2, n_char, p1, p2
    if len(sv_pokemon_description.get()) > 69:
        for line in desc_list:
            desc_split.append(line.split(" "))
        while n_char < 69:
            for word in desc_split[0]:
                word += str(" ")
                char_count = len(word)
                n_char += char_count
                print("n =", n_char)
                print("ok, count is under 69")
                if n_char > 69:
                    buffer_p2.append(word)
                else:
                    buffer_p1.append(word)
        for word in buffer_p1:
            p1 += word
        sv_pokemon_description_p1.set(p1)
        for word in buffer_p2:
            p2 += word
        sv_pokemon_description_p2.set(p2)
    else:
        sv_pokemon_description_p1.set(sv_pokemon_description.get())

    display_page_1()

    print("desc_list =", desc_list)
    print("desc_split =", desc_split)
    print("len(p1) =", len(p1))
    print("buffer_p1 =", buffer_p1)
    print("buffer_p2 =", buffer_p2)
    print("p1 =", p1)
    print("len(sv_pokemon_description.get()) =", len(sv_pokemon_description.get()))
    print("p2 =", p2)
    print("sv_pokemon_description_p2.get() =", sv_pokemon_description_p2.get())
    print("len(sv_pokemon_description_p2.get()) =", len(sv_pokemon_description_p2.get()))


def display_page_1():
    global pokemon_description, current_page
    current_page = 1
    if len(sv_pokemon_description_p2.get()) > 0:
        show_btn_next()
    else:
        destroy_btn_next()
    destroy_btn_previous()
    pokemon_description.destroy()
    pokemon_description = tkb.Label(root, textvariable=sv_pokemon_description_p1, wraplength=325, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
    pokemon_description.place(x=15, y=170)


def display_page_2():
    global pokemon_description, current_page
    current_page = 2
    print("sv_pokemon_description_p2.get() =", sv_pokemon_description_p2.get())
    destroy_btn_next()
    if len(sv_pokemon_description_p2.get()) > 0:
        destroy_btn_next()
        pokemon_description.destroy()
        pokemon_description = tkb.Label(root, textvariable=sv_pokemon_description_p2, wraplength=325, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
        pokemon_description.place(x=15, y=170)
        show_btn_previous()
    else:
        destroy_btn_previous()


def destroy_btn_previous():
    global btn_previous
    try:
        btn_previous.destroy()
    except:
        pass


def destroy_btn_next():
    global btn_next
    try:
        btn_next.destroy()
    except:
        pass


def show_btn_previous():
    global btn_previous
    btn_previous = tk.Button(root, image=icn_previous, autostyle=False, command=display_page_1)
    btn_previous.place(x=320, y=195, width=16, height=16)
    root.bind("<Up>", key_up)


def show_btn_next():
    global btn_next
    btn_next = tk.Button(root, image=icn_next, autostyle=False, command=display_page_2)
    btn_next.place(x=320, y=365, width=16, height=16)
    root.bind("<Down>", key_down)


def key_down(event):
    if current_page == 1:
        destroy_btn_next()
        display_page_2()


def key_up(event):
    if current_page == 2:
        destroy_btn_previous()
        display_page_1()


pokemon_description = tkb.Label(root, text="", wraplength=325, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
pokemon_description.place(x=15, y=170)

btn_next = tk.Button(root)
btn_next.place(x=320, y=365, width=16, height=16)
root.bind("<Down>", key_down)

btn_previous = tk.Button(root)
btn_previous.place(x=320, y=195, width=16, height=16)
root.bind("<Up>", key_up)

display_page_1()


if __name__ == '__main__':
    process_desc()
    root.mainloop()
