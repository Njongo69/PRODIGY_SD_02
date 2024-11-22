import tkinter as tk
from tkinter import messagebox
import random

# Number Guessing Game with GUI
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # Generate a random number between 1 and 100
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        
        # GUI Components
        tk.Label(root, text="Guess the number (between 1 and 100):").pack(pady=10)
        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack(pady=5)
        self.button_guess = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button_guess.pack(pady=10)
        
        self.label_feedback = tk.Label(root, text="")
        self.label_feedback.pack(pady=5)
    
    def check_guess(self):
        try:
            user_guess = int(self.entry_guess.get())
            self.attempts += 1
            
            if user_guess < self.random_number:
                self.label_feedback.config(text="Too low! Try again.")
            elif user_guess > self.random_number:
                self.label_feedback.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
    
    def reset_game(self):
        # Reset the game for a new round
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.label_feedback.config(text="")
        self.entry_guess.delete(0, tk.END)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
