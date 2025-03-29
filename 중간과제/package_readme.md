## package 에서 __init__.py  이해하기 :

week_05/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module1.py
    └── module2.py
- 새 집으로 이사 간다고 상상해봐. 현관문 앞에 "안녕하세요! 여기가 우리 집이에요." 라는 환영 매트가 깔려 있어.
- Python에서 __init__.py 파일은 이 환영 매트와 비슷한 역할을 해. Python에게 이렇게 말해주는 거지:
- “이 폴더는 패키지야—서로 관련된 코드들이 모여 있는 특별한 공간이야.” 이 파일이 있으면
- Python은 그 폴더를 패키지로 인식하고, 그 안에 있는 모듈들을 제대로 사용할 수 있게 돼.
- Imagine you’re moving into a new home. At the door, you have a welcome mat that says, “Hello! This is our home.” In Python, the __init__.py file works a lot like that welcome mat. It tells Python, “This folder is a package—a special place where related code lives.”
