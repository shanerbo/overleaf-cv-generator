import tkinter as tk
from CV import CV
from tkinter import messagebox


def run() -> None:
    cv = CV('./cv.txt')
    font = "Calibri 24"
    input_font = "Calibri 18"

    def validate():
        if not (len(title.get()) != 0
                and len(company_name.get()) != 0
                and len(company_name_short.get()) != 0
                and len(company_addr.get()) != 0
                and len(company_province.get()) != 0
                and len(receiver.get()) != 0
                and len(receiver_title.get()) != 0
                and len(receiver_last_name.get()) != 0
                and len(input.get()) != 0
                and len(output.get()) != 0):
            messagebox.showinfo("Missing input", "Please fill all input")

    def populate():
        return title.get()

    OptionList = [
        "Mr.",
        "Ms.",
        "Miss.",
        "Mrs."
    ]

    master = tk.Tk()
    master.geometry("1080x800")
    tk.Label(master, text="Job title", font=font).grid(row=0)
    tk.Label(master, text="Company name (SAP INC)", font=font).grid(row=1)
    tk.Label(master, text="Company name short form(SAP)", font=font).grid(row=2)
    tk.Label(master, text="Company address (xxxx xx st)", font=font).grid(row=3)
    tk.Label(master, text="Company province (Burnaby, BC, Canada", font=font).grid(row=4)
    tk.Label(master, text="Receiver (Jane Doe)", font=font).grid(row=5)
    tk.Label(master, text="Title (Ms.)", font=font).grid(row=6)
    tk.Label(master, text="Receiver Last Name (Doe)", font=font).grid(row=7)
    tk.Label(master, text="input file (extension with txt)", font=font).grid(row=8)
    tk.Label(master, text="Output tex file (extension .tex is not needed)", font=font).grid(row=9)
    tk.Label(master, text="First paragraph", font=font).grid(row=10)

    title = tk.Entry(master, font=input_font)
    company_name = tk.Entry(master, font=input_font)
    company_name_short = tk.Entry(master, font=input_font)
    company_addr = tk.Entry(master, font=input_font)
    company_province = tk.Entry(master, font=input_font)
    receiver = tk.Entry(master, font=input_font)
    receiver_title = tk.Entry(master, font=input_font)
    receiver_last_name = tk.Entry(master, font=input_font)
    input = tk.Entry(master, font=input_font)
    output = tk.Entry(master, font=input_font)
    paragraph = tk.Text(master, font=input_font, height=10, width=40)

    title.grid(row=0, column=1, ipady=3, ipadx=55)
    company_name.grid(row=1, column=1, ipady=3, ipadx=55)
    company_name_short.grid(row=2, column=1, ipady=3, ipadx=55)
    company_addr.grid(row=3, column=1, ipady=3, ipadx=55)
    company_province.grid(row=4, column=1, ipady=3, ipadx=55)
    receiver.grid(row=5, column=1, ipady=3, ipadx=55)
    receiver_title.grid(row=6, column=1, ipady=3, ipadx=55)
    receiver_last_name.grid(row=7, column=1, ipady=3, ipadx=55)
    input.grid(row=8, column=1, ipady=3, ipadx=55)
    output.grid(row=9, column=1, ipady=3, ipadx=55)
    paragraph.grid(row=10, column=1, ipady=3, ipadx=1)

    validator_button = tk.Button(master,
                                 text='Validate',
                                 command=validate).grid(row=13,
                                                        column=0,
                                                        pady=4)
    populate_button = tk.Button(master,
                                text='Populate', command=populate).grid(row=13,
                                                                        column=1,
                                                                        sticky=tk.W,
                                                                        pady=4)

    master.mainloop()
