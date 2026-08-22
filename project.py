import csv
import os


print("This is Study Buddy...")

while True:
    
    print("a. create your own flash card")
    print("b. test me ")
    print("c. quit")
    
    option = input("Select: ").lower()

    if option == "a":
        question = input("Enter a question: ")
        answer = input("Enter an answer: ")
        
        file_exists = os.path.exists("flashcards.csv")
        
        
        with open("flashcards.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["question", "answer"])
            if not file_exists:
                writer.writeheader()
            writer.writerow({"question": question, "answer": answer})
            
        
    elif option == "b":
        if not os.path.exists("flashcards.csv"):
            print("No flashcards yet! Add some first.")
        else:
            with open("flashcards.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"question: {row['question']}")
                    answer = input("Enter answer!: ").lower().strip()
                    if answer == row['answer'].lower().strip():
                        print("Correct!")
                    else:
                        print("Wrong!")
        
    elif option == "c":
        print("goodbye!")
        break
    else:
        print("Invalid choice")
        
        
    