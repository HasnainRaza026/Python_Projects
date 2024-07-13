import customtkinter


class LengthUnitConverter(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Length Unit Converter')
        self.geometry("400x200")

        # Configure grid weights to make the layout responsive
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.entry_boxes = [None, None]
        self.add_entry_boxes()

        self.option_values = ['nanometer', 'micrometer', 'millimeter', 'centimeter', 'meter', 'kilometer', 'mile', 'yard',
                              'foot', 'inch', 'nautical mile']
        self.conversion_factors = {
            'nanometer': 1e-9, 'micrometer': 1e-6, 'millimeter': 1e-3, 'centimeter': 1e-2,
            'meter': 1, 'kilometer': 1e3, 'mile': 1609.34, 'yard': 0.9144,
            'foot': 0.3048, 'inch': 0.0254, 'nautical mile': 1852
        }
        self.option_menus = [None, None]
        self.options_selected = [None, None]
        self.add_option_menu(0)
        self.add_option_menu(1)

        self.add_button()
        self.add_error_label()
        self.mainloop()

    def add_entry_boxes(self):
        for i in range(2):
            entry_box = customtkinter.CTkEntry(self, width=60)
            entry_box.grid(row=0, column=i, padx=10, pady=10, sticky='ew')
            self.entry_boxes[i] = entry_box

    def add_option_menu(self, index):
        option_menu = customtkinter.CTkOptionMenu(self, values=self.option_values, width=115,
                                                  command=lambda choice, i=index: self.option(choice, i))
        option_menu.set(self.option_values[index])
        option_menu.grid(row=1, column=index, padx=10, pady=10, sticky='ew')
        self.option_menus[index] = option_menu

    def option(self, choice, i):
        other_index = 1 - i
        if self.option_menus[other_index].get() == choice:
            for val in self.option_values:
                if val != choice:
                    self.option_menus[other_index].set(val)
                    break

        self.options_selected[i] = choice

    def add_button(self):
        button = customtkinter.CTkButton(
            master=self, text='Calculate', command=self.calculate_operation)
        button.grid(row=2, column=0, columnspan=2,
                    padx=20, pady=10, sticky='ew')

    def add_error_label(self):
        self.error_label = customtkinter.CTkLabel(
            master=self, text="", text_color="red")
        self.error_label.grid(
            row=3, column=0, columnspan=2, pady=5, sticky='ew')

    def calculate_operation(self):
        self.error_label.configure(text="")  # Clear any previous error message
        try:
            # Get the input value and selected units
            value = float(self.entry_boxes[0].get())
            from_unit = self.options_selected[0]
            to_unit = self.options_selected[1]

            # Convert the input value to meters
            value_in_meters = value * self.conversion_factors[from_unit]

            # Convert from meters to the target unit
            converted_value = value_in_meters / \
                self.conversion_factors[to_unit]

            # Display the converted value
            self.entry_boxes[1].delete(0, 'end')
            self.entry_boxes[1].insert(0, str(converted_value))

            # Adjust the width of the entry box based on the length of the result
            result_length = len(str(converted_value))
            # Minimum width 60, adjust based on length of result
            new_width = max(60, result_length * 10)
            self.entry_boxes[1].configure(width=new_width)

        except ValueError:
            self.error_label.configure(text="Invalid Input")
        except KeyError:
            self.error_label.configure(text="Select Units")


if __name__ == '__main__':
    length_converter = LengthUnitConverter()
