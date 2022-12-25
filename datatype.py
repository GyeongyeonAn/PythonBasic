# int(정수)형
a = 5
b = -5
c = 0
print(type(a), type(b), type(c))

# float(실수)형
d = 5.5
e = -5.5
f = 0.0
print(type(d), type(e), type(f))

# 과학적 표기법
g = 1.234567e5
print(g)

# complex(복소수)형
# a + bj

# 문자열
text = "String \"Data\" Type"
print(text)

# 탈출문자
# \', \", \\, \n, \r, \t
text = "\t\'Java\' \"Python\" \
\n\tis Easy"
print(text)

text = """python
is
Easy"""
print(text)

# bool형
is_ture = True
is_false = False

# 정수형으로 변환
print(int(123.92))
print(int(123.9123213))
print(int(123.93435))
print(int(True))
print(int(False))
print(type(int("284242")))

# 실수형으로 변환
print(float(200))
print(float(3))
print(float(True))
print(float(False))
print(float("23.234354"))
print(float("23"))

# 문자열로 변환
print(type(str(12312)))
print(type(str(12312.3434)))
print(type(str(True)))
print(type(str(False)))

# bool형으로 변환
# false
print(bool(0))
print(bool(0.0))
print(bool(""))
# true
print(bool(1))
print(bool(1.0))
print(bool("str"))
print(bool("1231"))
