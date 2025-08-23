word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

"""
Previously in line 3, relational operator was used ('==') instead of assignment operator ('='), so the 
code was breaking. Now it's fixed.
"""
