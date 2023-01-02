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
fruit = input("빼낼 과일을 입력하세요 > ")
while fruit in fruits:
    fruits.remove(fruit)
print(fruits)
print("{}을 모두 제거했습니다.".format(fruit))


# 최소값, 최대값 입력 받고, 그 사이의 숫자 중 짝수와 홀수 리스트 출력하기
max = int(input("최대값 입력 > "))
min = int(input("최소값 입력 > "))
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
