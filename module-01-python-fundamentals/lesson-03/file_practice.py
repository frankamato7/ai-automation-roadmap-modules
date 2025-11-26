
#Warmup #1
with open('note.txt', 'w') as f:
    f.write('Hello, this is my first note!\n')

#Warmup #2
with open('note.txt', 'r') as f:
    print(f.read())

#Warmup #3
with open('note.txt', 'a') as f:
    f.write('This is an appended line')

#Warmup #4
with open ('note.txt', 'r') as f:
    lines = f.readlines()
    print(lines)