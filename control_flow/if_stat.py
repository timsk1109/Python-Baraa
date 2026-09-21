# if statement used with else.
score = 30

if score >= 90:
    print("A")
else:
    print("Try again")

#elif statement used 

if score >= 95:
    print("Your score: " + str(score) +" and grade is A")
elif score >=85 and score <= 94:
    print("Your score" + str(score) +" and grade is B")
elif score >= 75 and score <=84:
    print("Your score: " + str(score) +" and grade is C")
elif score >= 65 and score <= 74:
    print("your score: " + str(score) + " and grade is D")
else:
    print("You scored below 65, your grade is F")