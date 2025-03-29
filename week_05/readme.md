## 1~4주차 복습하기
가. source, rendered html 실습 : python -m http.server --> F12로 'element', 'network'에서 비교

    * \week_03\rendered_html.html, week_03\source_html.html
    
나. requests 모듈 실습 :  python 실행모드에서(>>>) REST API 이해

    --> GET 방식과 POST(BODY) 방식 + POSATMAN(https://www.postman.com/)
```
    # https://requests.readthedocs.io/en/latest/user/quickstart/
        >>> import requests
        >>> r = requests.get('https://api.github.com/events')
        >>> print(r.status_code)
        >>> print(r.text)

        >>> print(r.status_code)
        >>> print(r.json())
        >>> res = requests.post(
            ...     'https://httpbin.org/post',
            ...     data={'조상구': '사람'},
            ...     headers={'Custom-Header': 'hello'}
            ... )
        >>> print(res.json()['headers'])
```
        
다. beautifulsoup 실습 : python -m http.server --> http://localhost:8000/

    * \week_03\soup_try.html, week_03\soup_try.ipynb

```
Text mining 하기 전에

1. preliminary snippet : 
    * webcrwal_text-mining.ipynb
    * 웹크롤링으로 얻은 text를 분석하고 예측모형에 투입될 입력변수를 수자로 표현하고(representation) 에측하는 것이 목적
```

## The Fundamental Text Minining 
### 5주차 ~ 7주차 강의 내용
*** 참고자료 : https://wikidocs.net/book/2155 

1. 텍스트마이닝 개요와 텍스트 전처리
2. 텍스트 표현 기법과 임베딩 (Representation)
3. LLM 기반 텍스트마이닝
4. 텍스트마이닝 실전 프로젝트

Week_05 : Topics
  1. tonizer
  2. stopword
  3. text data preprocessing

```
실습과제 : url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
--> 영화 평가 댓글이다. colab환경에서
1. url에서 압축파일을 다운받아 압축을 풀고
2. 디렉토리 aclImdb/train/pos/0_9.txt 훈련데이터를 다운받아
3. from nltk.tokenize import word_tokenize 로 불용어처리된 text를 토크나이저를 적용한 후
4. nltk.download('punkt'), nltk.download('stopwords') 모듈을 다운받아 불용어를 적용하고
5. from collections import Counter 로 단어의 출현빈도를 리스트로 만들어 워드클라우드로 시각화하고
6. 상위 N개 단어 보기, 전체 단어 수(중복 포함), 고유단어수, 5회 이상 등장 단어 등등 분석하라

```
