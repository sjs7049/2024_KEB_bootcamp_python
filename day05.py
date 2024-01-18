univ = 'inha university'
count_alphabet = {letter: univ.count(letter) for letter in univ}
print(count_alphabet)

counts_alphabet = dict()
for letter in univ:
    counts_alphabet[letter] = univ.count(letter)
print(counts_alphabet)