def func(num):
   while num > 0:
       yield num
       num -= 1


for num in func(5):
   if num == 2:
       break
   print(num)

"""
Здесь цикл for прерывается вызовом break и связанный с ним генератор никогда не отрабатывает до завершения. 
"""