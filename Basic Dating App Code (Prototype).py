# Beatrice Akinpelu
# 11/24/2024

# Simple dating app prototype using Python and Tkinter
# This app allows users to register, create profiles, and match with others.

import tkinter as tk
from tkinter import messagebox

class DatingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Dating App")

        self.users = []  # List to store user profiles
        self.current_user = None  # To store the profile of the currently logged-in user

        # User registration frame
        self.registration_frame = tk.Frame(root)
        self.registration_frame.pack(pady=20)

        self.name_label = tk.Label(self.registration_frame, text="Enter your name:")
        self.name_label.grid(row=0, column=0, padx=10)
        self.name_entry = tk.Entry(self.registration_frame)
        self.name_entry.grid(row=0, column=1, padx=10)

        self.age_label = tk.Label(self.registration_frame, text="Enter your age:")
        self.age_label.grid(row=1, column=0, padx=10)
        self.age_entry = tk.Entry(self.registration_frame)
        self.age_entry.grid(row=1, column=1, padx=10)

        self.gender_label = tk.Label(self.registration_frame, text="Select your gender:")
        self.gender_label.grid(row=2, column=0, padx=10)
        self.gender_var = tk.StringVar(value="Male")
        self.gender_male = tk.Radiobutton(self.registration_frame, text="Male", variable=self.gender_var, value="Male")
        self.gender_female = tk.Radiobutton(self.registration_frame, text="Female", variable=self.gender_var, value="Female")
        self.gender_male.grid(row=2, column=1, padx=10)
        self.gender_female.grid(row=2, column=2, padx=10)

        self.register_button = tk.Button(self.registration_frame, text="Register", command=self.register_user)
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def register_user(self):
        # Get user inputs from the registration form
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_var.get()

        if not name or not age or not gender:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create a user profile
        user_profile = {"name": name, "age": age, "gender": gender}
        self.users.append(user_profile)

        # Set the current user and go to matchmaking screen
        self.current_user = user_profile
        self.registration_frame.pack_forget()  # Hide registration frame
        self.show_matchmaking_screen()

    def show_matchmaking_screen(self):
        # Show matchmaking interface with the current user
        self.matchmaking_frame = tk.Frame(self.root)
        self.matchmaking_frame.pack(pady=20)

        self.profile_label = tk.Label(self.matchmaking_frame, text=f"Welcome, {self.current_user['name']}!")
        self.profile_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.match_button = tk.Button(self.matchmaking_frame, text="Find Matches", command=self.find_matches)
        self.match_button.grid(row=1, column=0, pady=10)

        self.quit_button = tk.Button(self.matchmaking_frame, text="Quit", command=self.root.quit)
        self.quit_button.grid(row=1, column=1, pady=10)

    def find_matches(self):
        # Find potential matches (users with different gender)
        matches = [user for user in self.users if user != self.current_user and user["gender"] != self.current_user["gender"]]
        if not matches:
            messagebox.showinfo("No Matches", "No matches found.")
            return

        match_names = "\n".join([match["name"] for match in matches])
        messagebox.showinfo("Matches", f"Here are your potential matches:\n{match_names}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DatingApp(root)
    root.mainloop()
