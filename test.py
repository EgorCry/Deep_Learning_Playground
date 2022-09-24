# from time import time
#
# def timer_func(func):
#     def _timer(*args, **kwargs):
#         t1 = time()
#         result = func(*args, **kwargs)
#         t2 = time()
#         print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
#     return _timer
#
#
# @timer_func
# def long_time(n):
#     for i in range(n):
#         for j in range(100_000):
#             i*j
#     print('Done')
#
#
# long_time(1_000)


import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 complete')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 complete')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2


s_time = time.time()

asyncio.run(main())

print(time.time() - s_time)
