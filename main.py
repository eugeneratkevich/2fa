import Tkinter as tk
import pyotp

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.master.title('Google 2FA')

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt = tk.Label(self, text="Enter a auth secret:", anchor="w")
        self.entry = tk.Entry(self, show="*")
        self.submit = tk.Button(self, text="Copy token to clipboard", command=self.calculate)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x", padx=20)
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def calculate(self):
        # get the value from the input widget,
        # and do a calculation
        try:
            secret = str(self.entry.get())
            totp = pyotp.TOTP(secret)
            result = totp.now()
        except ValueError:
            result = "Please enter auth secret"

        if type(result) == unicode:  # Set clipboard text.
            self.clipboard_clear()
            self.clipboard_append(result)

        # set the output widget to have our result
        self.output.configure(text=result)


# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
