
import math
import multiprocessing
import time


def check_prime(number: int) -> list:
    arr = [True]*number
    for num in range(number):
        if num < 2:
            arr[num] = False
        elif num > 2:
            for j in range(2, math.ceil(math.sqrt(num)) + 1):
                if num % j == 0:
                    arr[num] = False
                    break
    return arr


# Now rewrite the check_prime() func which can work with multiprocessing
def chech_prime_v2(number: int) -> list:
    """
        Not like above func we make a this func as to check a single number and return it's result.
        So we can run this func in parallel. Because every task is indipendant for each other.
    """
    if number < 2:
        return number, False
    elif number == 2:
        return number, True
    else:
        for j in range(2, math.ceil(math.sqrt(number)) + 1):
            if number % j == 0:
                return number, False
    return number, True


if __name__ == "__main__":
    number = 2 * 10 ** 6

    # Single Processing Code
    st = time.time()
    results = check_prime(number=number)
    print(results[:30])
    en = time.time()
    print(f"Total time took for single processing code: {en - st}\n")

    # Multiprocessing code
    st = time.time()
    num_arr = range(number)
    num_processers = 10

    with multiprocessing.Pool(processes=num_processers) as pool:
        results = pool.map(chech_prime_v2, num_arr)
    pool.close()
    print(results[:30])
    en = time.time()
    print(f"")
    print(f"Total time took for Multiprocessing code: {en - st}")






