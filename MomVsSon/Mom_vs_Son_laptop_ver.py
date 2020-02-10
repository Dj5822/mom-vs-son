from tkinter import *
import random

# Score and time left.
# The boolean is used to check if text is correct.
score = 0
time_left = 0
text_correct = False
WPM = 0

# Lists for speech
mum_speech = ["Son, why didn't you do your homework?",
              "Son... You are ugly.",
              "Why did you get 'not achieved' for maths.",
              "You are a disgrace.",
              "I told you to wash the dishes!",
              "You spent 10 hours playing games yesterday!",
              "Go to sleep earlier.",
              "Lose some fat son.",
              "Do some more studying.",
              "Play less games!",
              "You broke the TV again...",
              "Clean your room.",
              "You stink, take a shower.",
              "You're going to be late for school!",
              "Stop being so annoying.",
              "Do your homework!",
              "Are your really going to play LoL all day?",
              "You suck at Overwatch.",
              "CSGO? Grow up son.",
              "You never listen, do you?",
              ]

easy_text_choice = ["Sorry", "Please forgive me", "Cupcakes", "Whales",
                    "Gorillas", "Love is in the air", "Jesus is with us",
                    "Life is good", "I am so cool", "I do not understand",
                    "Cheeseburger", "Bananas are tasty",
                    "I regret nothing", "My mum is cool",
                    "Potato", "Hallelujah"]

medium_text_choice = ["I beg for your mercy", "Let's resolve this peacefully",
                      "I don't want to die", "Please don't kill me",
                      "Here, have an apple", "I just followed my destiny",
                      "There is a reason for everything", "There is no need to be angry",
                      "If there is a will there is a way"]

# What is going to be in the instructions
instructions_text = """
You are arguing with your mum.
Your goal to is respond quickly to your mum's
onslaught with whatever word you can think of.
When your mum shouts something in the speech bubble at the top of the screen,
you may choose to respond with any three of the options at the bottom of the screen.
You can respond by typing the option in the entry field.
The more statements you respond to, the higher your score.
The onslaught will continue for 1 minute, which is when your mum will get tired.
Your words per minute and final score will be presented at the end of the game.
Please remember to click on the entry field before starting.
Good luck!
"""

random_text_choice = [easy_text_choice[random.randint(0, 15)], easy_text_choice[random.randint(0, 15)], easy_text_choice[random.randint(0, 15)]]


# When enter event is triggered, the game starts
def start_game(event):
    global entry_field
    global main_screen
    global score
    global time_left
    if time_left == 6000:
        mum_speech_select()
        countdown()

    # When the game ends, resets everything.
    if time_left == 0:
        main_screen.delete("all")
        main_screen.create_text(950 / 2, 300, fill="black", font="Times 100 bold", text="Start Game")
        main_screen.create_text(950 / 2, 400, fill="black", font="Times 20", text="Press enter to start")
        option_screen.configure(text="")
        wpm_label.configure(text="WPM: 0")
        score_display.configure(text="score: 0")
        main_frame.pack_forget()
        start_screen.pack()
        data_reset()


# The timer. Checks the entry field every second to see if requirements are met.
def countdown():
    global time_left
    global timer
    global text_correct
    global score
    global random_text_choice
    if time_left > 0:
        time_left -= 1
        timer.configure(text="Time left: " + str(time_left/100))
        text_correct = False
        option_screen.configure(text="1) " + random_text_choice[0] + "     " +
                                     "2) " + random_text_choice[1] + "     " +
                                     "3) " + random_text_choice[2])
        check_text(entry_field.get())

        if text_correct:
            mum_speech_select()
            score += 1
            score_display.configure(text="score: {}".format(score))
            text_correct = False
            random_text_choice[0] = easy_text_choice[random.randint(0, 15)]
            random_text_choice[1] = easy_text_choice[random.randint(0, 15)]
            random_text_choice[2] = easy_text_choice[random.randint(0, 15)]

        timer.after(10, countdown)

    else:
        end_game()


# Clears the canvas and entry field and then selects a random "mum_speech" from the list.
def mum_speech_select():
    global mum_speech
    global main_screen
    global speech_bubble_image
    main_screen.delete("all")
    entry_field.delete(0, END)
    text = mum_speech[random.randint(0, 19)]
    main_screen.create_image(750, 300, image=bg_room)
    main_screen.create_image(100, 300, image=mom_image)
    main_screen.create_image(850, 300, image=son_image)
    main_screen.create_image(1000, 90, image=speech_bubble_image)
    main_screen.create_image(350, 375, image=thought_bubble)
    main_screen.create_text(950/2, 60, fill="black", font="Times 35", text=text)


# Checks if you have answered the players mother correctly.
def check_text(text):
    global text_correct
    global WPM
    if text == random_text_choice[0] or text == random_text_choice[1]\
            or text == random_text_choice[2]:
        timer.after(0, print_correct)
        timer.after(300, delete_correct)
        WPM += int(len(entry_field.get())/5)
        wpm_label.configure(text="WPM: {}".format(WPM))
        entry_field.delete(0, END)
        text_correct = True


# Prints a massive green 'O' onto the screen.
def print_correct():
    main_screen.create_text(950/2, 250, fill="green", font="Times 500", text="O", tag="correct")


# Removes the massive 'O'.
def delete_correct():
    main_screen.delete("correct")


# Shows the final score when the game ends.
def end_game():
    global main_screen
    global score
    global time_left
    main_screen.delete("all")
    main_screen.create_text(950/2, 300, fill="black", font="Times 70 bold", text="The game has ended.")
    main_screen.create_text(950/2, 400, fill="black", font="Times 20", text="Press enter to continue")
    option_screen.configure(text="Final score: {}      WPM:{}".format(score, WPM))


# Starts the game when 'Play' is pressed.
def start_button_pressed():
    global time_left
    start_screen.pack_forget()
    main_frame.pack()
    time_left = 6000


# Shows the instructions when 'How to Play' is pressed.
def instructions_button_pressed():
    start_screen.pack_forget()
    instructions_label.pack()
    exit_instructions.pack()


# Returns to menu when this button is pressed.
def return_to_menu():
    instructions_label.pack_forget()
    exit_instructions.pack_forget()
    start_screen.pack()


def data_reset():
    global score
    global time_left
    global text_correct
    global WPM
    score = 0
    time_left = 0
    text_correct = False
    WPM = 0


# Ends the game when 'exit' is pressed.
def exit_button_pressed():
    exit()


# Create window
window = Tk()

# Sets the title and makes window not resizable
window.title("Mom VS Son")
window.resizable(width=False, height=False)

# Finds the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Main frame
main_frame = Frame(window)

# Top right frame (Top right section)
top_right_frame = Frame(main_frame)

# Top left frame (Top left section)
top_left_frame = Frame(main_frame)

# Bind event to Return key
window.bind('<Return>', start_game)

# Score
score_display = Label(top_right_frame, width=15, height=3, text="Score: {}\n".format(str(score)),
                    font=('Helvetica', 22))
score_display.grid(row=0, column=0)

# WPM
wpm_label = Label(top_right_frame, height=3, width=15, text="WPM: {}\n".format(str(score)), font=('Helvetica', 22))
wpm_label.grid(row=1, column=0)

# Timer
timer = Label(top_right_frame, height=3, text="Time left: {}".format(str(time_left / 100)), font=('Helvetica', 22))
timer.grid(row=2, column=0, sticky="W")

# Main screen
main_screen = Canvas(top_left_frame, width=screen_width-240, height=screen_height*7/10, background="#A7DBDB")
main_screen.create_text(950/2, 300, fill="black", font="Times 100 bold", text="Start Game")
main_screen.create_text(950/2, 400, fill="black", font="Times 20", text="Press enter to start")
main_screen.grid(row=0, column=0)

# Creating images
speech_bubble_image = PhotoImage(file="images/speechbubble.gif")
son_image = PhotoImage(file="images/Son.gif")
mom_image = PhotoImage(file="images/Mom.gif")
thought_bubble = PhotoImage(file="images/thought_bubble.gif")
bg_room = PhotoImage(file="images/Empty_room.gif")

# Option screen
option_screen = Label(top_left_frame, width=60, height=3, text="", font=('Helvetica', 11), bg="white")
option_screen.grid(row=1, column=0)

# Entry frame (Bottom section)
entry_frame = Frame(main_frame, width=screen_width, height=35)
entry_frame.columnconfigure(0, weight=10)
entry_frame.grid_propagate(False)

# Entry field
entry_string = StringVar()
entry_field = Entry(entry_frame, textvariable=entry_string, font=('Helvetica', 15))
entry_field.grid(sticky="WE")

# The start screen
start_screen = Canvas(window, width=screen_width, height=screen_height-80, bg="#A7DBDB")
start_screen.create_text(screen_width/2, screen_height/4, fill="black", font="Helvetica 100", text="Mom VS Son")
start_screen.pack()

# The instructions label and exit instructions button
instructions_label = Label(window, height=10, text=instructions_text, font="Helvetica 24", bg="#A7DBDB")
exit_instructions = Button(window, width=52, font="Helvetica 30", text="Return to Menu", bg="#69d2e7", command=return_to_menu)

# Grid everything onto main frame
top_right_frame.grid(row=0, column=1, sticky="S")
top_left_frame.grid(row=0, column=0)
entry_frame.grid(row=1, column=0, columnspan=2)

# Buttons attached to the start screen
start_button = Button(start_screen, text="Play", command=start_button_pressed, bg="#69d2e7", font="bold")
instructions_button = Button(start_screen, text="How to Play", command=instructions_button_pressed, bg="#69d2e7", font="bold")
exit_button = Button(start_screen, text="Exit", bg="#69d2e7", font="bold", command=exit_button_pressed)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER, height=50, width=200)
instructions_button.place(relx=0.5, rely=0.6, anchor=CENTER, height=50, width=200)
exit_button.place(relx=0.5, rely=0.7, anchor=CENTER, height=50, width=200)

# Run main loop
window.mainloop()
