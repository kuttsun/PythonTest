import time
import concurrent.futures


def func1():
    for i in range(100):
        print("func1")
        time.sleep(0.01)
    print("func1_end")

def func2():
    for i in range(100):
        print("func2")
        time.sleep(0.01)
    print("func2_end")


executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
executor.submit(func1)
executor.submit(func2)

print("wait")
time.sleep(5)
print("end")
