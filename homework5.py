tuple_ = 1, 2, 'a', 'b'
print(tuple_)
#tuple_ =[1] = 150
#print(tuple_)
#Ошибка сообщает, что кортеж относится к неизменяемым типам данных
tuple_ = ([1, 2, 0], 2)
print(tuple_)
tuple_[0][0] = 4
print(tuple_)