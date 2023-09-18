import requests
from bs4 import BeautifulSoup

url = "https://dorm.kumoh.ac.kr/dorm/restaurant_menu01.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser') 


for tr_tag in soup.find_all('tr'):
    row_number = 0
    order_td = soup.new_tag('td')
    order_td.string = str(row_number)
    tr_tag.insert(0, order_td)
    row_number += 1

days = ['월', '화', '수', '목', '금']

for i, day in enumerate(days):
    print(f"{i+1}.{day}\t", end='')

print()

userInput = int(input("요일을 선택하세요 : "))
print()

if userInput == 1:
    print("<월요일 식단>")
elif userInput == 2:
    print("<화요일 식단>")
elif userInput == 3:
    print("<수요일 식단>")
elif userInput == 4:
    print("<목요일 식단>")
elif userInput == 5:
    print("<금요일 식단>")


    
list_result = []
day = ['월','화','수','목','금','토','일']

for days in day:
    for i in days:
        list_result[day][i]=
    
    
food = soup.find_all("ul", {"class": "s-dot"})
if food:
    for ul in food:
        menu_items = ul.find_all("li")
        for menu in menu_items:
            print(row_number)
            print(f"{menu.find_previous('td').text.strip()}. {menu.text.strip()}")
else:
    print("메뉴 정보를 찾을 수 없습니다.")
