word_1 = input("input your first word ")
word_2 = input("input your second word ")

intersection = set(word_1) and set(word_2)



outcome = " "

for char in word_1:
    if char in intersection and char not in outcome:
        outcome += char

print(outcome)
print(intersection)