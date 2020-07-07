'''
파이썬의 GIL 하에서는 코어가 몇 개든 상관없이 
특정 시점에서 하나의 코어만 실행된다. 
멀티코어 시대에 뒤쳐져 보일 수 있겠지만, 
GIL은 이렇게 특정 시점에서 언제나 하나의 쓰레드만 실행하도록 만든 것이다. 
다시 말해서 특정 시점에서 인터프리터를 사용하는 쓰레드는 언제나 1개라는 것이다.

그렇다면, 왜 파이썬은 GIL을 채택했을까?
'''
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
