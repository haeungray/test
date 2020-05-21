from random import *
import string 

_LENGTH = 10
i = randint(1,100)
string_pool = string.ascii_lowercase # 소문자
string_pool = string.ascii_uppercase # 대문자
# function for a in range(n)  구문 암기 

print("".join(choice(string.ascii_uppercase + string.digits) for _ in range(3)))