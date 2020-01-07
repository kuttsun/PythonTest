
a = "hoge"
b = 1234
c = 0.1234
d = -1234
e = -0.1234
print(f'{a} {b} {c} {d} {e}')

# 左寄せ、中央寄せ、右寄せ
print(f'{a:>10}|{b:>10}|{c:>10}|{d:>10}|{e:>10}|')
print(f'{a:^10}|{b:^10}|{c:^10}|{d:^10}|{e:^10}|')
print(f'{a:<10}|{b:<10}|{c:<10}|{d:<10}|{e:<10}|')

# ゼロパディング
a = 1.2345
b = 1234
c = -1.2345
d = -1234
print(f'{a:08}')
print(f'{b:08}')
print(f'{c:08}')
print(f'{d:08}')

# 組み合わせ
a = 1.2345
b = 1.2
c = 1234
d = -1.2345
e = -1.2
f = -1234
# print(f'{a:.3f}')
# print(f'{b:.3f}')
# print(f'{c:.3f}')
# print(f'{d:.3f}')
# print(f'{e:.3f}')
# print(f'{f:.3f}')

# print(f'{a:>10.3f}|{b:>10.3f}|{c:>10.3f}|{d:>10.3f}|{e:>10.3f}|{f:>10.3f}|')
# print(f'{a:^10.3f}|{b:^10.3f}|{c:^10.3f}|{d:^10.3f}|{e:^10.3f}|{f:^10.3f}|')
# print(f'{a:<10.3f}|{b:<10.3f}|{c:<10.3f}|{d:<10.3f}|{e:<10.3f}|{f:<10.3f}|')

# 符号
# a = 1.2345
# b = 1.2
# c = 1234
# d = -1.2345
# e = -1.2
# f = -1234
# print(f'{a:+}')
# print(f'{b:+}')
# print(f'{c:+}')
# print(f'{d:+}')
# print(f'{e:+}')
# print(f'{f:+}')

a = 1.2345
b = -1.2345
print(f'{a:>+10}|{b:>+10}|')
print(f'{a:^+10}|{b:^+10}|')
print(f'{a:<+10}|{b:<+10}|')

# 桁区切り

a = 123456789.123456789
b = -123456789.123456789
print(f'{a:,.3f}')
print(f'{b:,.3f}')
# print(f'{a:>+10}|{b:>+10}|')
# print(f'{a:^+10}|{b:^+10}|')
# print(f'{a:<+10}|{b:<+10}|')


# 2進数、8進数、16進数
# 指数表記
# パーセント表記


# 書式指定を変数で指定
a = 1234
b = -1.234
digit = 10
print(f'{a:>{digit}}')
print(f'{b:>{digit}.1f}')