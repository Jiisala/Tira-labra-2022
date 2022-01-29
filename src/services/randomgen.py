from time import time_ns
class RandomGen:
    """for generating ranndom numbers
    """
    
    def __init__(self) -> None:
        pass
    
    def random_number(self, min =0, max =10) -> int:
        """Generates random positive integer in the range specified. If no limits are set defaults to from 0 to 9
        Uses time_ns as a seed and simply returns the last digit(s). Max nuber of digits 19.
        Args:
            min (int, optional): lower bound, inclusive. Defaults to 0.
            max (int, optional): upper bound, exclusive. Defaults to 10.

        Returns:
            int: random positive integer
            if lower bound = upper bound returns lower bound  
        """
        if min > max or min < 0 or max > 10**20:
            print ("Error handlnig goes here")
            return None
        if min == max:
            return min
        digits = len("%i" % max)
        while True:
            seed = time_ns()
            #print (seed)
            number = seed % (10 **digits)
            if number in range(min, max):
                return number    

randomgen = RandomGen()