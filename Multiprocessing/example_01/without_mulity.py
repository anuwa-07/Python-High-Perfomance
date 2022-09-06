"""
    Very Simple Example for Single Processing Task
"""

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
    counter_01(num=number)
    counter_02(num=number)

    en = time.time()
    print(f"Total time took: {en - st}")

