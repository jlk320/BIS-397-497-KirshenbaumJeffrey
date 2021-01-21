
Alphabet= 'abcdefghijklmnopqrstuvwxyz'
def summarize_letters(string):
    letters=[]
    counts=[]
    
    for letter in string.lower():
        if letter in Alphabet:
            if letter in letters:
                index=letters.index(letter)
                counts[index] +=1
            else:
                letters.append(letter)
                counts.append(1)
    tuples = list(zip(letters,counts))
    tuples.sort()
    return tuples

sample = 'Jeff Kirshenbaum is Awesome and the Best'
summary = summarize_letters(sample)

for char, count in summary: 
    print(f'{char}:{count}')
    
all_letters = True 

if len(summary) == len(Alphabet):
    for item in summary:
        if item[0] not in Alphabet:
            all_letters = False
            break
else:
    all_letters = False 
    
    if all_letters:
        print(f' "{sample}" contains all letters in the alphabet')
    else: 
        print(f'"{sample}" does not contain all letters in alphabet ')