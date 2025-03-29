# __init__.py
# 이 파일은 패키지를 초기화하면서 필요한 클래스를 한 번에 불러오고
# 외부에서 어떤 모듈만 사용할 수 있을지 정리하고 로깅 등 초기 설정을 한다.

# .module1 : 상대 경로 import (같은 패키지 내)	패키지 내부 모듈에서 다른 모듈을 가져올 때
from .module1 import MyClass
from .module2 import useful_function

__all__ = ['MyClass', 'useful_f.unction']  # optional

print('Done from __init__.py')  # 언제 수행되는지 확인하려고고

# Setup code (optional)
import logging

logging.basicConfig(level=logging.INFO)
logging.info("mypackage is ready!")
