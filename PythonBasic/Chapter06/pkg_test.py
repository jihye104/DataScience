# import game.sound.echo
# game.sound.echo.echo_test()

# 환경변수 PYTHONPATH에 아래 경로를 설정하거나
# 아래와 같이 파이썬 자체에서 경로를 설정할 수 있다(배포 환경일 경우에 적용)

import sys
sys.path.append("D:/Pywork/DataScience/pkg_test")

from game.sound import echo

def print_hello():
    print("hello")

if __name__ == "__main__":
    print_hello()
    echo.echo_test()


from game.sound.echo import echo_test
echo_test()

from game.sound import *
wav.wav_test()