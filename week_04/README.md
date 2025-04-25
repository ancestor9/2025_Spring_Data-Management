## week_03 보충 ##
1. 인용문(https://quotes.toscrape.com/) 검색하기 (tag 별로 10페이지씩 순회)

## week_04 ##
Summary : 웹 스트래핑 Rule (F12 > copy > LLM prompts)
    -----------------------------------------------------------------------------
    | html 종류        | 파이썬 module                          |
    -----------------------------------------------------------------------------
    | Static (정적)    | requests, bs, trafilatura, re          | 
    | Dynamic (동적)   | requests, bs, selenium, crawl4AI, re   |  LLM 방식에 적합한 markdown 형태 데이터
    -----------------------------------------------------------------------------
----------
2. 네이버웹툰 만화 제목 추출(source_rendered html, 모두 Handling 가능)
  ---> crawl4AI Module
 https://docs.crawl4ai.com/core/quickstart/ 
 . url = 'https://www.nbcnews.com/business'로 크롤링 해보기 (optinal)
 . url = "https://comic.naver.com/webtoon/weekday" dynamic html 크롤링해보기
3. trafilatura Module: 정적 웹만
4. re moduel 실습 (Regular Expression, 정규표현식)
5. 실습과제
  - https://github.com/PacktPublishing 은 주로 프로그래밍, 웹 디자인, 데이터 분석, 하드웨어 등 정보 기술과 관련된 인쇄 및 전자 서적과 비디오를 출판
  5.1. 해당 url의 모든 페이지(1~297 페이지)를 순회하면서 책의 제목, 깃헙url, 인기(*star)의 순서로 스크래핑하라
       * 깃허브 서버가 robot crawling을 눈치못 채게, user agent, 깃허브 토큰 사용, 비동기방식 고려 등등

        | 제목       | URL           | *Stars |
        |------------|---------------|--------|
        | Hands-On...| https://gi.... | 852    |
        | Java-Codi...| https://gi... | 797    |
        | Modern-Co...| https://gi... | 788    |
        | Learning-...| https://gi... | 656    |
        | Mastering...| https://gi... | 651    |
        | Developin...| https://gi... | 0      |
        | Learning-...| https://gi... | 0      |
        7338 rows × 3 columns

  5.2. 책의 제목에서 가장 많이 나온 단어를 상위10가를 추출하라 (정규표현식, regular expression을 사용, import re)
  5.3. and, with 와 같은 단어(불용어, stopword)는 제거하고 Wordcloud를 그려라

 ---> 전체 코드를 제출하여 깃허브 주소를 구글시트에 기록하라 (eclass에 제출, mandatory)

6. 구글기사검색 API
   - serpapi


