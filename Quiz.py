print("===================================")
print("     GENERAL KNOWLEDGE QUIZ")
print("===================================")

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Paris.")

print()

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Mars.")

print()

# Question 3
answer = input("3. What is the largest ocean on Earth? ").strip().lower()

if answer == "pacific ocean" or answer == "pacific":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Pacific Ocean.")

print()
print("===================================")
print(f"Your Final Score: {score}/3")
print("===================================")

if score == 3:
    print("🏆 Excellent! You got all answers correct.")
elif score == 2:
    print("👍 Good Job! Keep practicing.")
elif score == 1:
    print("🙂 Nice try! Practice more.")
else:
    print("📚 Better luck next time!")