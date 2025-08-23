year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")


"""
Previously the '=' sign was missing from the elif block, so the year 1994 was not at all checked.
Now it's fixed.
"""