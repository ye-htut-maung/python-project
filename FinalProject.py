from tkinter.ttk import *
from tkinter import *
from random import *

from tkinter import messagebox


global point_of_game

window = Tk()
window.title("Gambling Game")
window.geometry('400x400')


def welcome_page():
    global point_of_game
    frame_welcome = Frame(window)
    frame_welcome.place(x=0, y=0, width=400, height=400)
    welcome_lbl = Label(frame_welcome, fg="dimgray",
                        text="Welcome to Gambling Game\nFirst, you need to top up your point\nTo top up, please press continue button\n",
                        font=('Monaco', 16))

    welcome_lbl.pack()

    def to_first_page():
        frame_welcome.destroy()
        Top_Up_page()

    point_of_game = 0
    welcome_btn = Button(frame_welcome, text="Continue", command=to_first_page, fg="dimgray", height=3, width=9,
                         font=("Monaco", 16))
    welcome_btn.pack()


def Top_Up_page():
    global point_of_game

    frame_of_first_page = Frame(window)

    frame_of_first_page.place(x=0, y=0, width=400, height=400)
    ask_user_to_change_point = Label(frame_of_first_page,
                                     text="Point(then) : {}\nTop Up\nWe have now 10% discount\nPlease input your cash\n"
                                          "|\n"
                                          "|\n"
                                          "\  |  /\n"
                                          "\ | /\n"
                                          "\|/".format(point_of_game), fg="dodgerblue", font=('Monaco', 16))
    ask_user_to_change_point.pack()

    cash_input = Entry(frame_of_first_page, width=10, justify='center', fg="dodgerblue",
                       font=("Monaco", 16))  # cash to point entry
    cash_input.pack()
    cash_input.focus()

    def show_point():
        global point_of_game
        user_point_get = int(cash_input.get())

        user_point = user_point_get + (user_point_get // 10)
        point_of_game += user_point
        show_changed_point = Label(frame_of_first_page, text="Your point is(now) : {}".format(point_of_game),
                                   fg="dodgerblue", font=('Monaco', 16))
        show_changed_point.pack()

        def check1():
            frame_of_first_page.destroy()
            menu()

        btn_of_next_first_page = Button(frame_of_first_page, text="Continue", height=2, width=14, command=check1,
                                        fg="dodgerblue",
                                        font=("Monaco", 16))
        btn_of_next_first_page.pack()

    btn_of_first_page = Button(frame_of_first_page, text="Top Up", command=show_point, height=2, width=14,
                               fg="dodgerblue",
                               font=("Monaco", 16)
                               )  # cash to point btn
    btn_of_first_page.pack()


def menu():
    global point_of_game
    frame_for_menu = Frame(window)
    frame_for_menu.place(x=0, y=0, width=400, height=400)
    lbl_menu = Label(frame_for_menu, text="MENU", fg="chocolate")
    lbl_menu.config(font=("Courier", 55))
    lbl_menu.pack()

    lbl_show_point = Label(frame_for_menu, text="Point : {}".format(point_of_game), fg="chocolate",
                           font=("Courier", 17))
    lbl_show_point.pack()

    def to_game_1():
        frame_for_menu.destroy()
        game_1()

    def to_game_2():
        frame_for_menu.destroy()
        game_2()

    def to_exit():
        frame_for_menu.destroy()
        redeem()

    def to_refill_point():
        frame_for_menu.destroy()
        Top_Up_page()

    game_1_btn = Button(frame_for_menu, text="Game1", command=to_game_1, height=3, width=20, fg="chocolate",
                        font=("Courier", 22))
    game_2_btn = Button(frame_for_menu, text="Game2", command=to_game_2, height=3, width=20, fg="chocolate",
                        font=("Courier", 22))
    game_refill_point = Button(frame_for_menu, text="Top Up Points", command=to_refill_point, height=3, width=20,
                               fg="chocolate", font=("Courier", 22))
    game_exit_btn = Button(frame_for_menu, text="Redeem & Exit", command=to_exit, height=3, width=20, fg="chocolate",
                           font=("Courier", 22))
    game_1_btn.pack()
    game_2_btn.pack()
    game_refill_point.pack()
    game_exit_btn.pack()


def game_1():
    global point_of_game
    global die, roll_die_game_1
    global game1_point
    frame_for_game_1 = Frame(window)
    frame_for_game_1.place(x=0, y=0, width=400, height=400)

    def game_1_submit():
        global point_of_game
        global game1_point
        global die, roll_die_game_1
        game1_point = int(input_for_game1_point.get())
        if game1_point > point_of_game:
            messagebox.showerror("Error", "You don't enough point\nPlease top up your point")
            frame_for_game_1.destroy()
            menu()
        elif game1_point == 0:
            messagebox.showerror("Error", "You can't play with 0 point")
            frame_for_game_1.destroy()
            game_1()
        else:
            point_of_game -= game1_point
            roll_die_game_1 = int(spin_game1_1_6.get())
            die = randint(1, 6)
            if roll_die_game_1 == die:
                frame_for_game_1.destroy()
                win_game_1()
            elif roll_die_game_1 != die:
                frame_for_game_1.destroy()
                lose_game_1()

    lbl_for_game_1 = Label(frame_for_game_1, fg="darkcyan",
                           text="WELCOME TO GAME 1\nUse Die - 1\nChoose 1 - 6\nIf the number = the die,\n you'll get 5x of you point\nOr lose your point\n"
                                "Please enter the amount of point\nBetween(1 ~ {})\n|\n\/".format(point_of_game),
                           font=("Monaco", 16))
    lbl_for_game_1.pack()
    input_for_game1_point = Entry(frame_for_game_1, width=10, fg="darkcyan", font=("Monaco", 16))
    input_for_game1_point.insert(END, '0')
    input_for_game1_point.pack()
    input_for_game1_point.focus()

    lbl_game1_1_6 = Label(frame_for_game_1, text="Please choose numbers from 1 to 6", fg="darkcyan",
                          font=("Monaco", 16))
    lbl_game1_1_6.pack()

    spin_game1_1_6 = Spinbox(frame_for_game_1, from_=1, to=6, width=7, fg="darkcyan", font=("Monaco", 16))
    spin_game1_1_6.pack()

    game_1_submit_btn = Button(frame_for_game_1, text="Submit", height=2, width=14, command=game_1_submit,
                               fg="darkcyan",
                               font=("Monaco", 16))
    game_1_submit_btn.pack()


def win_game_1():
    global game1_point
    global point_of_game
    global die, roll_die_game_1
    frame_win_game_1 = Frame(window)
    frame_win_game_1.place(x=0, y=0, width=400, height=400)

    point_of_game += game1_point * 5

    if die == 1:
        lbl_die = Label(frame_win_game_1, text=" -----------\n"
                                               "|           |\n"
                                               "|     O     |\n"
                                               "|           |\n"
                                               " ----------", fg="darkgreen", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 2:
        lbl_die = Label(frame_win_game_1, text=" -----------\n"
                                               "|   O       |\n"
                                               "|           |\n"
                                               "|       O   |\n"
                                               " -----------", fg="darkgreen", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 3:
        lbl_die = Label(frame_win_game_1, text=" -----------\n"
                                               "|   O       |\n"
                                               "|     O     |\n"
                                               "|       O   |\n"
                                               " -----------", fg="darkgreen", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 4:
        lbl_die = Label(frame_win_game_1, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|           |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkgreen", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 5:
        lbl_die = Label(frame_win_game_1, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|     O     |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkgreen", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 6:
        lbl_die = Label(frame_win_game_1, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|  O     O  |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkgreen", font=("Monaco", 16))
        lbl_die.pack()
    lbl_win_game_1 = Label(frame_win_game_1,
                           text="Die is {}\nYou choose {}\nYou win!\nPoint of game: {}".format(die, roll_die_game_1,
                                                                                               point_of_game),
                           fg="darkgreen", font=("Monaco", 16))
    lbl_win_game_1.pack()

    def to_game_1():
        frame_win_game_1.destroy()
        game_1()

    btn_play_again_game_1 = Button(frame_win_game_1, text="Play again?", command=to_game_1, width=15, height=2,
                                   fg="darkgreen", font=("Monaco", 16))
    btn_play_again_game_1.pack()

    def to_menu():
        frame_win_game_1.destroy()
        menu()

    btn_menu_from_game_1 = Button(frame_win_game_1, text="Menu", command=to_menu, width=15, height=2, fg="darkgreen",
                                  font=("Monaco", 16))
    btn_menu_from_game_1.pack()


def lose_game_1():
    global point_of_game
    global die, roll_die_game_1
    frame_lose_game_1 = Frame(window)
    frame_lose_game_1.place(x=0, y=0, width=400, height=400)
    if die == 1:
        lbl_die = Label(frame_lose_game_1, text=" -----------\n"
                                                "|           |\n"
                                                "|     O     |\n"
                                                "|           |\n"
                                                " ----------", fg="darkslategray", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 2:
        lbl_die = Label(frame_lose_game_1, text=" -----------\n"
                                                "|   O       |\n"
                                                "|           |\n"
                                                "|       O   |\n"
                                                " -----------", fg="darkslategray", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 3:
        lbl_die = Label(frame_lose_game_1, text=" -----------\n"
                                                "|   O       |\n"
                                                "|     O     |\n"
                                                "|       O   |\n"
                                                " -----------", fg="darkslategray", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 4:
        lbl_die = Label(frame_lose_game_1, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|           |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="darkslategray", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 5:
        lbl_die = Label(frame_lose_game_1, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|     O     |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="darkslategray", font=("Monaco", 16))
        lbl_die.pack()
    elif die == 6:
        lbl_die = Label(frame_lose_game_1, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|  O     O  |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="darkslategray", font=("Monaco", 16))
        lbl_die.pack()
    lbl_lose_game_1 = Label(frame_lose_game_1,
                            text="Die is {}\nYou choose{}\nYou lose!\npoint of game: {}".format(die, roll_die_game_1,
                                                                                                point_of_game),
                            fg="darkslategray", font=("Monaco", 16))
    lbl_lose_game_1.pack()

    def to_game_1():
        frame_lose_game_1.destroy()
        game_1()

    btn_play_again_game_1 = Button(frame_lose_game_1, text="Play again?", command=to_game_1, width=15, height=2,
                                   fg="darkslategray", font=("Monaco", 16))
    btn_play_again_game_1.pack()

    def to_menu():
        frame_lose_game_1.destroy()
        menu()

    btn_menu_from_game_1 = Button(frame_lose_game_1, text="Menu", command=to_menu, width=15, height=2,
                                  fg="darkslategray", font=("Monaco", 16))
    btn_menu_from_game_1.pack()


def game_2():
    global point_of_game
    global game2_point
    global die2, roll_die_game_2
    global die2_1, die2_2
    frame_for_game_2 = Frame(window)
    frame_for_game_2.place(x=0, y=0, width=400, height=400)

    lbl_for_game_2 = Label(frame_for_game_2,
                           text="WELCOME TO GAME 2\nUse Die - 2\nChoose 2 - 12\nIf the number = the die,\n you'll get 10x of you point\nOr lose your point\n"
                                "Please enter the amount of point\nBetween(1 ~ {})\n|\n\/".format(point_of_game),
                           fg="maroon", font=("Monaco", 16))
    lbl_for_game_2.pack()

    input_for_game2_point = Entry(frame_for_game_2, width=10, fg="maroon", font=("Monaco", 16))
    input_for_game2_point.insert(END, '0')
    input_for_game2_point.pack()
    input_for_game2_point.focus()

    lbl_game2_2_12 = Label(frame_for_game_2, text="Please choose numbers from 2 to 12", fg="maroon",
                           font=("Monaco", 16))
    lbl_game2_2_12.pack()

    spin_game2_2_12 = Spinbox(frame_for_game_2, from_=2, to=12, width=5, fg="maroon", font=("Monaco", 16))
    spin_game2_2_12.pack()

    def game_2_submit():
        global point_of_game
        global game2_point
        global die2, roll_die_game_2
        global die2_1, die2_2
        game2_point = int(input_for_game2_point.get())
        if game2_point > point_of_game:
            messagebox.showerror("Error", "You don't enough point\nPlease top up your point")
            frame_for_game_2.destroy()
            menu()
        elif game2_point == 0:
            messagebox.showerror("Error", "You can't play with 0 point")
            frame_for_game_2.destroy()
            game_2()
        else:
            point_of_game -= game2_point
            roll_die_game_2 = int(spin_game2_2_12.get())
            die2_1 = randint(1, 6)
            die2_2 = randint(1, 6)
            die2 = die2_1 + die2_2
            if roll_die_game_2 == die2:
                frame_for_game_2.destroy()
                win_game_2()
            elif roll_die_game_2 != die2:
                frame_for_game_2.destroy()
                lose_game_2()

    game_2_submit_btn = Button(frame_for_game_2, text="Submit", height=2, width=14, command=game_2_submit, fg="maroon",
                               font=("Monaco", 16))
    game_2_submit_btn.pack()


def win_game_2():
    global game2_point
    global point_of_game
    global die2, roll_die_game_2
    global die2_1, die2_2
    frame_win_game_2 = Frame(window)
    frame_win_game_2.place(x=0, y=0, width=400, height=400)

    point_of_game += game2_point * 10

    if die2_1 == 1:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|           |\n"
                                               "|     O     |\n"
                                               "|           |\n"
                                               " ----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 2:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|   O       |\n"
                                               "|           |\n"
                                               "|       O   |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 3:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|   O       |\n"
                                               "|     O     |\n"
                                               "|       O   |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 4:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|           |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 5:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|     O     |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 6:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|  O     O  |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    # -------------------
    if die2_2 == 1:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|           |\n"
                                               "|     O     |\n"
                                               "|           |\n"
                                               " ----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 2:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|   O       |\n"
                                               "|           |\n"
                                               "|       O   |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 3:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|   O       |\n"
                                               "|     O     |\n"
                                               "|       O   |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 4:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|           |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 5:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|     O     |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 6:
        lbl_die = Label(frame_win_game_2, text=" -----------\n"
                                               "|  O     O  |\n"
                                               "|  O     O  |\n"
                                               "|  O     O  |\n"
                                               " -----------", fg="darkorange", font=("Monaco", 15))
        lbl_die.pack()

    lbl_win_game_2 = Label(frame_win_game_2,
                           text="Die is {}\nYou choose {}\nYou win!\npoint of game: {}".format(die2, roll_die_game_2,
                                                                                               point_of_game),
                           fg="darkorange", font=("Monaco", 15))
    lbl_win_game_2.pack()

    def to_game_2():
        frame_win_game_2.destroy()
        game_2()

    btn_play_again_game_2 = Button(frame_win_game_2, text="Play again?", command=to_game_2, width=15, height=2,
                                   fg="darkorange", font=("Monaco", 15))
    btn_play_again_game_2.pack()

    def to_menu():
        frame_win_game_2.destroy()
        menu()

    btn_menu_from_game_2 = Button(frame_win_game_2, text="Menu", command=to_menu, width=15, height=2, fg="darkorange",
                                  font=("Monaco", 15))
    btn_menu_from_game_2.pack()


def lose_game_2():
    global point_of_game
    global die2, roll_die_game_2
    global die2_1, die2_2
    frame_lose_game_2 = Frame(window)
    frame_lose_game_2.place(x=0, y=0, width=400, height=400)

    if die2_1 == 1:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|           |\n"
                                                "|     O     |\n"
                                                "|           |\n"
                                                " ----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 2:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|   O       |\n"
                                                "|           |\n"
                                                "|       O   |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 3:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|   O       |\n"
                                                "|     O     |\n"
                                                "|       O   |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 4:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|           |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 5:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|     O     |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_1 == 6:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|  O     O  |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    # -------------------
    if die2_2 == 1:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|           |\n"
                                                "|     O     |\n"
                                                "|           |\n"
                                                " ----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 2:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|   O       |\n"
                                                "|           |\n"
                                                "|       O   |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 3:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|   O       |\n"
                                                "|     O     |\n"
                                                "|       O   |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 4:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|           |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 5:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|     O     |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()
    elif die2_2 == 6:
        lbl_die = Label(frame_lose_game_2, text=" -----------\n"
                                                "|  O     O  |\n"
                                                "|  O     O  |\n"
                                                "|  O     O  |\n"
                                                " -----------", fg="mediumvioletred", font=("Monaco", 15))
        lbl_die.pack()

    lbl_lose_game_2 = Label(frame_lose_game_2,
                            text="Die is {}\nYou choose{}\nYou lose!\npoint of game: {}".format(die2, roll_die_game_2,
                                                                                                point_of_game),
                            fg="mediumvioletred", font=("Monaco", 15))
    lbl_lose_game_2.pack()

    def to_game_2():
        frame_lose_game_2.destroy()
        game_2()

    btn_play_again_game_2 = Button(frame_lose_game_2, text="Play again?", width=15, height=2, command=to_game_2,
                                   fg="mediumvioletred", font=("Monaco", 15))
    btn_play_again_game_2.pack()

    def to_menu():
        frame_lose_game_2.destroy()
        menu()

    btn_menu_from_game_2 = Button(frame_lose_game_2, text="Menu", width=15, height=2, command=to_menu,
                                  fg="mediumvioletred", font=("Monaco", 15))
    btn_menu_from_game_2.pack()


def redeem():
    global point_of_game
    frame_redeem = Frame(window)
    frame_redeem.place(x=0, y=0, width=400, height=400)
    lbl_redeem = Label(frame_redeem,
                       text="You have {} points\nSo, you get {} cash back\nThank for playing gambling game!\nUwU".format(
                           point_of_game, point_of_game), fg="purple", font=("Monaco", 18))
    lbl_redeem.pack()
    btn_redeem = Button(frame_redeem, text="Get & Exit", command=window.destroy, height=2, width=14, fg="purple",
                        font=("Monaco", 18))
    btn_redeem.pack()


welcome_page()

mainloop()
