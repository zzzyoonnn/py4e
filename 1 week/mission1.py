year = int(input("몇년에 태어났나요?: "))
birth = input("생일이 지났나요? (O, X): ")
current_year = 2023

if birth == 'O':
    print(current_year - year)
else : 
    print(current_year - year - 1)