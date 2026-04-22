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