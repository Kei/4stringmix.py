import random
import requests

def generate_word(word_list):
    while True:
        word = random.choice(word_list)
        if len(word) <= 6 and sum(1 for char in word if char in 'aeiou') <= 3:
            return word

def generate_number():
    return str(random.randint(1, 9999))

# Fetch the word list from the web
response = requests.get("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt")
word_list = response.text.lower().splitlines()

filtered_word_list = [word for word in word_list if len(word) <= 6 and sum(1 for char in word if char in 'aeiou') <= 3]

output = []

# Generate 2-3 words
word_count = random.randint(2, 3)
for _ in range(word_count):
    output.append(generate_word(filtered_word_list))

# Generate a number sequence
output.append(generate_number())

# Fill any remaining slots with words
while len(output) < 4:
    output.append(generate_word(filtered_word_list))

# Shuffle the output list
random.shuffle(output)

# Print the generated output without line breaks
print(' '.join(output), end='\n')
