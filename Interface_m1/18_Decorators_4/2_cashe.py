"""
Еще один декоратор который может помочь при каких то больших и длительных операциях. Это декоратор @cache.
Он позволяет кэшировать, т.е временно сохранить результат, для быстрого доступа к нему.
"""
import time
from functools import cache


@cache
def func(n):
    result = 0
    for i in range(n):
        result += i
    return result


start1 = time.time()
print(func(100000000))
end1 = time.time()
print(end1 - start1, 'секунд')
start2 = time.time()
print(func(100000000))
end2 = time.time()
print(end2 - start2, 'секунд')
start3 = time.time()
print(func(100000001))
end3 = time.time()
print(end3 - start3, 'секунд')
