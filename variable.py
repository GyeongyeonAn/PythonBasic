a, b = 100, 200
a, b = b, a + b
print(a, b)
# 변수 할당 해제
del a, b

text = "Welcome to Python"
print((text + "\n") * 10)

# 이름, 핸드폰 번호, 거주지
name = "안경연"
phone = "010-7627-7444"
adress = "대전시 대덕구"
print(name)
print(phone)
print(adress)

# 식별자(변수 이름) 생성 규칙
# 1. 변수의 이름은 문자, 숫자, 밑줄(_)을 포함할 수 있다.
# 2. 변수의 이름은 숫자로 시작할 수 없다.
# 3. 공백을 포함할 수 없다.
# 4. 예약어(keyward)는 사용할 수 없다.

# 올바른 예
apple = "사과"
apples = "사과들"
apple3 = "사과3개"
app3le = "사3과"
red_apple = "빨간 사과"
very_delicious_red_apple = "아주 맛있는 빨간 사과"

# 잘못된 예
# red apple = "빨간 사과"
# 3apple = "3개의 사과"
# apple! = "사과!"
# apple& = "사과&"
# continue, if... (에약어 사용 불가능)
