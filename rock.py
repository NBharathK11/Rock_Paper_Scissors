import tkinter as tk
import random

# --- Game Setup ---
choices = ["Rock", "Paper", "Scissors"]
rounds_limit = 5

player_score = 0
computer_score = 0
round_count = 0

# --- Game Logic ---
def determine_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You Win!"
    else:
        return "Computer Wins!"

def play(choice):
    global player_score, computer_score, round_count

    if round_count >= rounds_limit:
        return  # Do nothing if game is over

    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)

    user_choice_label.config(text=f"You chose: {choice}")
    comp_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

    if "You Win" in result:
        player_score += 1
    elif "Computer Wins" in result:
        computer_score += 1

    round_count += 1
    score_label.config(text=f"Round {round_count} / {rounds_limit} - You: {player_score} | Computer: {computer_score}")

    if round_count == rounds_limit:
        show_final_result()

def show_final_result():
    if player_score > computer_score:
        final_result = "🎉 You won the game!"
    elif computer_score > player_score:
        final_result = "😞 Computer won the game!"
    else:
        final_result = "🤝 It's a tie!"

    result_label.config(text=final_result)
    play_again_btn.pack(pady=10)

def reset_game():
    global player_score, computer_score, round_count
    player_score = 0
    computer_score = 0
    round_count = 0

    user_choice_label.config(text="You chose: ")
    comp_choice_label.config(text="Computer chose: ")
    result_label.config(text="Make your move!")
    score_label.config(text=f"Round 0 / {rounds_limit} - You: 0 | Computer: 0")
    play_again_btn.pack_forget()

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock-Paper-Scissors (5 Rounds)")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

user_choice_label = tk.Label(root, text="You chose: ", font=("Helvetica", 12), bg="#f0f0f0")
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer chose: ", font=("Helvetica", 12), bg="#f0f0f0")
comp_choice_label.pack()

result_label = tk.Label(root, text="Make your move!", font=("Helvetica", 14, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, font=("Helvetica", 12), command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, font=("Helvetica", 12), command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, font=("Helvetica", 12), command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

score_label = tk.Label(root, text=f"Round 0 / {rounds_limit} - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#f0f0f0")
score_label.pack(pady=10)

play_again_btn = tk.Button(root, text="Play Again", font=("Helvetica", 11), command=reset_game)

root.mainloop()
