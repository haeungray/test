'''
파이썬에서 명령을 실행하거나 디스크의 파일을 실행하는 방법은 여러가지가 있다.
이들을 적용하는 방안은 그 목적이 무엇인가에 따라 달라진다. 
일반적인 시나리오로는 다음과 같은 것들이 존재한다.
    1. 현재 스크립트 안에 실행 유지하기
    2. 서브 프로세스 생성하고 관리하기
    3. 외부 명령이나 프로그램 실행하기
    4. 입력을 요구하는 명령 실행하기
    5. 네트워크를 통해서 명령 호출하기
    6. 처리가 필요한 출력을 생성하는 명령 실행하기
    7. 다른 파이썬 스크립트 실행
    8. 동적으로 생성된 일련의 파이썬 구문 실행하기 

위에서 기술한 기능을 제공하는 내장 모듈이나 외부 모듈이 있다. 

많은 파이썬 객체들이 "callable"인데, 이것은 함수 연산자 () 를 가지고 호출할 수 있는 객체라는 의미이다.
이 함수 연산자는 호출할 객체의 이름 바로 뒤에 놓인다.

이미 알고 있듯이 callable 객체들은 기능적 프로그램이 인터페이스를 통해서 호출할 수 있다. 

파이썬은 네 가지의 callable 객체를 가지는데, 함수, 메소드, 클래스, 그리고 어떤 클래스 인스턴스이다.
이러한 객체의 어떠한 부가적인 참조나 별칭들도 역시 callable이라는 점을 염두해 두자.
'''


# BIFs(Built-in Functions)
# 내장 함수 : 파이썬 인터프리터로 컴파일되어 가장 먼저 
# 네임스페이스의 부분으로 시스템에 적재된다. 
# 이러한 함수들은 __builtin__ 모듈 안에서 발견할 수 있고, 
# __builtins__ 모듈로서 인터프리터에 임포트된다. 
# 제한된 실행 모드에서는 이 함수들 중 일부만이 사용 가능하다. 

# 이러한 속성들은 내장 함 수 dir() 을 이요해 검증할 수 있다.
# 내부적으로 내장 함수는 내장 메소드와 같은 형태로 표현되기 때문에
# 내장 함수나 내장 메소드 위에 type() 내장 함수를 호출하는 것은 아래에 나타난 것처럼 "builtin function or method" 를 출력한다. 
type(type)



# UDF(User-Define Funtion)
# 사용자 정의 함수 
# 일반적으로 모듈의 최상위 레벨 부분에 정의되고, 전역 네임스페이스의 부분으로서 적재된다. 
# 함수는 다른 함수 안에서 정의될 수 있다. 
# 그러나 가장 안쪽에 있는 함수는 자신을 포함하는 함수의 지역 범위에 접근할 수 없다. 
# 앞장에서 언급한 바와 같이 현재 파서 함수 안에서 정의된 모든 이름들은 지역 네임스페이스의 부분이다. 

udf.__doc__
udf.__name__
udf.func_code
udf.func_defaults # Default argument tuple
udf.func_globals  # 함수 안에서 globals를 호출하는 것과 같다 ? ... 




