import os
import time



def play_type_game(path):

    with open(path,"r") as f:
        starting_count = 0

# while문 버전 (용량이 클때 좋음)

        while True:

            line = f.readline()
            if line == "":
                break

            line = line.strip()

            if line != "":  # line에 문자열이 있는 경우

                starting_count += len(line)

                while True: # "참"일동안 진행

                    print("\n",line)
                    start_time = time.time()
                    user = input(">")
                    end_time = time.time()

                    if line == user: # line == user 면 멈추고 다음으로 이어 진행
                        break
                    else: # 거짓일 경우 똑같은거 계속 반복함. 맞을때까지.
                        print("잘못입력했습니다.\n")


        t_time = end_time-start_time
        print(f"총 {t_time}초 걸렸습니다.")
        taza = starting_count/t_time*60
        print(f"타수:{int(starting_count/t_time*60)}/분")