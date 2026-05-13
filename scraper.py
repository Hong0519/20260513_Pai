import requests
from bs4 import BeautifulSoup

def run_scraper():
    # 1. 대상 사이트 주소
    url = "https://news.naver.com/section/105"
    
    # 2. 브라우저 정보를 담은 헤더 (접속 거부 방지)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    try:
        # 3. 페이지 데이터 요청
        print(f"데이터를 가져오는 중: {url}")
        response = requests.get(url, headers=headers)
        
        # 4. HTML 분석 시작
        soup = BeautifulSoup(response.text, "html.parser")

        # 5. 뉴스 제목 요소 찾기 (네이버 뉴스 기준 클래스명)
        # .sa_text_strong 은 현재 네이버 뉴스 제목의 CSS 클래스 이름입니다.
        titles = soup.select(".sa_text_strong")

        print("\n=== 오늘의 IT 뉴스 헤드라인 ===")
        for i, title in enumerate(titles[:15], 1):
            print(f"{i}. {title.get_text(strip=True)}")

    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    run_scraper()