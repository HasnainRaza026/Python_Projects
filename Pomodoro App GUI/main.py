import customtkinter as ctk
import tkinter as tk

PINK = "#e2979c"
RED = "#f26849"
BLUE = "#b3dab5"
FONT_NAME = "Courier"


class BackgroundApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        self.title("Pomodoro App")

        self.background_photo = tk.PhotoImage(file="tomato.png")

        # Configure columns for the main window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Place other widgets on top of the canvas
        self.text_label = ctk.CTkLabel(self, text="Timer", font=(
            FONT_NAME, 48), bg_color="transparent", text_color=BLUE)
        self.text_label.grid(row=0, column=1, padx=20, pady=10)

        # Create a canvas to place the image
        self.canvas = ctk.CTkCanvas(self, width=200, height=224, bg="#ebebeb")
        self.canvas.grid(row=1, column=1, padx=20, pady=10)
        # Add the background image to the canvas
        self.canvas.create_image(
            0, 0, image=self.background_photo, anchor="nw")

        # Place other widgets on top of the canvas
        self.timer_label = ctk.CTkLabel(self, text="25:00", font=(
            FONT_NAME, 30, "bold"), bg_color=RED, text_color="white", fg_color='transparent')
        self.timer_label.grid(row=1, column=1, padx=20, pady=20)

        self.start_button = ctk.CTkButton(
            self, text="Start Timer", command=self.start_timer, width=60)
        self.start_button.grid(row=2, column=0, padx=20, pady=20)

        self.reset_button = ctk.CTkButton(
            self, text="Reset Timer", command=self.reset_timer, width=60)
        self.reset_button.grid(row=2, column=2, padx=20, pady=20)

        self.study_time = 1500
        self.short_break_time = 300
        self.long_break_time = 1200

        self.running = False
        self.work_sessions = 0

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_25min_studytimer()

    def stop_timer(self):
        if self.running:
            self.running = False

    def reset_timer(self):
        self.stop_timer()
        self.study_time = 1500
        self.short_break_time = 300
        self.long_break_time = 1200
        self.work_sessions = 0
        self.text_label.configure(text="Timer", text_color=BLUE)
        self.timer_label.configure(text="25:00")

    def calculate_and_display_timeleft(self, time_left):
        minutes, seconds = divmod(time_left, 60)
        self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")

    def update_25min_studytimer(self):
        self.text_label.configure(text="Work", text_color=BLUE)
        if self.running:
            self.calculate_and_display_timeleft(self.study_time)
            if self.study_time > 0:
                self.study_time -= 1
                self.after(1000, self.update_25min_studytimer)
            elif self.study_time == 0:
                self.study_time = 1500
                self.work_sessions += 1
                if self.work_sessions < 4:
                    self.update_5min_breaktimer()
                else:
                    self.update_20min_breaktimer()

    def update_5min_breaktimer(self):
        self.text_label.configure(text="Break", text_color=PINK)
        if self.running:
            self.calculate_and_display_timeleft(self.short_break_time)
            if self.short_break_time > 0:
                self.short_break_time -= 1
                self.after(1000, self.update_5min_breaktimer)
            else:
                self.short_break_time = 300
                self.update_25min_studytimer()

    def update_20min_breaktimer(self):
        self.text_label.configure(text="Break", text_color=PINK)
        if self.running:
            self.calculate_and_display_timeleft(self.long_break_time)
            if self.long_break_time > 0:
                self.long_break_time -= 1
                self.after(1000, self.update_20min_breaktimer)
            else:
                self.long_break_time = 1200
                self.work_sessions = 0
                self.update_25min_studytimer()


app = BackgroundApp()
app.mainloop()
