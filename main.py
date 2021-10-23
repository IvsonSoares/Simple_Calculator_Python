import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 35, "bold")
OPERATORS_FONT_STYLE = ("Arial", 20)
MEDIUM_FONT_STYLE = ("Arial", 15, "bold")
DIGITS_FONT_STYLE = ("Arial", 12, "bold")
DEFAULT_FONT_STYLE = ("Arial", 10)

WHITE = "#ffffff"
BUTTONS_BLUE = "#ccedff"
BUTTONS_GRAY = "#878480"
LABEL_BACKGROUND_COLOR = "#ebf0f7"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("457x464")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.current_base = 2

        self.letters_list = []
        self.digits_list = []

        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (4, 1), 5: (4, 2), 6: (4, 3),
            2: (5, 2), 3: (5, 3), 1: (5, 1),
            0: (6, 2)
        }

        self.operations = {"+": "+", "-": "-"}
        self.hex_letters = ["a", "b", "c", "d", "e", "f"]
        self.numeric_bases = {"HEX": 1, "DEC": 2, "OCT": 3, "BIN": 4}

        self.display_frame = self.create_display_frame()
        self.total_label, \
        self.hex_base_label, \
        self.dec_base_label, \
        self.oct_base_label, \
        self.bin_base_label, \
        self.label = self.create_display_labels()
        self.buttons_frame = self.create_display_frame()
        self.create_buttons()
        self.create_hex_letters()
        self.call_numeric_bases(self)

    def create_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_numeric_bases_buttons()

    def create_display_labels(self):
        # label superior
        total_label = tk.Label(self.display_frame,
                               text=self.total_expression,
                               anchor=tk.E, bg=LABEL_BACKGROUND_COLOR,
                               fg=LABEL_COLOR,
                               padx=24,
                               pady=10,
                               font=MEDIUM_FONT_STYLE)

        total_label.pack(expand=True, fill='both')

        # label principal
        label = tk.Label(self.display_frame,
                         text=f"{self.current_expression}",
                         anchor=tk.E,
                         bg=LABEL_BACKGROUND_COLOR,
                         height=2,
                         fg=LABEL_COLOR,
                         padx=24,
                         font=LARGE_FONT_STYLE)

        label.pack(expand=True, fill='both')

        # HEXADECIMAL LABEL

        hex_base_label = tk.Label(self.display_frame,
                                  text="HEX:",
                                  anchor=tk.W, bg=LABEL_BACKGROUND_COLOR,
                                  fg=LABEL_COLOR,
                                  font=DEFAULT_FONT_STYLE)

        hex_base_label.pack(expand=True, fill=tk.X)

        # DECIMAL LABEL

        dec_base_label = tk.Label(self.display_frame,
                                  text="DEC:",
                                  anchor=tk.W, bg=LABEL_BACKGROUND_COLOR,
                                  fg=LABEL_COLOR,
                                  font=DEFAULT_FONT_STYLE)

        dec_base_label.pack(expand=True, fill=tk.X)

        # OCTA LABEL

        oct_base_label = tk.Label(self.display_frame,
                                  text="OCT:",
                                  anchor=tk.W,
                                  bg=LABEL_BACKGROUND_COLOR,
                                  fg=LABEL_COLOR,
                                  font=DEFAULT_FONT_STYLE)

        oct_base_label.pack(expand=True, fill=tk.X)

        # BINARY LABEL

        bin_base_label = tk.Label(self.display_frame,
                                  text="BIN:",
                                  anchor=tk.W,
                                  bg=LABEL_BACKGROUND_COLOR,
                                  fg=LABEL_COLOR,
                                  font=DEFAULT_FONT_STYLE)

        bin_base_label.pack(expand=True, fill=tk.X)

        return total_label, hex_base_label, dec_base_label, \
               oct_base_label, bin_base_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
        self.numeric_bases_display()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,
                               text=str(digit),
                               bg=WHITE,
                               fg=LABEL_COLOR,
                               font=DIGITS_FONT_STYLE,
                               borderwidth=0,
                               bd=3,
                               command=lambda x=digit: self.add_to_expression(x))

            self.digits_list.append(button)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame,
                               text=symbol,
                               bg=WHITE,
                               fg=LABEL_COLOR,
                               font=OPERATORS_FONT_STYLE,
                               bd=3,
                               command=lambda x=operator: self.append_operator(x))

            button.grid(row=i + 3, column=4, rowspan=2, sticky=tk.NSEW)
            i += 2

    def append_operator(self, operator):

        # hexa
        if self.current_base == 1:
            self.current_expression = hex(int(self.current_expression, 16))

        # octa
        elif self.current_base == 3:
            self.current_expression = oct(int(self.current_expression, 8))

        # binario
        elif self.current_base == 4:
            self.current_expression = bin(int(self.current_expression, 2))

        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.numeric_bases_display()
        self.update_label()


    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.numeric_bases_display()
        self.update_total_label()
        self.update_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame,
                           text="CE",
                           bg=BUTTONS_GRAY,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0,
                           bd=3,
                           command=self.clear)

        button.grid(row=6, column=1, sticky=tk.NSEW)

    def create_hex_letters(self):

        i = 0
        for symbol in self.hex_letters:
            button = tk.Button(self.buttons_frame,
                               state=tk.DISABLED,
                               text=symbol,
                               bg=WHITE,
                               fg=LABEL_COLOR,
                               font=DIGITS_FONT_STYLE,
                               borderwidth=0,
                               padx=24,
                               bd=3,
                               command=lambda x=symbol: self.add_to_expression(x))

            self.letters_list.append(button)
            button.grid(row=i + 1, column=0, sticky=tk.NSEW)
            i += 1

    def create_numeric_bases_buttons(self):
        i = 0
        for base, operation in self.numeric_bases.items():
            button = tk.Button(self.buttons_frame,
                               state=tk.NORMAL,
                               text=base,
                               bg=BUTTONS_BLUE,
                               fg=LABEL_COLOR,
                               font=DIGITS_FONT_STYLE,
                               bd=3,
                               padx=24,
                               command=lambda x=operation: self.call_numeric_bases(x))

            button.grid(row=1, rowspan=2, column=i + 1, sticky=tk.NSEW)
            i += 1

    def evaluate(self):
        try:
            # hexa
            if self.current_base == 1:
                self.total_expression += hex(int(self.current_expression, 16))
                self.current_expression = hex(eval(self.total_expression))

            # decimal
            elif self.current_base == 2:
                self.total_expression += self.current_expression
                self.current_expression = str(eval(self.total_expression))

            # octa
            elif self.current_base == 3:
                self.total_expression += oct(int(self.current_expression, 8))
                self.current_expression = oct(eval(self.total_expression))

            # binario
            else:
                self.total_expression += bin(int(self.current_expression, 2))
                self.current_expression = bin(eval(self.total_expression))

            self.update_total_label()
            self.total_expression = ""

        except Exception as e:
            self.current_expression = "Error"

        finally:
            self.numeric_bases_display()
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame,
                           text="=",
                           bg=BUTTONS_BLUE,
                           fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE,
                           bd=3,
                           command=self.evaluate)

        button.grid(row=6, column=3, sticky=tk.NSEW)

    # label superior
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    # label principal
    def update_label(self):
        self.label.config(text=self.current_expression[:15])

    # label bases
    def numeric_bases_display(self):

        if self.current_expression != "":
            if self.current_base == 1:
                base = 16
            elif self.current_base == 2:
                base = 10
            elif self.current_base == 3:
                base = 8
            else:
                base = 2

            hex_display = hex(int(self.current_expression, base))
            dec_display = int(self.current_expression, base)
            oct_display = oct(int(self.current_expression, base))
            binary_display = bin(int(self.current_expression, base))

        else:
            hex_display = ""
            dec_display = ""
            oct_display = ""
            binary_display = ""

        text_hex_value = tk.StringVar()
        text_hex_value.set(f"HEX: {hex_display}")
        self.hex_base_label.config(textvariable=text_hex_value)

        text_dec_value = tk.StringVar()
        text_dec_value.set(f"DEC: {dec_display}")
        self.dec_base_label.config(textvariable=text_dec_value)

        text_oct_value = tk.StringVar()
        text_oct_value.set(f"OCT: {oct_display}")
        self.oct_base_label.config(textvariable=text_oct_value)

        text_bin_value = tk.StringVar()
        text_bin_value.set(f"BIN: {binary_display}")
        self.bin_base_label.config(textvariable=text_bin_value)

    def call_numeric_bases(self, x):
        # HEXA
        if x == 1:
            self.current_base = 1
            self.clear()
            for i in self.letters_list:
                i['state'] = tk.NORMAL
            for j in self.digits_list[0:9]:
                j['state'] = tk.NORMAL

        # DECIMAL
        elif x == 2:
            self.current_base = 2
            self.clear()
            for i in self.letters_list:
                i['state'] = tk.DISABLED
            for j in self.digits_list[0:9]:
                j['state'] = tk.NORMAL

        # OCTA
        elif x == 3:
            self.current_base = 3
            self.clear()
            for i in self.letters_list:
                i['state'] = tk.DISABLED
            for j in self.digits_list:
                j['state'] = tk.NORMAL
            for k in self.digits_list[1:3]:
                k['state'] = tk.DISABLED

        # BINARIO
        elif x == 4:
            self.current_base = 4
            self.clear()
            for i in self.letters_list:
                i['state'] = tk.DISABLED
            for j in self.digits_list[0:8]:
                j['state'] = tk.DISABLED

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
