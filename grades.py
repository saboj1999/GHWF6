
def compute_hw_average(grades):
    """
    Compute the average grade for a list of assignment grades.

    Param: list of grades (all floats)
    Return: float representing the average grade
    """
    if len(grades) == 0:
        return 0
    return grades[0]
