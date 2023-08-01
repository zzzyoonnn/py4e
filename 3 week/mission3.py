def find_even_number(first, second) :
    #print(first, second)
    numbers = [i for i in range(first, second + 1)]
    #print(numbers)
    even_numbers = [j for j in numbers if j % 2 == 0]
    #print(even_numbers)

    j = len(numbers)
    #print(j)
    if j % 2 == 1:
        median = numbers[j // 2]
        print(median, "중앙값")
        for even_number in even_numbers:
            if even_number == median:
                print(even_number, "짝수")
                print(even_number, "중앙값")
            else:
                print(even_number, "짝수")
    else:
        median = None
        for even_number in even_numbers:
            print(even_number, "짝수")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)