
list_a = [1, 2, 3, 4]
list_b = ["a", "b", "c"]
list_c = [True, False]
list_d = [1, "a", True]
print(list_a)
print(list_b)
print(list_c)
print(list_d)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[0])
print(numbers[3:5])
print(numbers[1:])
print(numbers[-3:-1])

list_lan = ["JAVA", "C", "PYTHON", "Go"]
print(list_lan[0][2])
print(list_lan[2][2:4])

list_lan[1] = "C++"
print(list_lan)

list_lan[1:3] = ["C#", "PYTHON3"]
print(list_lan)

# 리스트 요소 개수 출력
print(len(list_lan))

# 리스트 맨 뒤에 새로운 요소 추가
list_lan.append("Ruby")
print(list_lan)

# 리스트 안에 리스트 요소 추가
list_a = [1, 2, 3]
list_lan.append(list_a)
print(list_lan)

# 리스트 요소를 추출하여 리스트 안에 추가
list_lan.extend(list_a)
print(list_lan)

# 문자열을 extend로 추가하는 경우 문자열의 각 문자 하나씩 리스트에 저장됨
list_lan.extend("JavaScript")
print(list_lan)

# 원하는 위치에 데이터를 리스트에 삽입
list_lan.insert(0, "R")
print(list_lan)

# 제일 뒤에 있는 요소를 반환해주고 삭제
print(list_lan.pop())
print(list_lan)

# 원하는 요소 삭제
list_lan.remove("PYTHON3")
print(list_lan)

# 원하는 요소 위치로 삭제
del list_lan[1]
print(list_lan)

# 리스트 오름차순으로 정렬
numbers = [1000, 5000, 160, 100, 20, 3450]
numbers.sort()
print(numbers)

# 리스트 요소 역순으로 변경
numbers.reverse()
print(numbers)

# 리스트 내림차순으로 정렬
numbers.sort(reverse=True)
print(numbers)

names = ["홍길동", "이승철", "김개똥"]
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# 리스트안에 요소 찾기
list_lan = ["Java", "C", "Python", "Go"]
numbers = [1, 200, 3, 50, 5, 77, 7, 55, 9]
print(50 in numbers)
print("C" not in list_lan)
print("Java Script" not in list_lan)

# 2차원 리스트
td_number = [[10, 20, 30], [1, 2, 3]]
print(td_number)
print(td_number[0][1])
