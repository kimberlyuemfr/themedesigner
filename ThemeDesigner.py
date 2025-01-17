import os
import ctypes
from tkinter import Tk, Button, Label, ColorChooser, filedialog

class ThemeDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title('ThemeDesigner')
        self.root.geometry('400x200')
        
        self.bg_color = "#FFFFFF"
        self.fg_color = "#000000"
        
        self.bg_label = Label(root, text="Background Color:", bg=self.bg_color, fg=self.fg_color)
        self.bg_label.pack(pady=10)
        
        self.bg_button = Button(root, text="Choose Background Color", command=self.choose_bg_color)
        self.bg_button.pack(pady=5)
        
        self.fg_label = Label(root, text="Foreground Color:", bg=self.bg_color, fg=self.fg_color)
        self.fg_label.pack(pady=10)
        
        self.fg_button = Button(root, text="Choose Foreground Color", command=self.choose_fg_color)
        self.fg_button.pack(pady=5)
        
        self.apply_button = Button(root, text="Apply Theme", command=self.apply_theme)
        self.apply_button.pack(pady=20)
        
    def choose_bg_color(self):
        color_code = ColorChooser.askcolor(title="Choose Background Color")
        if color_code:
            self.bg_color = color_code[1]
            self.update_preview()
        
    def choose_fg_color(self):
        color_code = ColorChooser.askcolor(title="Choose Foreground Color")
        if color_code:
            self.fg_color = color_code[1]
            self.update_preview()
            
    def update_preview(self):
        self.bg_label.config(bg=self.bg_color, fg=self.fg_color)
        self.fg_label.config(bg=self.bg_color, fg=self.fg_color)
        
    def apply_theme(self):
        # This is just a placeholder for applying the theme.
        # You would replace this with actual code to change Windows theme.
        print(f"Applying Theme: Background Color: {self.bg_color}, Foreground Color: {self.fg_color}")
        
        # Placeholder for system call to apply theme
        ctypes.windll.user32.MessageBoxW(0, f"Theme applied with Background: {self.bg_color} and Foreground: {self.fg_color}", "Theme Applied", 1)
        
if __name__ == "__main__":
    root = Tk()
    app = ThemeDesigner(root)
    root.mainloop()