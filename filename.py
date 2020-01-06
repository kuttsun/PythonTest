from os import path

# https://improve-future.com/get-the-current-script-file-name-in-python.html
print(__file__)
print(path.basename(__file__))
print(path.splitext(path.basename(__file__))[0])
print(path.abspath(__file__))
print(path.dirname(__file__))
print(path.abspath(path.dirname(__file__)))