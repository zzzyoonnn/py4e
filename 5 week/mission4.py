from datetime import datetime, timedelta

def after_100(month, day, weekday):
    # 요일 이름을 인덱스로 매핑
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    weekday_index = weekdays.index(weekday)

    # 입력된 월, 일, 요일로부터 날짜 생성
    base_date = datetime(datetime.now().year, month, day)

    # 요일 조정
    while base_date.weekday() != weekday_index:
        base_date += timedelta(days=1)

    # 100일 뒤의 날짜 계산
    future_date = base_date + timedelta(days=100)
    return future_date

# 사용자 입력 받기
print("ex) 입력 : 6,21,월")
input_month, input_day, input_weekday = input("after_100 :").split(',')
print("우리의 기념일은 ", input_month,"월 ", input_day,"일 ", input_weekday, "요일 입니다.")
result_date = after_100(int(input_month), int(input_day), input_weekday)
result_date_str = result_date.strftime('%Y년 %m월 %d일')

# 요일 이름을 한글로 나타내기 위한 리스트 정의
korean_weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
result_weekday = korean_weekdays[result_date.weekday()]  # 날짜의 요일 인덱스로 요일을 가져옴

print("이로부터 100일 뒤의 날짜는", result_date_str, result_weekday, "입니다.")