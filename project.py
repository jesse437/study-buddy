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
        print("coming soon!")
    elif option == "c":
        print("goodbye!")
        break
    else:
        print("Invalid choice")
        
        