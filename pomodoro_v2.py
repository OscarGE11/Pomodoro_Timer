import tkinter as tk
import winsound
import threading

screen = tk.Tk()

screen.title("Pomodoro Timer!")
screen.geometry("700x400")
screen.config(bg="#FF7F7F")

# Inicialización de variables
initial_time = 25 * 60
timer = initial_time
running_timer = False
timer_id = None

def play_sound():
 
    threading.Thread(target=lambda: winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)).start()

def format_timer(seconds):
    minutes = seconds // 60
    missing_seconds = seconds % 60
    return f"{minutes:02d}:{missing_seconds:02d}"

def countdown():
    global timer, running_timer, timer_id
    if timer > 0:
        timer -= 1
        timer_label.config(text=format_timer(timer))
        timer_id = screen.after(10, countdown) 
    else:
        running_timer = False
        play_sound()

def toggle_timer():
    global running_timer, timer_id
    if running_timer:
        screen.after_cancel(timer_id)
        running_timer = False
        control_button.config(text="Start")
    else:
        running_timer = True
        control_button.config(text="Pause")
        countdown()

def restart_timer():
    global running_timer, timer_id, timer
    if timer_id is not None:
        screen.after_cancel(timer_id)
    running_timer = False
    timer = initial_time
    timer_label.config(text=format_timer(timer))
    control_button.config(text="Start")

# Título
titulo = tk.Label(text="Pomodoro Timer", fg="green", font=("Helvetica", 48), bg="#FF7F7F")
titulo.pack(pady=20)

# Etiqueta de tiempo
timer_label = tk.Label(text=format_timer(timer), fg="black", font=("Bold", 25), bg="#FF7F7F")
timer_label.pack(pady=20)

# Botón de control
control_button = tk.Button(
    screen,
    text="Start",
    command=toggle_timer,
    font=("Helvetica", 16, "bold"),
    bg="#4CAF50",
    fg="white",
    width=10,
    height=2,
    bd=0,
    relief="flat",
    highlightthickness=0,
    padx=20,
    pady=10,
    borderwidth=0
)
control_button.pack(pady=20)

# Botón de reinicio
restart_button = tk.Button(
    screen,
    text="Restart",
    command=restart_timer,
    font=("Helvetica", 16, "bold"),
    bg="#f44336",
    fg="white",
    width=10,
    height=2,
    bd=0,
    relief="flat",
    highlightthickness=0,
    padx=20,
    pady=10,
    borderwidth=0
)
restart_button.pack(pady=20)

screen.mainloop()
