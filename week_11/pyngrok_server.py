# pyngrok_server.py
import os
import subprocess
import time
from pyngrok import ngrok, conf
from dotenv import load_dotenv
load_dotenv()

def start_http_server(port=8000):
    """HTTP 서버를 백그라운드에서 시작합니다."""
    print(f"포트 {port}에서 HTTP 서버를 시작합니다...")
    # 현재 디렉토리에 있는 파일들을 서빙하는 HTTP 서버 시작
    # 백그라운드에서 실행하기 위해 subprocess 사용
    if os.name == 'nt':  # Windows
        subprocess.Popen(f"python -m http.server {port}", shell=True)
    else:  # Linux/Mac
        subprocess.Popen(f"python -m http.server {port} &", shell=True)
    # 서버가 시작될 때까지 잠시 대기
    time.sleep(2)
    print(f"HTTP 서버가 포트 {port}에서 실행 중입니다.")

def create_ngrok_tunnel(port=8000):
    """ngrok 터널을 생성하여 로컬 서버를 인터넷에 공개합니다."""
    print(f"포트 {port}에 대한 ngrok 터널을 설정합니다...")
    # ngrok 설정 - API 키(인증 토큰) 안전하게 등록
    # 환경 변수에서 토큰을 가져오거나 사용자 입력 받기
    import os
    # 1. 환경 변수에서 토큰 확인
    ngrok_token = os.environ.get("NGROK_AUTH_TOKEN")
    # 2. 환경 변수에 없으면 사용자에게 입력 요청
    if not ngrok_token:
        import getpass
        print("ngrok 인증 토큰이 필요합니다 (입력 내용은 화면에 표시되지 않습니다)")
        ngrok_token = getpass.getpass("ngrok 인증 토큰을 입력하세요: ")
    # 토큰 설정
    if ngrok_token:
        conf.get_default().auth_token = ngrok_token
    else:
        print("경고: ngrok 인증 토큰이 제공되지 않았습니다. 제한된 기능으로 실행됩니다.")
    
    # HTTP 프로토콜을 사용하여 지정된 포트에 대한 터널 생성
    public_url = ngrok.connect(port, "http")
    print(f"ngrok 터널이 생성되었습니다!")
    print(f"공개 URL: {public_url}")
    
    return public_url

def main():
    port = 8000
    
    # 1. HTTP 서버 시작
    start_http_server(port)
    
    # 2. ngrok 터널 생성
    public_url = create_ngrok_tunnel(port)
    
    print("\n이제 다음 URL을 통해 HTTP 서버에 접근할 수 있습니다:")
    print(f"➡️  {public_url}")
    print("\n종료하려면 Ctrl+C를 누르세요...")
    
    try:
        # 터널이 활성 상태로 유지되도록 프로그램을 계속 실행
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 사용자가 Ctrl+C를 눌러 종료할 때 정리 작업
        print("\n프로그램을 종료합니다...")
        ngrok.kill()  # ngrok 프로세스 종료

if __name__ == "__main__":
    main()