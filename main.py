from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    '''
    Restart the: Timer clock, Title, Checkmarks and reps
    :return: clean start
    '''
    window.after_cancel(timer) # stops the timer
    tomato_canvas.itemconfig(timer_text, text="00:00") # reset the clock
    timer_label.config(text="Timer", fg="Black") # reset the title
    chekmarks.config(text="") # reset the checkmarks
    global reps
    reps = 0 # reset marks


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    '''
    Starts the timer, and count the reps for break
    '''
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: # If it's the 1st/3rd/5th/7th rep
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=GREEN)
    elif reps % 2 == 0: # If it's the 2nd/4th/6th rep
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work!", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60) # Gets the mins remain
    count_sec = count % 60 # Gets the secs remain
    # Ifs for the Timer
    if count_sec < 10: # when less then 10 sec, you will see 0{cuont_sec}
        count_sec = f"0{count_sec}"

    tomato_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # Change the text on the 'timer _text' variable
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)  # Calls a function after X amount of miliseconds
    else:
        start()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        chekmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50, bg=YELLOW)

# Insert the image
tomato_img = PhotoImage(file="tomato.png") # Format the image for the Canvas
tomato_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Size the photo
tomato_canvas.create_image(100, 112, image=tomato_img) # Create the image the insert the converted image
timer_text = tomato_canvas.create_text(116, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
tomato_canvas.grid(column=1, row=1)

# Label for timer
timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW)
timer_label.grid(column=1,row=0)

# Buttons
start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(column=2,row=2)

# CheckMark
chekmarks = Label(font=(FONT_NAME, 12, "bold"), bg=YELLOW)
chekmarks.grid(column=1,row=4)

window.mainloop()