import requests # requests 라이브러리를 가져옴
from bs4 import BeautifulSoup # BeautifulSoup 클래스를 bs4 라이브러리에서 가져옴

url = "https://dorm.kumoh.ac.kr/dorm/restaurant_menu01.do" # 웹 페이지의 URL을 변수에 저장
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"} # HTTP 요청 헤더를 정의하는 딕셔너리를 생성
res = requests.get(url, headers=headers) # requests 라이브러리를 사용하여 HTTP GET 요청을 보냄(이에 대한 응답은 res변수에 저장)

if res.status_code == 200: # HTTP GET 요청이 수락(200)되었을 경우 아래 코드를 실행
    soup = BeautifulSoup(res.text, 'lxml')

    # "중식","석식" 항목을 모두 찾고 대응되는 변수에 할당
    lunch_menu_p = soup.find_all('p', text='중식')
    dinner_menu_p = soup.find_all('p', text='석식')

    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"] # 리스트에 각 요일 저장
    
    # enumerate(zip(lunch_menu_p, dinner_menu_p), start=0)를 사용하여 lunch_menu_p와 dinner_menu_p를 병렬로 순회하면서, 각 요일에 해당하는 메뉴 정보를 가져와 출력
    for i, (lunch_p, dinner_p) in enumerate(zip(lunch_menu_p, dinner_menu_p), start=0): 
        day_of_week = days[i] # day_of_week 변수에 현재 요일을 할당
        print(f"\n{day_of_week} 식단\n")
        
        print(f"중식\n")
        lunch_menu_items = lunch_p.find_next('ul', class_='s-dot').find_all('li') # lunch_menu_items 변수에 "중식" 메뉴 항목을 저장하고, 각 항목의 텍스트를 가져와 출력
        for item in lunch_menu_items:
            print(item.get_text(strip=True))
        
        print(f"\n석식\n")
        dinner_menu_items = dinner_p.find_next('ul', class_='s-dot').find_all('li')
        for item in dinner_menu_items:
            print(item.get_text(strip=True))
else:
    print('요청이 거절되었습니다.') # 만약 HTTP GET 요청이 거절되면, "요청이 거절되었습니다." 메시지가 출력
    

 
 