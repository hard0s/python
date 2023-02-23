import random

with open('test.txt') as f:
    lines = f.readlines()

qa_pairs = [line.strip().split('|') for line in lines]
question, answer = random.choice(qa_pairs)
user_answer = input(question + '\n')

if user_answer.strip().lower() == answer.lower():
    print('Correct!')
else:
    print(f'Sorry, the correct answer is "{answer}".')