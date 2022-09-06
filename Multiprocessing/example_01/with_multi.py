"""
    Very Simple Example with using Multiprocessing!
"""
import multiprocessing
import time

def counter_01(num: int) -> None:
    count = 0
    for _ in range(num):
        count += 1
    print("Counter 01 is Done!")



def counter_02(num: int) -> None:
    count = 0
    for _ in range(0, num, 2):
        count += 1
    print("Counter 02 is Done!")


if __name__ == "__main__":
    st = time.time()
    number = 2 * 10 ** 8
    process_01 = multiprocessing.Process(target=counter_01, args=(number,))
    process_02 = multiprocessing.Process(target=counter_02, args=(number,))

    process_01.start()
    process_02.start()

    process_01.join()
    process_02.join()
    
    en = time.time()
    print(f"Total time took: {en - st}")
