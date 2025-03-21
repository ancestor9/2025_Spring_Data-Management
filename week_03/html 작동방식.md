# 웹 페이지 렌더링 과정과 Beautiful Soup 한계
### - robots.txt 규칙 예제, www.google.com.robots.txt

## 주요 단계별 HTML 상태

| 단계 | Source HTML | Rendered HTML | Beautiful Soup 가능 여부 |
|---|---|---|---|
| 1. 사용자 요청 | 아직 없음 (요청 중) | 아직 없음 | - |
| 2. HTML 다운로드 | 서버가 생성한 정적 HTML | 아직 생성되지 않음 | ✅ |
| 3. HTML 파싱 | 원본 HTML 그대로 유지 | 기본 DOM 구조 생성 | ✅ |
| 4. CSS 적용 | 원본 HTML 그대로 유지 | CSS 스타일 적용된 상태 | ❌ (CSSOM 처리 불가) |
| 5. JavaScript 실행 | 원본 HTML 변화 없음 | JS로 DOM 조작 및 데이터 추가 | ❌ (JS 실행 불가) |
| 6. 레이아웃 및 페인팅 | 원본 HTML 변화 없음 | 최종 완성된 화면 | ❌ (렌더링 불가) |

## 핵심 정리

- **Source HTML**: 서버에서 받은 원본 정적 HTML (JavaScript 실행 전)
- **Rendered HTML**: 브라우저가 JavaScript 실행 후 최종 완성된 HTML (동적 데이터 포함)
- **Beautiful Soup 한계**: 정적 웹페이지(Source HTML)만 스크래핑 가능
- **해결 방법**: 동적 콘텐츠는 `Selenium`이나 `Playwright` 같은 도구 사용 필요

👉 결론: `bs4`는 **정적 웹페이지**(Source HTML)만 스크래핑 가능!  
👉 **동적 웹페이지(Rendered HTML)는 Selenium 같은 도구를 사용해야 함!** 
🚀 naver_cartoon.py로 확인하기기
