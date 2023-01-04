# while문
i = 0
print("while 문")
while i < 5:
    i += 1
    print(i)
else:
    print("값이 {}이상으로 종료합니다.".format(i))


# list while문
fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
fruit = "사과"
while fruit in fruits:
    fruits.remove(fruit)
print(fruits)
print("{}을 모두 제거했습니다.".format(fruit))


# 최소값, 최대값 입력 받고, 그 사이의 숫자 중 짝수와 홀수 리스트 출력하기
max = 10
min = 1
odd_list = []
even_list = []
num = min
if min < max:
    while num <= max:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
        num += 1
    print("홀수 리스트 {}".format(odd_list))
    print("짝수 리스트 {}".format(even_list))
else:
    print("최대값 {}이 최소값 {}보다 크지 않습니다.".format(max, min))


# range 함수
# 0 부터 9 까지 숫자 반환
numbers = list(range(0, 10))
print(numbers)
# -10 부터 -1 까지 숫자 반환
numbers = list(range(-10, 0))
print(numbers)
# -10 부터 4 까지 숫자 반환
# // 몫 연산 반환값 정수
numbers = list(range(-10, 10//2))
print(numbers)


# for문
for i in range(1, 10+1):
    print(i)

for i in "일이삼사오":
    print(i)

fruits = ["사과", "딸기", "바나나"]
for i in fruits:
    print("과일 바구니에 {}가 들어있습니다.".format(i))


# 1부터 30까의 수 중에서 3의 배수들의 합을 구하시오.
sum = 0
for i in range(1, 30+1):
    if (i % 3 == 0):
        print("{} + {} = ".format(sum, i), end="")
        sum += i
print(sum)


# 딕셔너리 for문 사용
coffee = {"아메리카노": 2500, "라떼": 3000, "자바": 2500}
for i in coffee.values():
    print(i)


# 리스트 인덱스와 요소 enumerate로 출력하기
for i, j in enumerate(fruits):
    print(f"{i+1}번째 과일은 {j}입니다.")


# 중첩 for문
list_2nd = [[1, 2, 3], ["a", "b", "c"]]
for i in list_2nd:
    for j in i:
        print(j)

# 딕셔너리에 차가운 메뉴와 뜨거운 메뉴 각각 출력하기
menu = {"아이스 아메리카노": 3000, "아메리카노": 2500,
        "아이스 라떼": 4000, "라떼": 3500, "아이스크림": 8000}

print("차가운 메뉴")
for key, value in menu.items():
    if key[0:3] == "아이스":
        print("제품 : {}, 가격 {}".format(key, value))

print("뜨거운 메뉴")
for key, value in menu.items():
    if key[0:3] != "아이스":
        print("제품 : {}, 가격 {}".format(key, value))
