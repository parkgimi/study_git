from tkinter import Label, Tk
from datetime import datetime

app_window = Tk()
app_window.wm_attributes("-topmost", 1)
app_window.title("박희영, 시간은 화살보다 빨리 지나간다. 한강물 다 녹았다!!!")
app_window.overrideredirect(True)
app_window.geometry("974x90+333+0")
app_window.resizable(0, 0)

text_font = ("Consolas", 50, 'bold')
background = "#000000"
foreground = "#acc0c7"
border_width = 5

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def digital_clock():
    # display text
    date_live = str(datetime.now().strftime("%Y-%m-%d"))
    time_live = str(datetime.now().strftime("%H:%M:%S.%f"))[:-3]
    days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
    a = datetime.today().weekday()
    label.config(text=date_live+" "+days[a]+" "+time_live)
    label.after(100, digital_clock)


digital_clock()
app_window.mainloop()
