"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(remaining_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - remaining_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate how long the lasagna would take to prepare based on the number of layers it will have

    Parameters:
        number_of_layers (int): The number of layers planned for the lasagna

    Returns:
        int: minutes of preparation time given the number of layers * time per layer

    """

    return number_of_layers * PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate how much total time has been spent making the lasagna

    Parameters:
        number of layers (int): the amount of layers the lasagna will have

    Returns:
        int: number of minutes of total time
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time