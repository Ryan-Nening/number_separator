import tkinter
from tkinter import filedialog
from tkinter import messagebox

def __init__(self):
    self.main_window = tkinter.Tk()
    self.main_window.title("Number Separator Tool")
    self.main_window.geometry("300x150")

def build_user_interface(self):
    self.instruction_label = tkinter.Label(self.main_window, text="Select your numbers text file:")
    self.instruction_label.pack()
    self.process_button = tkinter.Button(self.main_window, text="Choose File & Separate", command=self.process_text_files)
    self.process_button.pack()

def process_text_files(self):
    input_file_name = filedialog.askopenfilename(title="Select Numbers File")

def process_text_files(self):
    input_file_name = filedialog.askopenfilename(title="Select Numbers File")
    if input_file_name != "":
        input_file = open(input_file_name, "r")
        even_file = open("even.txt", "w")
        odd_file = open("odd.txt", "w")
        for current_line in input_file:
            current_number = int(current_line.strip())
            if current_number % 2 == 0:
                even_file.write(str(current_number) + "\n")
            else:
                odd_file.write(str(current_number) + "\n")
        input_file.close()
        even_file.close()
        odd_file.close()
        messagebox.showinfo("Success", "Separation complete! Check your folder for even.txt and odd.txt")

def run_application(self):
    self.build_user_interface()
    self.main_window.mainloop()