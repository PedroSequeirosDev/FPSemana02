sentence = str(input("write a phrase of your choice "))

words = sentence.split(" ")

output = {}

for letters in words:
    output[letters]=len(letters)

print (output)