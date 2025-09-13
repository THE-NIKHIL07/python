'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number 

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time=time.time()

    ##create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)
# Creates a pool of worker processes (default = number of CPU cores).

# pool.map() → Distributes the list of numbers across the worker processes.

# Example: One process handles 5000!, another 6000!, etc.

# Runs them in parallel on different cores.

# Collects results in the list results.
    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")

