import tkinter as tk

screen = tk.Tk()

# Crear la ventana
screen.title("Pomodoro Timer!")
screen.geometry("700x400")
screen.config(bg="#FF7F7F")

# Duraciones en segundos
pomodoro_time = 5 * 60  # 5 minutos (ajustado para pruebas rápidas)
short_break_time = 1 * 60  # 1 minuto (ajustado para pruebas rápidas)
long_break_time = 2 * 60  # 2 minutos (ajustado para pruebas rápidas)

# Estado inicial
current_time = pomodoro_time
active_timer = False
id_timer = None
in_break = False
session_count = 0

def time_format(seconds):
    minutes = seconds // 60
    missing_seconds = seconds % 60
    return f"{minutes:02d}:{missing_seconds:02d}"

def countdown():
    global active_timer, current_time, id_timer, in_break, session_count
    if current_time > 0:
        current_time -= 1
        time_label.config(text=time_format(current_time))
        id_timer = screen.after(10, countdown)  # Llama a countdown después de 1 segundo
    else:
        if not in_break:
            # Cambiar a descanso corto después de una sesión de trabajo
            session_count += 1
            in_break = True
            if session_count % 4 == 0:
                current_time = long_break_time
                text_label.config(text="Long Break Time!")
            else:
                current_time = short_break_time
                text_label.config(text="Short Break Time!")
        else:
            # Volver a sesión de trabajo después del descanso
            in_break = False
            current_time = pomodoro_time
            text_label.config(text="Pomodoro Time")
            session_count = 0
        time_label.config(text=time_format(current_time))
        countdown()

def start_timer():
    global active_timer
    if not active_timer:
        countdown()
        active_timer = True

def stop_timer():
    global active_timer, id_timer
    if active_timer:
        screen.after_cancel(id_timer)  # Cancelar la llamada a countdown
        active_timer = False

def restart_timer():
    global current_time, active_timer, id_timer, in_break
    stop_timer()
    if in_break:
        current_time = short_break_time
        text_label.config(text="Break Time!")
    else:
        current_time = pomodoro_time
        text_label.config(text="Pomodoro Time")
    time_label.config(text=time_format(current_time))
    active_timer = False

# Etiqueta que muestra el temporizador
text_label = tk.Label(screen, text="Pomodoro Timer", font=("Helvetica", 30), bg="#FF7F7F", fg="green")
text_label.pack(pady=5)

time_label = tk.Label(screen, text=time_format(pomodoro_time), font=("Helvetica", 48), bg="#FF7F7F")
time_label.pack(pady=20)

# Botones para controlar el temporizador
start_button = tk.Button(screen, text="Start", command=start_timer)
start_button.pack(pady=5)

pause_button = tk.Button(screen, text="Pause", command=stop_timer)
pause_button.pack(pady=5)

restart_button = tk.Button(screen, text="Restart", command=restart_timer)
restart_button.pack(pady=5)

# Iniciar el bucle de la ventana
screen.mainloop()
