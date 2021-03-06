import asyncio
import time

# https://dev.classmethod.jp/etc/python-asyncio/

async def sleeping(sec):
    loop = asyncio.get_event_loop()
    print(f'start:  {sec}秒待つよ')
    await loop.run_in_executor(None, time.sleep, sec)
    print(f'finish: {sec}秒待つよ')
 
 
def main():
    array = [5, 1, 8, 3, 4]
 
    loop = asyncio.get_event_loop()
 
    print('=== 一つだけ実行してみよう ===')
    loop.run_until_complete(sleeping(2))
 
    print('\n=== 5つ並列的に動かしてみよう')
    gather = asyncio.gather(
        sleeping(5),
        sleeping(1),
        sleeping(8),
        sleeping(3),
        sleeping(4)
    )
    loop.run_until_complete(gather)
 
 
if __name__ == '__main__':
    main()