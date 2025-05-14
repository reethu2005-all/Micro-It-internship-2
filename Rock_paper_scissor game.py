import tkinter as tk
from tkinter import messagebox
import random
import pyttsx3
import csv
from datetime import datetime

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "Player"
    else:
        return "Computer"

# Save result to CSV file
def save_to_csv(player_score, computer_score):
    with open("rps_game_results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), player_score, computer_score])

# Handle user choice via button
def player_choice_handler(player_choice):
    global player_score, computer_score, rounds

    computer_choice = random.choice(["rock", "paper", "scissors"])
    winner = determine_winner(player_choice, computer_choice)

    result_msg = f"You: {player_choice}\nComputer: {computer_choice}\nResult: {winner}"
    result_label.config(text=result_msg)
    speak(result_msg)

    if winner == "Player":
        player_score += 1
    elif winner == "Computer":
        computer_score += 1

    score_label.config(text=f"Score → You: {player_score} | Computer: {computer_score}")
    rounds += 1

    if player_score == 3 or computer_score == 3:
        final_msg = "🎉 You won the game!" if player_score > computer_score else "💻 Computer won the game!"
        speak(final_msg)
        messagebox.showinfo("Game Over", final_msg)
        save_to_csv(player_score, computer_score)
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors - Internship Project")
root.geometry("400x400")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="🎮 Rock-Paper-Scissors Game", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 12),
                     command=lambda: player_choice_handler("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 12),
                      command=lambda: player_choice_handler("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 12),
                         command=lambda: player_choice_handler("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Initialize scores
player_score = 0
computer_score = 0
rounds = 0

speak("Welcome to Rock Paper Scissors. First to win 3 rounds is the winner. Click a button to start.")

root.mainloop()
