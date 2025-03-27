# main.py

from mypackage import MyClass, useful_function

obj = MyClass()

print(obj.greet())

print(useful_function())


'''
init__.py : 해당 디렉토리를 패키지로 인식하게 함
내부 코드 실행 : logging.info()는 import될 때 자동 실행됨
from ... import : init__.py 덕분에 MyClass, useful_function을 직접 패키지에서 가져올 수 있음
all : 패키지를 from mypackage import * 했을 때 가져올 대상 제한
'''

'''
실습해 볼 것 !
실습 1. init__.py를 비워놓고 어떤 일이 벌어지는지 실험
실습 2. all__ 목록에 일부만 포함시켜보고 외부에서 접근 가능한지 확인
'''