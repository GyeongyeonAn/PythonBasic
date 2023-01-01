# input 함수 : 값을 입력받음
text = input("성을 입력해주세요. > ")
text2 = input("이름을 입력해주세요. > ")
print(text + text2)

number = input("첫번째 정수를 입력해 주세요. > ")
number2 = input("두번째 정수를 입력해 주세요. > ")

# input으로 받는 값은 string 형이기 때문에 숫자 연산은 문자열 연결하기 연산이 수행된다.
print(number + number2)

# 형번환을 통해 숫자 연산을 수행한다.
print(int(number) + int(number2))

# if 조건문
if True:
    print("실행할 문장입니다.")

study_time = int(input("오늘의 공부시간을 입력해주세요 > "))

if 6 >= study_time >= 3:
    print("Python 공부를 한다.")

elif study_time < 3:
    print("오늘은 시간이 별로 없으니깐 놀자!")

odd = input("정수를 입력해주세요 > ")

if odd % 2 == 1:
    print("입력하신 정수는 홀수 입니다.")
else:
    print("입력하신 정수는 짝수 입니다.")

domain = input("웹 사이트의 주소를 입력해주세요 > ")
nation = domain.split(".")

if nation[-1] == "kr":
    print("한국")
elif nation[-1] == "uk":
    print("영국")
elif nation[-1] == "com":
    print("기업")
elif nation[-1] == "org":
    print("기관")
else:
    print("알 수 없음")
