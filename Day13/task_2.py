from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 5)
print(dice_images[dice_num])


"""
Previously line no 3 was 'dice_num = randint(1,6)', 
so at times when the dice_num was getting value as 6, 
then the whole code was breaking.
"""