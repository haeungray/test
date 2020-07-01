# GIL

import random, datetime, threading, time

def calc():
    max([random.random() for i in range(500000)])
    max([random.random() for i in range(500000)])
    max([random.random() for i in range(500000)])

# 1 Threads
start_time = datetime.datetime.now()
calc()
calc()
end_time = datetime.datetime.now()
print(end_time - start_time)


# 2 Threads
start_time = datetime.datetime.now()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=calc))
    threads[-1].start()


for t in threads:
    t.join()
 
end_time = datetime.datetime.now()
print(end_time - start_time)

'''
이상하게도 멀티쓰레딩의 수행 시간이 2초 정도 더 소요되었다. 어째서 이러한 결과가 나오는지 궁금했는데, 그 이유는 파이썬에서 Global Interpreter Lock (이하 GIL) 이라고 부르는 동기화 방식 때문이다.
'''
