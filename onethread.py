from time import sleep, time, ctime

def loop0():
    print("start loop 0 at : ", ctime(time()))
    sleep(4)
    print("loop 0 done at : ", ctime(time()))

def loop1():
    print('start loop 1 at : ', ctime(time()))
    sleep(2)
    print("loop 1 done at : ", ctime(time()))

def main():
    print("starting ...")
    loop0()
    loop1()
    print("All Done at :", ctime(time()))


'''
ctime은 일반 날짜가 아니다
ctime함수의 반환값인 'Sun Oct 11 12:00:50 2015'와 같이 정확한 문구가 나온다.
starting ...
start loop 0 at :  Fri May 15 00:32:41 2020
loop 0 done at :  Fri May 15 00:32:45 2020
start loop 1 at :  Fri May 15 00:32:45 2020
loop 1 done at :  Fri May 15 00:32:47 2020
All Done at : Fri May 15 00:32:47 2020
'''
if __name__ == "__main__":
    main()