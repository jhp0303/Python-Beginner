# 변수를 선언합니다.
example_a = "문자열"
example_b = { "키A":"값A", "키B":"값B"}
example_c = range(10)

# 출력합니다.
print("# 문자열에 반복 적용")
for char in example_a:
    print("-", char)

print()
print("# 딕셔너리에 반복 적용")
for key in example_b:
    print("-", key)

print()
print("# 범위에 반복 적용")
for i in example_c:
    print("-", i)