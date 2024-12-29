word = input()
vowels = "aeiouy"
for vowel in vowels:
    word = word.replace(vowel, '')
print("YES" if word == word[::-1] else "NO")