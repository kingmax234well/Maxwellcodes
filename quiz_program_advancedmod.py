# Define quiz questions, options, an answers
quiz_questions = {
    "What is the capital of France?": {
        "A": "Paris",
        "B": "London",
        "C": "Berlin",
        "D": "Rome",
        "Answer" : "A"
    },
    "What is the largest planet in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "Answer" : "C"
    },
    "What is the smallest country in the world?": {
        "A": "Monaco",
        "B": "Vatican city",
        "C": "Nauru",
        "D": "Tuvalu",
        "Answer" : "B"
    },
    "What is the chemical symbol of gold?": {
        "A": "Ag",
        "B": "Au",
        "C": "Hg",
        "D": "Pb",
        "Answer" : "B"
    },
    "Who painted the Mona lisa?": {
        "A": "Michelangelo",
        "B": "Raphael",
        "C": "Caravaggio",
        "D": "Leonardo da vinci",
        "Answer" : "D"
    },
    "What is the largest mammal on Earth?": {
        "A": "Blue whale",
        "B": "Fin whale",
        "C": "Humpback whale",
        "D": "Sperm whale",
        "Answer" : "A"
    },
    "Which element has the atomic number 1?": {
        "A": "Helium",
        "B": "Hydrogen",
        "C": "Oxygen",
        "D": "Nitrogen",
        "Answer" : "B"
    },
    "Who wrote Romeo and Juliet?": {
        "A": "William Shakespare",
        "B": "Jane Austen",
        "C": "Charles Dickens",
        "D": "J.K Rowling",
        "Answer" : "A"
    },
    "What is the largest living structure on the Earth?a": {
        "A": "The Amazon Rainforest",
        "B": "The Grand Canyon",
        "C": "The Great Barrier Reef",
        "D": "Th Great Wall of China",
        "Answer" : "C"
    },
    "Which programming language is used for this quiz?": {
        "A": "Java",
        "B": "Python",
        "C": "C++",
        "D": "Javascript",
        "Answer" : "B"
    },
}

def run_quiz(questions):
    player_score = 0
    for question, options in questions.items():
        print(question)
        for option, value in options.items():
           if option != "Answer":
               print(f"{option}: {value}")
        while True:
         try:
          answer = input("Choose the correct option (A, B, C, D): ").upper()
          if answer in["A", "B", "C", "D"]:
            if answer == options["Answer"]:
               print("Correct!\n")
               player_score += 1
            else:
               print(f"Sorry, the correct answer is {option['Answer']}: {options['Answer']}\n")
            break
          else:
              print("Invalid option! Please choose within the four given options")
         except(TypeError):
            print("Wrong answer! Try Again.")
    return player_score

def main():
    print("Welcome to the quiz! :) :) ")
    player_score =run_quiz(quiz_questions)
    print(f"Quiz finished! Your final score is {player_score} out of {len(quiz_questions)}.")
    print("Your percentage accuracy is " + str(int(player_score/10 * 100)) + "%")

if __name__ == "__main__":
    main()

    