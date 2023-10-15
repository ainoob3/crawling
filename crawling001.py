import requests # requests 라이브러리를 가져옵니다
from bs4 import BeautifulSoup # BeautifulSoup 클래스를 bs4 라이브러리에서 가져옵니다

url = "https://dorm.kumoh.ac.kr/dorm/restaurant_menu01.do" # 웹 페이지의 URL을 변수에 저장합니다
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"} # HTTP 요청 헤더를 정의하는 딕셔너리를 생성합니다
res = requests.get(url, headers=headers) # requests 라이브러리를 사용하여 HTTP GET 요청을 보냅니다(이에 대한 응답은 res변수에 저장됩니다)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')

    # "중식" 항목을 모두 찾음
    lunch_menu_p = soup.find_all('p', text='중식')
    dinner_menu_p = soup.find_all('p', text='석식')

    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    
    for i, (lunch_p, dinner_p) in enumerate(zip(lunch_menu_p, dinner_menu_p), start=0):
        day_of_week = days[i]
        print(f"\n{day_of_week} 식단\n")
        
        print(f"중식\n")
        lunch_menu_items = lunch_p.find_next('ul', class_='s-dot').find_all('li')
        for item in lunch_menu_items:
            print(item.get_text(strip=True))
        
        print(f"\n석식\n")
        dinner_menu_items = dinner_p.find_next('ul', class_='s-dot').find_all('li')
        for item in dinner_menu_items:
            print(item.get_text(strip=True))
else:
    print('요청이 거절되었습니다.')
    

 
 