# 예외 처리하기
def division():
    try:
        num1 = int(input("첫번째 정수를 입력해주세요 > "))
        num2 = int(input("두번째 정수를 입력해주세요 > "))
        result = num1 / num2
    except Exception:
        print("오류가 발생했습니다.")
    # 오류가 아닌 경우에 return을 사용
    else:
        print("정상적으로 나누기 함수가 호출되었습니다.")
        return print(f"{num1}을 {num2}로 나눈 값은 {result}입니다.")
    # finally는 무조건 출력이 됨
    finally:
        print("함수가 끝났습니다.")


division()


class Toilet:
    def __init__(self):
        self.using = False

    def in_use(self):
        if self.using == False:
            print("화장실을 사용했습니다.")
            self.using = True
        else:
            raise Exception("안에 사람이 있어요.")  # 예외 일으키기

    def not_in_use(self):
        self.using = False
        print("안에 사람이 없습니다.")


def not_in_use(self):
    self.using = False
    print("안에 사람이 없습니다.")


man = Toilet()

while True:
    use = input("화장실을 사용하겠습니까?(y/n")
    try:
        if use == "y":
            man.in_use()
        else:
            man.not_in_use()
    except Exception as e:
        print(e)
