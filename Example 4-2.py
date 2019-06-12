# 변수를 선언합니다.
result = ["1"]

# 10번째까지의 개미 수열을 구합니다.
for i in range(10):
    # 과정을 볼 수 있게 출력하겠습니다.
    print("".join(result))

    # 변수를 선언합니다.
    next = []   # 다음 단계의 개미 수열을 구해 넣을 리스트
    number = result[0]  # 현재 숫자
    count = 0   # 현재 숫자의 출현 개수

    # 숫자를 확인하고 개수를 계산
    for item in result:
        # 같은 요소 반복이라면 개수를 1만큼 증가
        if number == item:
            count += 1
        # 다른 요소가 등장하면 기존에 세던 것을 리스트에 추가하고 초기화
        else:
            next.append(number)
            next.append(str(count))
            number = item
            count = 1
    # 마지막 숫자 추가
    next.append(number)
    next.append(str(count))

    # 다음 단계를 구할 수 있께 result를 교체합니다.
    result = next

# 최종 결과를 출력합니다.
print()
print("10번째 개미수열:", "".join(result))