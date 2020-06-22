'''
싱글톤 디자인 패턴은 글로벌하게 접근 가능한 단 한 개의 객체만을 허용하는 패턴이다. 
따라서 싱글톤은 로깅이나 DB 관련작업, 프린터 스풀러 등의 애플리케이션에서 동일한 리소스에 대한 동시 요청의 
충돌을 막기 위해 한 개의 인스턴스만 필요한 경우에 주로 쓰인다. 

예를 들어, 데이터의 일관성 유지를 위해 db에 작업을 수행하는 한 개의 DB 객체가 필요한 경우 또는 
여러 서비스의 로그를 한 개의 로그 파일에 순차적으로 동일한 로깅 객체를 사용해 남기는 경우에 적합한 패턴이다. 

싱글톤 디자인 패턴의 목적은 다음과 같다. 
1. 클래스에 대한 단일 객체 생성
2. 전역 객체 제공 
3. 공유된 리소스에 대한 동시 접근 제어 

생성자를 private로 선언하고 객체를 초기화하는 static 함수를 만들면 간단하게 싱글톤을 구현할 수 있다. 
첫 호출에 객체가 생성되고 클래스는 동일한 객체를 계속 반환한다. 

하지만 파이선에서 생성자를 private으로 선언할 수가 없어서 다른 방법이 필요하다. 


파이썬에 인스턴스 생성하기 
new를 호출해서 인스턴스를 생성하고 init를 호출하여 인스턴스의 값을 넣는 구조가
파이썬의 인스턴스를 만드는 구조이다. 

A.__new__()를 가장 먼저 호출해서 클래스 객체를 생성하고 
init을 통해서 속성 값들을 초기화한다. 


python 매개변수 self와 cls 차이 그리고 static method에 대해서! 

* 가끔 기술된 파이썬 문서들을 보면 method 입력인자로 cls와 self가 들어가는 것을 본적이 있을 것이다. 
* 이 둘을 구분짓는 것은 'PEP8'에서 정의된 Instance method와 Class method의 차이에 따라 경우를 나누어 씁니다. 
* Instance Method의 정의는 클래스 내부에 정의되어 있는 함수를 호출할 때, 
Instance를 필요로 한다는 조건이 있는 것을 알 수 있습니다. 

이때 첫번째 매개변수는 항상 self이고, self 이외에 다른 변수를 사용하는 것은 어긋난 행동입니다. 

반면에, Class Method는 Instance Method와 다소 흡사하지만 
첫번째 매개변수를 보내는 일을 하지 않고, 클래스 자기 자신을 첫번쨰 
매개변수로 받는 차이가 있고, 또한 Class Method는 

'''


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new(cls)
        return cls.instance


s = Singleton()
print("object created ", s)

s1 = Singleton()
print("Object created ", s1)


'''
게으른 초기화는 싱글톤 패턴의 한 종류다. 모듈을 임포트할 때 