# 묘듈을 읽어 들입니다.
import textwrap

# 여러 줄 문자열의 들여쓰기를 만들기 위해 구문을 사용해봅니다.
if True:
    # 변수를 선언합니다.
    test = """\
        이런저런
        문자열을
        생성해요"""

        # 출력합니다.
    print("- test:", test)
    print("- textwrap.dedent(test):", textwrap.dedent(test))