def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

"""
Previously the higher endpoint of the range function was 20, 
so 'i' was never assigned the value 20 and the if block was checking if 'i' was 20, 
so again the code was breaking
"""