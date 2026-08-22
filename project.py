import csv
import os

def check_answer(user_answer, correct_answer):
    return user_answer.lower().strip() == correct_answer.lower().strip()

def create_card(question, answer):
    file_exists = os.path.exists("flashcards.csv")
    with open("flashcards.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["question", "answer"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"question": question, "answer": answer})
    return True

print("This is Study Buddy...")

while True:
    
    print("a. create your own flash card")
    print("b. test me ")
    print("c. quit")
    
    option = input("Select: ").lower()

    if option == "a":
        question = input("Enter a question: ")
        answer = input("Enter an answer: ")
        create_card(question, answer)
            
        
    elif option == "b":
        if not os.path.exists("flashcards.csv"):
            print("No flashcards yet! Add some first.")
        else:
            score = 0
            total = 0
            with open("flashcards.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"question: {row['question']}")
                    answer = input("Enter answer!: ")
                    if check_answer(answer, row['answer']):
                        print("Correct!")
                        score += 1
                    else:
                        print("Wrong!")
                    total += 1
                print(f"You got {score} out of {total}!")
        
    elif option == "c":
        print("goodbye!")
        break
    else:
        print("Invalid choice")
        
        
if __name__ == "__main__":
    main()