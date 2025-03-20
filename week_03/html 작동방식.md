| 단계 | 설명 | Source HTML (원본 HTML) | Rendered HTML (최종 HTML) | bs4 한계 |
|------|---------------------------|----------------------------------|----------------------------------|---------------------------|
| **1. 사용자가 웹페이지 요청** | 사용자가 브라우저 주소창에 URL 입력 또는 링크 클릭 시 요청 발생 | `requests.get(url)`로 HTML 요청 가능 | - | ✅ `requests.get(url)` 가능 |
| | - HTTP/HTTPS 프로토콜을 사용하여 요청 | | | |
| | - GET, POST 등의 HTTP 메서드 사용 | | | |
| | - DNS가 도메인 네임을 해당 서버의 IP 주소로 변환 | | | |
| **2. 서버와 통신하여 HTML 다운로드** | 브라우저가 DNS를 통해 서버 IP 확인 후 웹 서버와 연결 | 서버가 생성한 정적 HTML | - | ✅ `bs4`로 HTML 가져올 수 있음 |
| | - 웹 서버(Apache, Nginx 등)가 요청을 처리하고 HTML 반환 | | | |
| | - 동적 웹페이지(PHP, Node.js, Python 등)는 서버에서 HTML 생성 후 응답 | | | |
| | - CDN(Content Delivery Network)이 캐싱된 HTML을 제공할 수도 있음 | | | |
| **3. 브라우저가 HTML을 파싱 (Parsing)** | 브라우저가 HTML을 한 줄씩 읽어 DOM 트리 생성 | `Source HTML`만 존재, JavaScript 미실행 | 브라우저가 HTML을 해석하여 `DOM` 트리 생성 | ✅ `bs4`로 파싱 가능 |
| | - DOM(Document Object Model) 트리 생성 | | | |
| | - `<script>` 태그를 만나면 HTML 파싱이 중단되고 스크립트 실행 | | | |
| **4. CSS 요청 및 스타일 적용** | HTML 파싱 중 `<link>` 태그를 만나면 CSS 다운로드 및 적용 | `<link>` 태그만 있음 | CSS 적용된 화면이 렌더링됨 | 🔴 `bs4`는 CSSOM을 다루지 않음 |
| | - CSS 파일을 파싱하여 CSSOM(CSS Object Model) 트리 생성 | | | |
| | - DOM 트리와 CSSOM 트리를 결합하여 Render Tree 구성 | | | |
| **5. JavaScript 실행** | HTML 파싱 중 `<script>` 태그를 만나면 스크립트 실행 | JS가 실행되기 전이라 `<div>` 같은 요소가 비어 있음 | JavaScript 실행 후 새로운 데이터 추가됨 | 🔴 `bs4`는 JS 실행 불가능! |
| | - JavaScript가 DOM을 조작할 수 있어 HTML 파싱이 중단될 수 있음 | | | |
| | - `async`: 다운로드 후 즉시 실행, `defer`: HTML 파싱 완료 후 실행 | | | |
| **6. 레이아웃(배치, Layout) 단계** | Render Tree를 기반으로 각 요소의 크기와 위치 계산 | CSS와 JS가 적용되지 않음 | 최종적으로 렌더링된 화면이 완성됨 | ❌ `bs4`는 브라우저가 아님, 화면 렌더링 못함 |
| | - 브라우저 뷰포트 크기에 따라 요소 위치 결정 | | | |
| | - 상대 크기(%, em 등)는 부모 요소 기준으로 계산 | | | |
| **7. 페인팅(Painting) 단계** | 화면에 픽셀을 그리는 단계 | | | |
| | - 계산된 위치와 스타일을 GPU에 전달하여 렌더링 | | | |
| | - 색상, 배경, 테두리, 그림자 등의 스타일 적용 | | | |
| **8. 합성(Compositing) 및 화면 출력** | 모든 요소를 최적화하여 GPU가 레이어별로 그린 후 화면 출력 | JavaScript 실행 결과가 없음 | JavaScript 실행 후 최종적으로 완성된 HTML | 🔴 `bs4`는 JavaScript 실행 후의 HTML을 가져올 수 없음 |
| | - CSS 애니메이션, WebGL, 3D 변환 등 효과 적용 | | | |
| | - 스크롤 시 최적화된 부분만 다시 그림 (Repaint) | | | |

## 💡 쉽게 말하면?
- `Source HTML` → **서버에서 받은 원본 HTML** (JavaScript 미실행, 데이터 없음)  
- `Rendered HTML` → **브라우저가 JavaScript 실행 후 최종 완성된 HTML** (데이터 포함)  
- `bs4`는 **Rendered HTML을 가져올 수 없어서** **JavaScript가 추가하는 데이터는 못 가져옴**  

## 📌 해결 방법
✅ **API 직접 호출** → `F12 > Network > XHR` 에서 API 요청 URL 찾아 `requests.get()` 사용  
✅ **Selenium 사용** → 실제 브라우저 띄워 JavaScript 실행 후 HTML 가져오기  
✅ **Headless Browser 활용** → `playwright` 같은 최신 기술로 빠르게 JS 실행  

👉 결론: `bs4`는 **정적 웹페이지**(Source HTML)만 스크래핑 가능!  
👉 **동적 웹페이지(Rendered HTML)는 Selenium 같은 도구를 사용해야 함!** 🚀
