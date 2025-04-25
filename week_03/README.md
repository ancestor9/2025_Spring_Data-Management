# 📌 정적(Static Web Page) 크롤링과 데이터프레임 생성

## 🏫 강의 내용

### 1. Source HTML vs. Rendered HTML 
### 1.1 source_html.html, rendered_html.html 실습
### 1.2 F12의 element와 network 이해하기기

### 2. 웹 크롤링(Crawling)과 웹 스크래핑(Scraping)

### 2.1 `requests` 모듈 이해하기
- `requests` 라이브러리는 HTTP 요청을 보낼 수 있도록 도와주는 파이썬 라이브러리
- 공식 문서: [requests.readthedocs.io](https://requests.readthedocs.io/en/latest/)

### 2.2 `BeautifulSoup` 실습
- `BeautifulSoup`은 HTML 및 XML 파일을 파싱하여 원하는 데이터를 추출하는 라이브러리
- 태그, 속성명을 활용하여 특정 요소를 선택하는 방법 실습(soup_try.html -> soup_try.ipynb)
- webcrawl_04_bs4.ipynb

## 🛠 실습 과제

### 1️⃣ [quotes.toscrape.com](https://quotes.toscrape.com/)에서 인용구 및 작가 정보 크롤링
- 10페이지 분량의 데이터를 수집
- 인용구(`quote`), 작가(`author`), 태그(`tags`) 추출 후 데이터프레임 생성

### 2️⃣ 다양한 사이트에서 크롤링 실습
| 사이트 | 설명 |
|--------|-----|
| [quotes.toscrape.com](https://quotes.toscrape.com) | 인용구 스크래핑 연습용 사이트 |
| [books.toscrape.com](https://books.toscrape.com) | 책 정보 스크래핑 연습용 사이트 |
| [news.ycombinator.com](https://news.ycombinator.com) | 해커 뉴스, 기술 관련 뉴스 및 토론 |
| [example.com](https://example.com) | 단순 HTML 구조 테스트 사이트 |
| [httpbin.org](https://httpbin.org) | HTTP 요청 테스트 사이트 |

---

## ⚙️ How to do (실습 방법)

### ✅ 1. 웹 페이지 구조 확인
- **F12 (개발자 도구) 사용**하여 태그와 속성 분석
- `Copy Element` 기능 활용
- VScode Copilot과 함께 vibe coding 실습

### ✅ 2. HTML 구조 학습 참고 자료
- [HTML 태그 및 요소 구조](https://www.tcpschool.com/html/html_intro_elementStructure)

### ✅ 3. 필요한 라이브러리 설치
```bash
pip install requests beautifulsoup4 pandas

