date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
journal = input("Let your thougts flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(journal)
