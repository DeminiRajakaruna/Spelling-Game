import tkinter as tk
from tkinter import messagebox

class SpellGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Game")
        
        self.label = tk.Label(self.root, text="Enter the correct spelling of 'apple':")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(self.root, text="Check Spelling", command=self.check_spelling)
        self.button.pack(pady=10)

    def check_spelling(self):
        user_input = self.entry.get().strip().lower()
        correct_word = "apple"
        
        if user_input == correct_word:
            messagebox.showinfo("Spelling Result", "Correct! You spelled 'apple' correctly.")
        else:
            messagebox.showerror("Spelling Result", f"Incorrect. Try again!")

def main():
    root = tk.Tk()
    app = SpellGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
