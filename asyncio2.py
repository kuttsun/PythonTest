import asyncio
import time

# https://dev.classmethod.jp/etc/python-asyncio/

def fire_and_forget(task, *args, **kwargs):
    loop = asyncio.get_event_loop()
    if callable(task):
        return loop.run_in_executor(None, task, *args, **kwargs)
    else:    
        raise TypeError('Task must be a callable')

def foo(sec: int):
    print(f'start:  {sec}秒待ちます')
    time.sleep(sec)
    print(f'finish: {sec}秒待ちました')


fire_and_forget(foo, 3)

# プログラムが終了しないように待っているだけ（実際には以下は不要）
print(f'wait')
time.sleep(10)
print(f'exit')




# def foo(sec: int):
#     print(f'start:  {sec}秒待ちます')
#     time.sleep(sec)
#     print(f'finish: {sec}秒待ちました')

# loop = asyncio.get_event_loop()
# loop.run_in_executor(None, foo, 3)

# # プログラムが終了しないように待っているだけ（実際には以下は不要）
# print(f'wait')
# time.sleep(10)
# print(f'exit')