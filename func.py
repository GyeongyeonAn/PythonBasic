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
