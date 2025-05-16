# Quizoku 📝

A modern Python quiz application built with Tkinter and ttkbootstrap, featuring a sleek user interface and comprehensive quiz management system.

## Features ✨

- Modern and responsive GUI using ttkbootstrap
- Support for multiple question types:
  - Multiple Choice Questions (MCQ)
  - Fill in the Blanks
  - True/False Questions
- Student information tracking
- Detailed quiz results with score calculation
- Automatic result saving with timestamps
- Progress tracking during quiz
- Immediate feedback on answers

## Prerequisites 📋

- Python 3.x
- pip (Python package installer)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Quizoku.git
cd Quizoku
```

2. Install the required dependencies:
```bash
pip install ttkbootstrap
```

## Project Structure 📁

```
Quizoku/
├── Quizoku.py          # Main application file
├── Quizsheet.csv       # Quiz questions database
└── Results/            # Directory for quiz results
```

## Results 📈

Quiz results are automatically saved in the `Results` directory with the following format:
```
YYYY-MM-DD_StudentName_StudentID_results.txt
```

Each result file includes:
- Student information
- Final score and percentage
- Detailed breakdown of each question
- Correct and incorrect answers

## Author 👨‍💻

- **Clyde Heinrich "Birdabo"**
- Created: May 1st, 2025

## License 📄

This project is open source and available under the MIT License.

## Acknowledgments 🙏

- ttkbootstrap for the beautiful UI components
- Python Tkinter for the GUI framework
