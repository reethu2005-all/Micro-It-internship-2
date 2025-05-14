# Micro-It-internship-2

🪨📄✂️ Rock-Paper-Scissors Game (Python + Tkinter)
An interactive Rock-Paper-Scissors game built using Python with a Tkinter GUI, text-to-speech (TTS) feedback, score tracking, and CSV logging. This project was developed for a Micro IT Internship to showcase GUI design, logic implementation, and basic use of Python libraries.

📌 Features
🎮 Best of 5 gameplay (first to 3 wins)

🖱️ Button-based selection for Rock, Paper, or Scissors

🗣️ Text-to-Speech feedback using pyttsx3

📊 Game result saved to a .csv file with timestamp

🖼️ Clean and simple Tkinter GUI

📁 Modular and readable code with comments

🛠 Technologies Used
Tech	Purpose
Python 3	Core programming language
Tkinter	GUI interface
pyttsx3	Text-to-speech output
CSV Module	Save game history
datetime	Timestamping game results

🧠 How the Game Works
The user clicks one of the buttons: 🪨 Rock, 📄 Paper, or ✂️ Scissors.

The computer randomly chooses one of the three options.

The winner is decided based on standard rules:

Rock beats Scissors

Scissors beats Paper

Paper beats Rock

First to 3 wins the game.

Result is shown on the screen and spoken aloud.

Final scores are saved to a rps_game_results.csv file.

🚀 Getting Started
✅ Prerequisites
Make sure you have Python 3 installed. You also need the pyttsx3 library.

bash
Copy
Edit
pip install pyttsx3
▶️ Run the Game
bash
Copy
Edit
python rps_game.py
📁 File Structure
bash
Copy
Edit
rock-paper-scissors/
├── rps_game.py              # Main game script
├── rps_game_results.csv     # Game results saved here
├── README.md                # Project documentation
📷 Screenshots (Optional)
📌 Add screenshots of the GUI interface and result screen here if you're uploading to GitHub.

✅ Example Game Output
yaml
Copy
Edit
You: rock
Computer: scissors
Result: Player
Score → You: 1 | Computer: 0

📈 Sample CSV Output
javascript
Copy
Edit
Date,Player Score,Computer Score
2025-05-14 12:35:12,3,1
🔮 Future Enhancements
Add a leaderboard from the CSV history

Show visual icons for each choice

Add sound effects for win/loss

Implement multiplayer over LAN or web using sockets or Flask

🙋‍♂️ Author
P. Reethu Reddy
Micro IT Internship Project
2025

