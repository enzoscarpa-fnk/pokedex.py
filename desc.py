import tkinter as tk
import ttkbootstrap as tkb
from tkinter import *

root = tkb.Window(title='Pokédex', resizable=(tkb.NO, tkb.NO))
root.geometry("350x440+1000+150") #temporary

data = [("001", "Il a une étrange graine plantée sur son dos. Elle grandit avec lui depuis la naissance."), ("002", "Son bulbe dorsal devient si gros qu'il ne peut plus se tenir sur ses membres postérieurs.")]

sv_pokemon_description = tkb.StringVar(value="Il a une étrange graine plantée sur son dos. Elle grandit avec lui depuis la naissance.")
sv_pokemon_description_p1 = tkb.StringVar(value="")
sv_pokemon_description_p2 = tkb.StringVar(value="")
icn_previous = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/previous.png')
icn_next = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/next.png')
current_page = 1

index = 2
current_index = 0


def key_left(event):
    go_previous()


def key_right(event):
    go_next()


def go_previous():
    global current_index
    if current_index > 0:
        current_index -= 1
        display(current_index)
    else:
        current_index = 0
        display(current_index)


def go_next():
    global current_index
    if current_index < 2 - 1:
        current_index += 1
        display(current_index)


def display(index):
    global current_index
    if 0 <= index < 2:
        current_entry = data[index]
        sv_pokemon_description.set(current_entry[1])
        process_desc()
        current_index = index
    print("sv_pokemon_description: (display)", sv_pokemon_description.get())


"""def process_desc():  # 1 row = 23 chars -> 3 rows = 69 chars
    desc_list = [sv_pokemon_description.get()]
    desc_split = []
    buffer_p1 = []
    buffer_p2 = []
    n_char = 0
    p1 = ""
    p2 = ""
    if len(sv_pokemon_description.get()) > 69:
        for line in desc_list:
            desc_split.append(line.split(" "))
        while 0 <= n_char <= 46:
            for word in desc_split[0]:
                word += " "
                char_count = len(word)
                n_char += char_count
                buffer_p1.append(word)
        while 47 <= n_char <= 69:
            for word in desc_split[0]:
                word += " "
                char_count = len(word)
                n_char += char_count
                buffer_p1.append(word)
        while n_char > 69:
            for word in desc_split[0]:
                word += " "
                char_count = len(word)
                n_char += char_count
                buffer_p2.append(word)
        for word in buffer_p1:
            p1 += word
        sv_pokemon_description_p1.set(p1)
        for word in buffer_p2:
            p2 += word
        sv_pokemon_description_p2.set(p2)
    else:
        sv_pokemon_description_p1.set(sv_pokemon_description.get())

    display_page(1)"""


def process_desc():
    desc = sv_pokemon_description.get()
    if len(desc) <= 69:
        sv_pokemon_description_p1.set(desc)
        sv_pokemon_description_p2.set("")
    else:
        words = desc.split()
        p1, p2 = "", ""
        n_char = 0
        buffer_p1 = []
        buffer_p2 = []
        current_line_length = 0
        current_line = 1

        for word in words:
            spaced_word = word + " "
            word_length = len(spaced_word)

            if current_line == 1 and current_line_length + word_length <= 23:
                buffer_p1.append(spaced_word)
                current_line_length += word_length
            elif current_line == 1:
                current_line += 1
                current_line_length = word_length
                buffer_p1.append(spaced_word)
            elif current_line == 2 and current_line_length + word_length <= 23:
                buffer_p1.append(spaced_word)
                current_line_length += word_length
            elif current_line == 2:
                current_line += 1
                current_line_length = word_length
                buffer_p1.append(spaced_word)
            elif current_line == 3 and current_line_length + word_length <= 23:
                buffer_p1.append(spaced_word)
                current_line_length += word_length
            else:
                buffer_p2.append(spaced_word)

        p1 = "".join(buffer_p1).strip()
        p2 = "".join(buffer_p2).strip()

        sv_pokemon_description_p1.set(p1)
        sv_pokemon_description_p2.set(p2)

    display_page(1)


    print("current_index: (process_desc):", current_index)
    print("sv_pokemon_description: (process_desc)", sv_pokemon_description.get())
    #  print("desc_list: (process_desc)", desc_list)
    print("sv_pokemon_description_p1: (process_desc)", sv_pokemon_description_p1.get())
    print("sv_pokemon_description_p2: (process_desc)", sv_pokemon_description_p2.get())


def display_page(page_number):
    global pokemon_description, current_page
    current_page = page_number

    destroy_btn_down()
    destroy_btn_up()
    pokemon_description.destroy()

    current_desc = sv_pokemon_description_p1 if page_number == 1 else sv_pokemon_description_p2

    pokemon_description = tkb.Label(root, textvariable=current_desc, wraplength=325, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
    pokemon_description.place(x=15, y=170)

    if page_number == 1 and len(sv_pokemon_description_p2.get()) > 0:
        show_btn_down()
    elif page_number == 2:
        show_btn_up()


def destroy_btn_up():
    global btn_up
    if btn_up:
        btn_up.destroy()


def destroy_btn_down():
    global btn_down
    if btn_down:
        btn_down.destroy()


def show_btn_down():
    global btn_down
    btn_down = tk.Button(root, image=icn_next, autostyle=False, command=lambda: display_page(2))
    btn_down.place(x=320, y=365, width=16, height=16)
    root.bind("<Down>", key_down)


def show_btn_up():
    global btn_up
    btn_up = tk.Button(root, image=icn_previous, autostyle=False, command=lambda: display_page(1))
    btn_up.place(x=320, y=195, width=16, height=16)
    root.bind("<Up>", key_up)


def key_down(event):
    if current_page == 1:
        destroy_btn_down()
        display_page(2)


def key_up(event):
    if current_page == 2:
        destroy_btn_up()
        display_page(1)


pokemon_description = tkb.Label(root, text="", wraplength=325, font=('Pokémon Red/Blue/Green/Yellow Edition Font', 28))
pokemon_description.place(x=15, y=170)

btn_down = tk.Button(root)
btn_down.place(x=320, y=365, width=16, height=16)
root.bind("<Down>", key_down)

btn_up = tk.Button(root)
btn_up.place(x=320, y=195, width=16, height=16)
root.bind("<Up>", key_up)

display_page(1)

process_desc()

icn_previous = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/previous.png')
btn_previous = tk.Button(root, image=icn_previous, autostyle=False, command=go_previous)
btn_previous.place(x=200, y=365, width=16, height=16)
root.bind("<Left>", key_left)
icn_next = PhotoImage(file=r'/Users/fnk/PycharmProjects/Pokedex/src/sprites/next.png')
btn_next = tk.Button(root, image=icn_next, autostyle=False, command=go_next)
btn_next.place(x=320, y=365, width=16, height=16)
root.bind("<Right>", key_right)

if __name__ == '__main__':
    root.mainloop()