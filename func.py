# 함수
def menu():
    print("오늘의 메뉴")
    print("오늘 점심메뉴는 제육볶음입니다.")


menu()


def add(num1, num2, num3):
    print(num1, num2, num3)


add(1, 2, 3)


def addText(text1, text2):
    ''' 문자열 두개를 입력받아서 합쳐서 출력
    args
        text1 : 성을 받는 문자열
        text2 : 이름을 받는 문자열
    '''
    print(text1, text2)


addText("홍", "길동")


def game(text):
    while True:
        print(text)
        keyword = input("끝말을 이어주세요 > ")
        if text[-1] == keyword[0]:
            text = keyword
        else:
            print("끝말이 이어지지 않았습니다.")
            break


game("함수호출")


# 지역변수 (Local Variable)
def jeju_potato():
    potato = "고구마"
    print(potato)


jeju_potato()

# 전역변수(Global Variable)
potato = "감자"


def jeju_potato_2():
    global potato
    print(potato)
    potato = "고구마"
    print(potato)


jeju_potato_2()


# 매개변수에 기본값 지정해주기
# 매개변수 기본값을 맨 앞에 매개변수로 지정해준 경우
# 함수를 호출할 때, 매개변수를 생략할 수 없게 된다.


def add(num1, num2=20):
    return num1 + num2


print(add(10))


a, b = 20, 40


def add_2(num1=a, num2=b):
    return num1 + num2


print(add_2())


# 가변 매개변수
# 일반 매개변수 앞에 올 수 없다
# add(*argc, num) (x)


def add(*argc):
    return argc


# 튜플 형태로 반환된다.
print(add(10, 20, 30, 40))


# 키워드 매개변수
# 키워드 = 특정값 형태로
def star_player(**kwargs):
    for i, j in kwargs.items():
        if "서장훈" in kwargs.values():
            print("저는 LG팬이라 서장훈을 좋아했어요")
        else:
            print("{}는 역시 {}지".format(i, j))


star_player(농구="서장훈")


# 모든 종류 매개변수 사용
def func_a(name, *argc, address="한국", **kwargs):
    print(name, argc, address, kwargs)


func_a("홍길동", "옛날", "사람", address="한양", 직업="도둑")


# 숫자 나열에서 최대값, 최소값 추출하기
# def max_min_search(*numbers):
#     max = numbers[0]
#     min = numbers[0]
#     for number in numbers:
#         if max < number:
#             max = number
#         if min > number:
#             min = number
#     return max, min

def max_min_search(*numbers):
    return max(numbers), min(numbers)


print(max_min_search(15, 30, 4, 600, 7, 80, 32))
