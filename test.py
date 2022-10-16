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
#

# import asyncio
# import time
#
#
# async def fun1(x):
#     print(x**2)
#     await asyncio.sleep(3)
#     print('fun1 complete')
#
#
# async def fun2(x):
#     print(x**0.5)
#     await asyncio.sleep(3)
#     print('fun2 complete')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# s_time = time.time()
#
# asyncio.run(main())
#
# print(time.time() - s_time)

def metric(y_test, y_pred, threshold):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for i in range(len(y_pred)):
        if (y_pred[i] >= threshold):
            if (y_test[i] == 1):
                tp += 1
            else:
                fp += 1
        elif (y_pred[i] < threshold):
            if (y_test[i] == 0):
                tn += 1
            else:
                fn += 1

    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)

    return [fpr, tpr]


thresholds = [0, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75, .8, .85, .9, .95, 1]

roc_points = []
for threshold in thresholds:
    rates = metric(list(y_test), y_pred[:, 1], threshold)
    roc_points.append(rates)