studentsNameAndScore = {}

while True:
    name = input("\nEnter your name of 'done' to stop: ")
    if name.lower() == 'done':
     break

    scoreInput = input("Enter your score or 'done' to quit: ")

    if scoreInput.lower() == 'done':
       break
    score = int(scoreInput)
    if score > 100  or score < 0:
       print("Sorry, score can't be greater than 100 or less than zero(0).")
       break
    else:
        print(f"{name.title()}'s score is {scoreInput}.")

    studentsNameAndScore[name] = score
print(studentsNameAndScore)


listOfScores = []
print("\nStudent score:")
for student, studentScores in studentsNameAndScore.items():
   print(f"{student.title()} - {studentScores}")

for student,studentScores in studentsNameAndScore.items():
   listOfScores.append(studentScores)
highestScore = f"{student} ({max(studentsNameAndScore.values())})"
lowestScore = f"{student} ({min(studentsNameAndScore.values())})"



print(f"\nAverage score: {sum(listOfScores)/len(listOfScores)}")
print(f"Highest score: {highestScore}")
print(f"Lowest score: {lowestScore}")


  

   