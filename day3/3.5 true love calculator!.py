print("Hello! Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# We lowercase the input so we can count correctly
name1_lower = name1.lower()
name2_lower = name2.lower()

# We count the letters
true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
true_letters = 0
love_letters = 0

# We still did not learn for loops in the course, but this solution made the most sense to me
for letter in true:
    true_letters += name1_lower.count(letter)
    true_letters += name2_lower.count(letter)
for letter in love:
    love_letters += name1_lower.count(letter)
    love_letters += name2_lower.count(letter)

# We calculate and give the total score back
total_score = true_letters * 10 + love_letters

# We return and comment on the love score
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos!")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together")
else:
    print(f"Your total score is {total_score}")