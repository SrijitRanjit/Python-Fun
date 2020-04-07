#
# piglatin.py : convert any string to pig latin
#

vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O']
instring = input('Enter the string')
firstletter = instring[0]
print('\nfirst letter is: ', firstletter)
for index in range(0, len(vowels)-1):
    if firstletter == vowels[index]:
        print('\nits a vowel so...')
        print(instring + '-' + 'ay')
print('\nits a consonant so: ')
print(instring[1:len(instring)] + '-' + firstletter + 'ay')
