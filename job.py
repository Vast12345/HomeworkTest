phrase = str("""Jacob takes the ladder and leans it against the tree. He starts to climb up and tries not to look down. He cannot believe he is doing this. His neighbor’s cat climbed up the tree in front of the house and cannot climb down. Now normally, Jacob would not offer to rescue a cat in a tree. He is afraid of heights, ladders and cats. But his neighbor, Anita, is gorgeous and rescuing her cat would be the perfect way to be a hero and get her attention.

He is almost there. The ladder begins to shake and he looks down and realizes how high he is. He looks at his beautiful neighbor and decides that it is not worth it. He screams loudly “HELP!!! I’M FALLING!!!” The cat suddenly jumps from the tree onto his head. They both fall to the ground and the cat runs to her owner. Anita runs to Jacob, who is lying on the ground.

“Thank you so much”, she says. “That was very heroic! I hope you are not hurt.”

“It was nothing”, he whispers. “By the way, if it’s not too much trouble, would you be so kind as to call me an ambulance?\"""")
#print(phrase)

letterCount = len(phrase)
onlyLetters = [char for char in phrase if char.isalpha()]
onlyLetterCount = len(onlyLetters)
onlyCharacters = sum(1 for char in phrase if not char.isalpha())

uppercaseLetters = phrase.upper()
lowercaseLetters = phrase.lower()

print(uppercaseLetters)
print(lowercaseLetters)
print(onlyLetterCount)
print(onlyCharacters)

print_letter_count = input()
print_only_letters = input()
print_only_letter_count = input()
print_only_characters = input()

'''inputted_number = input()

if inputted_number == '1':
    print()'''
