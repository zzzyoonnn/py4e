def check_id(id_number):
    if len(id_number) != 14 or id_number[6] != '-':
        print("잘못된 번호입니다.")
        return
    
    gender_digit = int(id_number[7])
    if gender_digit == 1 or gender_digit == 3:
        gender = "남자"
    elif gender_digit == 2 or gender_digit == 4:
        gender = "여자"
    else:
        print("잘못된 번호입니다.")
        return
    
    birth_year_prefix = int(id_number[:2])
    if 0 <= birth_year_prefix <= 23:
        birth_year_input = input("2000년 이후 출생자입니까? (O/X): ")
        if birth_year_input.lower() == 'o':
            if gender_digit == 1 or gender_digit == 2:
                print("잘못된 입력입니다.")
                print("올바른 번호를 넣어주세요")
                return
            else :
                birth_year = 2000 + birth_year_prefix
        elif birth_year_input.lower() == 'x':
            if gender_digit == 3 or gender_digit == 4:
                print("잘못된 입력입니다.")
                print("올바른 번호를 넣어주세요")
            else :
                birth_year = 1900 + birth_year_prefix
        else:
            print("잘못된 입력입니다.")
            return
    else:
        birth_year = 1900 + birth_year_prefix
    
    birth_month = id_number[2:4]
    print(f"{birth_year}년{birth_month}월 {gender}")

a = input("a = ")
check_id(a)


