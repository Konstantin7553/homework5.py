tuple_ = 1, 2, 'a', 'b'
print(tuple_)
#tuple_ =[1] = 150
#print(tuple_)
#Ошибка сообщает, что кортеж не поддерживает обращение к элементам
tuple_ = ([1, 2, 0])
print(tuple_)
tuple_[0][0] = 4
print(tuple_)