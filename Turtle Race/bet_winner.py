import tkinter as tk


class BetWinner:
    def __init__(self):
        self.bet_color = None
        self.root = tk.Tk()
        self.root.title("Make your bet")
        self.root.geometry("300x150")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Create and place the label
        self.label = tk.Label(
            self.root, text="Who will win the race, make your bet:- \n 'red', 'green', 'blue', 'brown', 'purple', 'pink'")
        self.label.pack(pady=10)

        # Create and place the entry widget
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Create and place the OK button
        self.ok_button = tk.Button(
            self.button_frame, text="OK", command=self.on_ok, width=10)
        self.ok_button.grid(row=0, column=0, padx=5)

        # Create and place the Cancel button
        self.cancel_button = tk.Button(
            self.button_frame, text="Cancel", command=self.on_cancel, width=10)
        self.cancel_button.grid(row=0, column=1, padx=5)

    def on_ok(self):
        self.bet_color = self.entry.get().lower()
        self.root.destroy()  # Close the window after getting input

    def on_cancel(self):
        print("Operation cancelled")
        self.root.destroy()  # Close the window without taking input


if __name__ == "__main__":
    app = BetWinner()
