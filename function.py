from collections import deque

# C# のデリゲートのようなことをしたい
def apply_async(func, args, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

q = deque(maxlen=10)

q.append({
    'func': add, # 実行したい関数
    'args': (3, 2), # 実行したい関数に渡したい引数
    'callback': print, # 結果を受け取るコールバック関数
})

q.append({
    'func': sub, # 実行したい関数
    'args': (3, 2), # 実行したい関数に渡したい引数
    'callback': print, # 結果を受け取るコールバック関数
})

while len(q) > 0:
    # キューから取出して実行
    hoge = q.popleft()
    ret = hoge['func'](*hoge['args'])
    # 結果をコールバック関数に渡す
    hoge['callback'](ret)