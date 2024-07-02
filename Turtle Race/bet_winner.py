import tkinter as tk


class BetWinner:
    """
    A class to handle user bets in a turtle race game.
    """

    def __init__(self):
        """
        Initializes the BetWinner class and sets up the GUI.
        """
        self.bet_color = None
        self.valid_colors = ['red', 'green', 'blue', 'brown', 'purple', 'pink']
        self.root = tk.Tk()
        self.root.title("Make your bet")
        self.root.geometry("300x200")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        """
        Creates the GUI widgets for user input and interaction.
        """
        self.label = tk.Label(
            self.root, text="Who will win the race? Make your bet:\n 'red', 'green', 'blue', 'brown', 'purple', 'pink'")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)

        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.pack(pady=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.ok_button = tk.Button(
            self.button_frame, text="OK", command=self.on_ok, width=10)
        self.ok_button.grid(row=0, column=0, padx=5)

        self.cancel_button = tk.Button(
            self.button_frame, text="Cancel", command=self.on_cancel, width=10)
        self.cancel_button.grid(row=0, column=1, padx=5)

    def on_ok(self):
        """
        Handles the OK button click event. Validates the input and stores the bet color.
        """
        self.bet_color = self.entry.get().lower()
        if self.bet_color in self.valid_colors:
            self.root.destroy()  # Close the window after getting valid input
        else:
            self.message_label.config(
                text="Invalid color! Please enter a valid color.")

    def on_cancel(self):
        """
        Handles the Cancel button click event. Closes the window without taking input.
        """
        print("Operation cancelled")
        self.root.destroy()  # Close the window without taking input
