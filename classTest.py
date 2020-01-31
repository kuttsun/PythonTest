class Hoge:
    def __init__(self, id):
        self.__id = id
    
    def print_id(self):
        print(self.__id)


hoge1 = Hoge(1)
hoge2 = Hoge(2)

# 以下は例外が発生する
#print(hoge1.__id)
#print(hoge2.__id)

hoge1.print_id()
hoge2.print_id()
    