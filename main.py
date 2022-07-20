import random
names = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]

scores = {name: random.randint(1, 100) for name in names}

passed = {name: score for (name, score) in scores.items() if score >= 60}
print(scores)

print(passed)
