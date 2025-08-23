import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
alphabet_data = pandas.read_csv('nato_phonetic_alphabet.csv')

#Using Dict comprehension to create dict out of the pandas dataframe
alpha_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word:\n').upper()
code_words = [alpha_dict[character] for character in word]

print(code_words)




