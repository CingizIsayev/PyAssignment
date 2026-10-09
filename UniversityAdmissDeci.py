examscore = int(input("Enter your exam score: "))
schoolscore = int(input("Enter your school score: "))
age = int(input("Enter your age: "))

if age < 16:
    print("You are too young to apply. REJECTED")
if age >= 16:
    if examscore > 0 and examscore < 700:
        if schoolscore > 0 and schoolscore < 101:
            if examscore >= 600 : 
                print("SCOLARSHIP BABYYYY")
            elif examscore < 600:
                print("Application is APPROVED. Congratulations!")
            elif examscore < 451:
                if schoolscore >= 80:
                    print("Application is APPROVED. Congratulations!")
                elif schoolscore < 80:
                    print("Application is REJECTED. LOW SCHOOL SCORE!")
            elif examscore < 300:
                print("Application is REJECTED. LOW EXAM SCORE!")
        else:
            print("Invalid school score. Please enter a score between 0 and 100.")