from tkinter import *
from data import Data

THEME_COLOR = "#f77f00"
FONT = ("Arial", 20, "normal")

class UI():

    def __init__(self):
        self.window = Tk()
        self.window.state('zoomed')
        self.window.title("Condensed Nearest Neighbour")
        self.window.minsize(width=500, height=300)
        self.window.config(padx=10, pady=20)

        self.canvas = Canvas(bg='white', width=500, height=250)
        self.canvas.grid(column=0, row=0, columnspan=2)


        # Label
        my_label = Label(text="Separability degree:", font=("Arial", 12, "bold"))
        my_label.grid(column=0, row=1)
        my_label.config(padx=10, pady=10)
        self.input_sep = Entry(width=10)
        self.input_sep.grid(column=1, row=1)

        my_label=Label(text="Balance ratio:", font=("Arial", 12, "bold"))
        my_label.grid(column=0, row=2)
        my_label.config(padx=10, pady=10)
        self.input_br = Entry(width=10)
        self.input_br.grid(column=1, row=2)

        my_label = Label(text="Number of samples:", font=("Arial", 12, "bold"))
        my_label.grid(column=0, row=3)
        my_label.config(padx=10, pady=10)
        self.input_ns = Entry(width=10)
        self.input_ns.grid(column=1, row=3)

        self.button = Button(text="Show Original", command=self.org_button_clicked)
        self.button.grid(column=0, row=4)

        self.button = Button(text="Show Undersampled", command=self.under_button_clicked)
        self.button.grid(column=1, row=4)

        self.button = Button(text="Generate new data", command=self.get_data)
        self.button.grid(column=0, row=5)
        self.window.mainloop()

    def get_data(self):


        self.sep = self.input_sep.get()
        self.br = self.input_br.get()
        self.ns = self.input_ns.get()
        data = Data(sep=int(self.sep), n_samples=int(self.ns), weights=float(self.br))
        org_img = PhotoImage(file="Original.png")
        self.org_img = org_img.subsample(2, 2)
        under_img = PhotoImage(file="Undersampled.png")
        self.under_img = under_img.subsample(2, 2)

    def org_button_clicked(self):
        self.canvas.delete("all")
        self.canvas_image = self.canvas.create_image(250, 125, image=self.org_img)
        self.canvas.grid(column=0, row=0, columnspan=2)


    def under_button_clicked(self):
        self.canvas.delete("all")
        self.canvas_image = self.canvas.create_image(250, 125, image=self.under_img)





        # self.canvas_img = self.canvas.create_image(200, 200, width=380, text="TEXT")
        # self.canvas.itemconfig(self.canvas_img, image, font=FONT)

        #
        # original_img.grid(column=0, row=0)
        # Undersampled_img = PhotoImage(file="Undersampled.png")
        # Undersampled_img.grid(column=0, row=0)




        # # Button
        # self.button = Button(text="Click Me")
        # self.button.grid(column=1, row=1)
        #
        # self.new_button = Button(text="New Button")
        # self.new_button.grid(column=2, row=0)
        #
        # # Entry
        # input = Entry(width=10)
        # print(input.get())
        # input.grid(column=3, row=2)





