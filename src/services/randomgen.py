from time import time_ns

class RandomGen:
    """for generating ranndom numbers
    """

    def __init__(self) -> None:
        self.divider = 1

    def random_number(self, lower_bound=0, upper_bound=100) -> int:
        """Generates random positive integer in the range specified. If no limits are set defaults
        to from 0 to 99. Uses time_ns as a seed and does few calculations to derive a random number.
        Can not handle ridicilously huge numbers (more than 15 digits or so).
        Args:
            lower_bound (int, optional): lower bound, inclusive. Defaults to 0.
            upper_bound (int, optional): upper bound, exclusive. Defaults to 100.

        Returns:
            int: random positive integer
            if lower_bound = upper_bound returns lower_bound
        """
        try:
            if lower_bound > upper_bound or lower_bound < 0 or upper_bound > 10**15:
                raise ValueError
            if lower_bound == upper_bound:
                return lower_bound
            while True:
                seed = time_ns()
                self.divider +=1
                if self.divider > seed//2:
                    self.divider = 1
                seed = seed // self.divider
                number = int(seed % upper_bound)
                if number in range(lower_bound, upper_bound):
                    return number
        except(ValueError,TypeError):
            print("""Incorrect arguments""")

randomgen = RandomGen()
