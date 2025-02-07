studentsNameAndScore = {}

while True:
    name = input("\nEnter your name or 'done' to stop: ")
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

if studentsNameAndScore != {}:
 print("\nStudent score:")
 for student, studentScores in studentsNameAndScore.items():
   print(f"{student.title()} - {studentScores}")
 
 listOfScores = []
 for studentScores in studentsNameAndScore.values():
   listOfScores.append(studentScores)
   highestScore = max(listOfScores)
   lowestScore = min(listOfScores)
   averageScore = sum(listOfScores) / len(listOfScores)
 print(f"\nAverage score: {averageScore:.2f}")

 for key, value in studentsNameAndScore.items():
      if value == highestScore:
        print(f"Highest score: {key.title()} ({highestScore})")
      if value == lowestScore:
         print(f"Lowest score: {key.title()} ({lowestScore})")

else:
   print("Sorry, no data inputed..")

   