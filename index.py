# index

# 앞부터 추출
print("index"[0])
print("index"[1])
print("index"[2])
print("index"[3])
print("index"[4])

# 뒤부터 추출
print("index"[-5])
print("index"[-4])
print("index"[-3])
print("index"[-2])
print("index"[-1])

str_ = "0123456789"

print(str_[0])
print(str_[1])
print(str_[2])
print(str_[3])
print(str_[4])
print(str_[5])
print(str_[6])
print(str_[7])
print(str_[8])
print(str_[9])

# str slicing
# [0:8] : 0부터 7까지
print("0123456789"[0:8])

print("0123456789"[0:])
print("0123456789"[:10])
print("0123456789"[:])
print("0123456789"[-10:])

# step
print("0123456789"[0:10:2])

print("0123456789"[::-3])

str_slice = "Python"
print(str_slice[0:]+str_slice[::-1])
print(str_slice[1:5]+str_slice[0]+str_slice[5])
